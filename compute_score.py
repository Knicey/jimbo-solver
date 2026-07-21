from cards import PlayingCard, ranks


def score_all_cards(hand: tuple[PlayingCard, ...]) -> tuple[PlayingCard, ...]:
    """
    Some hand types are trivial and always require all 5 cards to be played.
    

    Without Four Fingers
    - Straight
    - Flush
    - Straight Flush

    Always
    - Full House
    - Flush House (hand must be a full house and a flush, four fingers makes it so that only 4 have to be same suit)
    - Flush Five (hand must be 5 of the same rank and suit, four fingers makes it so that only 4 have to be same suit)

    Args:
        hand (tuple): A tuple of PlayingCard objects.
    Returns:
        scored_cards (tuple): A tuple of cards that would be scored.
        
    """
    
    if not hand:
        return tuple()

    return hand



def high_card_scored_cards(hand: tuple[PlayingCard, ...]) -> tuple[PlayingCard, ...]:
    """
    Assuming that "High Card" is the highest tier for the hand, return what card will be scored.

    Args:
        hand (tuple): A tuple of PlayingCard objects.
    Returns:
        scored_cards (tuple): A tuple of cards that would be scored.
    """
    if not hand:
        return tuple()
    
    ranks_hierachy = tuple(ranks[1:] + ranks[:1])  # Move 'a' to the end of the list to make it the highest rank

    max_card_rank = 0
    max_rank_card = None

    for card in hand:
        card_rank = ranks_hierachy.index(card.rank)
        if card_rank >= max_card_rank:
            max_card_rank = card_rank
            max_rank_card = card

    return tuple([max_rank_card]) if max_rank_card else tuple()


def pair_scored_cards(hand: tuple[PlayingCard, ...]) -> tuple[PlayingCard, ...]:
    """
    Assuming that "Pair" is the highest tier for the hand, return what cards will be scored.
    
    Args:
        hand (tuple): A tuple of PlayingCard objects.
    Returns:
        scored_cards (tuple): A tuple of cards that would be scored.
    """
    if not hand:
        return tuple()

    rank_counts = {}
    for card in hand:
        rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

    pair_rank = None
    for rank, count in rank_counts.items():
        if count == 2:
            pair_rank = rank
            break

    if pair_rank is None:
        return tuple()

    return tuple(card for card in hand if card.rank == pair_rank)


def two_pair_scored_cards(hand: tuple[PlayingCard, ...]) -> tuple[PlayingCard, ...]:
    """
    Assuming that "Two Pair" is the highest tier for the hand, return what cards will be scored.
    
    Args:
        hand (tuple): A tuple of PlayingCard objects.
    Returns:
        scored_cards (tuple): A tuple of cards that would be scored.
    """
    if not hand:
        return tuple()

    rank_counts = {}
    for card in hand:
        rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

    pairs = [rank for rank, count in rank_counts.items() if count == 2]

    if len(pairs) < 2:
        return tuple()

    return tuple(card for card in hand if card.rank in pairs)


def three_oa_kind_scored_cards(hand: tuple[PlayingCard, ...]) -> tuple[PlayingCard, ...]:
    """
    Assuming that "Three of a Kind" is the highest tier for the hand, return what cards will be scored.
    
    Args:
        hand (tuple): A tuple of PlayingCard objects.
    Returns:
        scored_cards (tuple): A tuple of cards that would be scored.
    """
    if not hand:
        return tuple()

    rank_counts = {}
    for card in hand:
        rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

    three_of_a_kind_rank = None
    for rank, count in rank_counts.items():
        if count == 3:
            three_of_a_kind_rank = rank
            break

    if three_of_a_kind_rank is None:
        return tuple()

    return tuple(card for card in hand if card.rank == three_of_a_kind_rank)


