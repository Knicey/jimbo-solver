from cards import fromStr
from calculator import determine_highest_hand_ranking, pokerHands

# consider storing this as separate JSON(s)
cases = {
    "fromStr": {
        "1h": ("a", "hearts"),
        "10h": ("10", "hearts"),
        "1hh": ("a", "hearts", "holographic"),
        "1hbl": ("a", "hearts", "base", "blue"),
        "1h_bl": ("a", "hearts", "base", "blue"),
        "1hb_l": ("a", "hearts", "base", "blue"),
        "1h_b": ("a", "hearts", "base", "blue"),
        "1h__b": ("a", "hearts", "base", "base", "bonus"),
        "01difopul": ("a", "diamonds", "foil", "purple", "lucky"),
        "01dpp": ("a", "diamonds", "polychrome", "purple"),
        "14DiamondsPolyPurple": ("a", "diamonds", "polychrome", "purple"),
        "adpoP": ("a", "diamonds", "polychrome", "purple"),
        "acdipp": ("a", "diamonds", "polychrome", "purple"),
        "13s_pl": ("k", "spades", "base", "purple", "lucky"),
        "kings puluck": ("k", "spades", "base", "purple", "lucky"),
        "KSPAD-pl": ("k", "spades", "base", "purple", "lucky"),
    },
    "determine_highest_hand_ranking": {
        "12H,13D,12D,12H": pokerHands.repHands[3],
        "12H,12H,12H,12H,12H": pokerHands.flushFive,
        "12H,12H,12H,13H,13H": pokerHands.fullHouses[True],
        "12H,12H,13H,13H,14H": pokerHands.flush,
        "09H,10H,11H,12H,13H": pokerHands.straights[True],
        "09H,10H,11H,12H,13C": pokerHands.straights[False],
        "09H,09H,09C,12D,12D": pokerHands.fullHouses[False],
        "14H,14D,13D,11H": pokerHands.repHands[2],
        "14H,14D,11D,11H": pokerHands.twoPair,
        "01H,02H,03H,04H,05C": pokerHands.straights[False],
        "10S,jH ,qD ,kD ,aH ": pokerHands.straights[False],
        "1h ,1h ,1h ,1h ,1cw": pokerHands.flushFive,
    }
}


class test_fromStr:
    name = "fromStr"

    def __init__(self, testCases: dict[str, tuple[str, str]] = cases[name]) -> None:
        self.testCases = testCases

    def validate(self):
        for k, v in self.testCases.items():
            card = fromStr(k)
            # print(card, v)
            assert card.rank == v[0]
            assert card.suit == v[1]
            if len(v) >= 3:
                assert card.edition == v[2]
            else:
                assert card.edition == "base"
            if len(v) >= 4:
                assert card.seal == v[3]
            else:
                assert card.seal == "base"
            if len(v) >= 5:
                assert card.enhancement == v[4]
            else:
                assert card.enhancement == "base"
        return True


class test_determine_highest_hand_ranking:
    name = "determine_highest_hand_ranking"

    def __init__(self, testCases: dict[str, str] = cases[name]) -> None:
        self.testCases = testCases

    def validate(self):
        for k, v in self.testCases.items():
            playedHand = k.split(",")
            result = determine_highest_hand_ranking(playedHand)
            assert result == v
        return True


tests = [test_fromStr(), test_determine_highest_hand_ranking()]
verbose = True

for t in tests:
    result = t.validate()
    if result:
        if verbose:
            print(f"All test cases for '{t.name}' passed!")
