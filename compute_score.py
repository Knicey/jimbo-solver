from cards import PlayingCard, ranks

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
    Assuming that "Pair" is the highest tier for the hand, return what card will be scored.
    
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
    scored_cards = high_card_scored_cards(test_hand)

    scored_cards2 = pair_scored_cards(test_hand2)
    
    print(f"The following card/s will be scored: {scored_cards2}")  # Output: The following card/s will be scored: ('k', 'spades')