def straight_scored_cards(hand: tuple[PlayingCard, ...], four_fingers = False, shortcut = False) -> tuple[PlayingCard, ...]:
    """
    Assuming that "Flush" is the highest tier for the hand, return what cards will be scored.
    Requires special calculation for four fingers joker
    
    Args:
        hand (tuple): A tuple of PlayingCard objects.
    Returns:
        scored_cards (tuple): A tuple of cards that would be scored.
    """
    if not hand:
        return tuple()
    
    if not four_fingers:
        return score_all_cards(hand)
    
    ### If the hand size is 4 with four-fingers active, it's always those 4 cards being played
    if len(hand) == 4:
        return hand
    
    ### If the hand size is 5 with four-fingers active, need to verify if 4 or 5 cards need to be played
    suits = [card.suit for card in hand]


def flush_scored_cards(hand: tuple[PlayingCard, ...], four_fingers = False) -> tuple[PlayingCard, ...]:
    """
    Assuming that "Flush" is the highest tier for the hand, return what cards will be scored.
    Requires special calculation for four fingers joker
    
    Args:
        hand (tuple): A tuple of PlayingCard objects.
    Returns:
        scored_cards (tuple): A tuple of cards that would be scored.
    """
    if not hand:
        return tuple()
    
    if not four_fingers:
        return score_all_cards(hand)
    
    ### If the hand size is 4 with four-fingers active, it's always those 4 cards being played
    if len(hand) == 4:
        return hand
    
    ### If the hand size is 5 with four-fingers active, need to verify if 4 or 5 cards need to be played
    suits = [card.suit for card in hand]
    

    ### One suit means all cards should be scored
    if len(set(suits)) == 1:
        return hand
    
    ### More than one suit, means it's a match of 4
    else:
        return tuple(card for card in hand if suits.count(card.suit) == 4)



def four_oa_kind_scored_cards(hand: tuple[PlayingCard, ...]) -> tuple[PlayingCard, ...]:
    """
    Assuming that "Four of a Kind" is the highest tier for the hand, return what cards will be scored.

    Args:
        hand (tuple): A tuple of PlayingCard objects.
    Returns:
        scored_cards (tuple): A tuple of cards that would be scored.
    """
    if not hand:
        return tuple()

    card_ranks = [card.rank for card in hand]

    return tuple(card for card in hand if card_ranks.count(card.rank) == 4)


if __name__ == "__main__":
    test_hand = (
        PlayingCard(rank = '2', suit = 'hearts'),
        PlayingCard(rank = 'k', suit = 'spades'),
        PlayingCard(rank = 'q', suit = 'diamonds'),
        PlayingCard(rank = '10', suit = 'clubs'),
    )

    test_hand2 = (
        PlayingCard('2', 'hearts'),
        PlayingCard('4', 'spades'),
        PlayingCard('5', 'diamonds'),
        PlayingCard('4', 'clubs'),
    )

    test_hand3 = (
        PlayingCard('2', 'hearts'),
        PlayingCard('4', 'spades'),
        PlayingCard('5', 'diamonds'),
        PlayingCard('4', 'clubs'),
        PlayingCard('5', 'hearts'),
    )

    test_hand4 = (PlayingCard('2', 'hearts'), PlayingCard('2', 'spades'), PlayingCard('2', 'diamonds'), PlayingCard('4', 'clubs'))

    test_hand5 = (PlayingCard('2', 'hearts'), PlayingCard('2', 'spades'), PlayingCard('2', 'diamonds'), PlayingCard('2', 'clubs'),PlayingCard('3', 'clubs'))


    scored_cards = high_card_scored_cards(test_hand)

    scored_cards2 = pair_scored_cards(test_hand2)

    scored_cards3 = two_pair_scored_cards(test_hand3)

    scored_cards4 = three_oa_kind_scored_cards(test_hand4)

    scored_cards5 = four_oa_kind_scored_cards(test_hand5)
    
    print(f"The following card/s will be scored: {scored_cards5}")  # Output: The following card/s will be scored: ('k', 'spades')