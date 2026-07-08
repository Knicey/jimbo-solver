from random import randint
from typing import assert_type


numberRanks = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
faceRanks = ["j", "q", "k"]
ranks = tuple(["a"] + numberRanks + faceRanks)
black_suits = ["spades", "clubs"]
red_suits = ["hearts", "diamonds"]
suits = tuple(black_suits + red_suits)
editions = ("base", "foil", "holographic", "polychrome")
seals = ("base", "gold", "red", "blue", "purple")
enhancements = ("base", "bonus", "mult", "wild", "glass", "steel", "stone", "gold", "lucky")


class PlayingCard:
    def __init__(self, rank: str, 
                 suit: str, 
                 edition: str = "base", 
                 seal: str = "base", 
                 enhancement: str = "base", 
                 seeded: int = 0,
                 hikerUpgrade: int = 0) -> None:
        #probably a more elegant way to do this
        assert rank in ranks
        assert suit in suits
        assert edition in editions
        assert seal in seals
        assert enhancement in enhancements
        assert hikerUpgrade >= 0
        #consider handling assertion errors

        self.rank = rank
        self.suit = suit
        self.edition = edition
        self.seal = seal
        self.enhancement = enhancement
        self.hikerUpgrade = hikerUpgrade
        self._chips = 0
        self._mults = 0
        self.multmult = 1.5 if self.edition == "polychrome" else 1
        self.seeded = seeded
    
    def __repr__(self):
        s = f"{self.rank.upper()} of {self.suit.title()}"
        if self.edition != "base": s += f", {self.edition.title()}"
        if self.seal != "base": s += f", {self.seal.title()}"
        if self.enhancement != "base": s += f", {self.enhancement.title()}"
        if self.hikerUpgrade > 0: s += f", Hiker +{self.hikerUpgrade}"
        return s

    @property
    def chips(self) -> int:
        c = 0
        if self.enhancement == "stone": c = 50 #could change this to += for consistency
        else:
            if self.enhancement == "bonus": c += 30
            chipsByRank = {"a":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "j":10, "q":10, "k":10}
            c += chipsByRank[self.rank]
        c += self.hikerUpgrade
        if self.edition == "foil": c += 50
        if self.seal == "red": c *= 2 #won't work if card is modified after scoring, e.g. hiker
        self._chips = c
        return self._chips
    
    @property
    def mults(self) -> float:
        #if seeded is 1..4, lucky mult triggers:
        # seeded = 1 => first time only
        # seeded = 2 => second time only
        # seeded = 3 => both times
        # seeded = 4 => zero times
        #behavior only matters for lucky cards
        #everything else triggers normal RNG
        seeded = self.seeded
        m = 0
        r = 2 if self.seal == "red" else 1
        for it in range(r):
            if self.enhancement == "mult": m += 4
            elif self.enhancement == "lucky":
                if 1 <= seeded and seeded <= 4:
                    if (seeded >> it) & 1 == 1:
                        m += 20
                else:
                    seed = randint(1, 5)
                    if seed == 1: m += 20
            if self.edition == "holographic": m += 10
        self._mults = m
        return self._mults


deckTypes = ("base", "abandoned", "checkered", "random") #verify name of last deck type

class Deck:
    def __init__(self, cardSet: set[PlayingCard]) -> None:
        self._cards = cardSet
        self.remaining = len(cardSet)
    
    @property
    def cards(self):
        """
        Returns the set of `PlayingCard`s within the deck
        Does NOT affect the contents
        """
        return self._cards
    @cards.setter
    def cards(self, newCards: set[PlayingCard]) -> set[PlayingCard]:
        """
        Adds the set of `PlayingCard`s to the deck
        Returns the contents of the deck, including new additions
        """
        return self._cards.union(newCards)
    @cards.deleter
    def cards(self, remCard: PlayingCard):
        """
        Removes the specified `PlayingCard` object from the deck
        Throws an error if no such card was in the deck
        """
        self._cards.remove(remCard)
    @cards.getter
    def draw(self) -> PlayingCard:
        """
        Removes an arbitrary `PlayingCard` from the deck and returns it
        Throws an error if the deck is empty
        """
        return self._cards.pop() #this might be very bad rng, but it's easy


def generateDeck(d: str = "base") -> set[PlayingCard]:
    assert d in deckTypes
    cardSet = set()
    if d != "random":
        filteredRanks = ranks
        filteredSuits = suits
        if d != "base":
            if d == "abandoned": filteredRanks = ["a"] + numberRanks
            elif d == "checkered": filteredSuits = ["spades", "hearts"] * 2
        for r in filteredRanks:
            for s in filteredSuits:
                #different objects get hashed separately, even if they have the same attributes
                cardSet.add(PlayingCard(r, s))
    else: 
        #TODO
        #need to look at how Balatro generates it
        pass
    return cardSet
