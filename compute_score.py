from cards import PlayingCard, ranks

def high_card_scored_cards(hand: tuple[PlayingCard]) -> tuple[PlayingCard]:
    """
    Assuming that "High Card" is the highest tier for the hand, return what card will be scored.

    Args:
        hand (list): A set of PlayingCard objects.
    Returns:
        scored_cards (list): A set of cards that would be scored.
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



if __name__ == "__main__":
    test_hand = (
        PlayingCard(rank = '2', suit = 'hearts'),
        PlayingCard(rank = 'k', suit = 'spades'),
        PlayingCard(rank = 'q', suit = 'diamonds'),
        PlayingCard(rank = '10', suit = 'clubs'),
    )
    scored_cards = high_card_scored_cards(test_hand)
    print(f"The following card/s will be scored: {scored_cards[0].rank} of {scored_cards[0].suit}")  # Output: The following card/s will be scored: ('k', 'spades')