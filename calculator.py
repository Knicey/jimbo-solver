from cards import PlayingCard, fromStr


def numericRank(rank: str, aceHigh: bool = False) -> int:
    faceOrder = ("j", "q", "k")
    if rank == "a":
        return 14 if aceHigh else 1
    elif rank in faceOrder:
        return faceOrder.index(rank) + 11
    else:
        return int(rank)


def determine_highest_hand_ranking(hand: list[PlayingCard]) -> str:
    """
    Calculate what the highest ranked hand available is.

    Args:
        hand (list): A list of cards in the hand. Each card is represented as a string.
        Cards strings are in the format RRS where RR is the rank (01, 02, ..., 13) and S is the suit (H, D, C, S).
    Returns:
        str: The name of the highest ranked hand.
    """

    if not hand:
        return ""

    ranks = [numericRank(card.rank, False) for card in hand]
    for _ in range(ranks.count(1)):
        ranks.append(numericRank("a", True))
    suits = [card.suit for card in hand]

    rank_counts = {rank: ranks.count(rank) for rank in set(ranks)}
    suit_counts = {suit: suits.count(suit) for suit in set(suits)}

    highest_rank_count = max(rank_counts.values())
    highest_suit_count = max(suit_counts.values())

    num_pairs = [v for k, v in rank_counts.items() if k != 14].count(2)

    isStraight = max(ranks) - min(ranks) == len(ranks) - \
        1 and len(set(ranks)) == len(ranks)

    nOfRank = ("", "high_card", "pair", "three_of_a_kind",
               "four_of_a_kind", "five_of_a_kind")[highest_rank_count]
    isFlush = highest_suit_count == 5

    if len(hand) <= 4:
        # since num_pairs is the number of distinct pairs, a 3- and 4-of-a-kinds require num_pairs=1
        # thus, if a two-pair is playable, 3- and 4-of-a-kind's are not playable, so it's the best hand
        return "two_pair" if num_pairs == 2 else nOfRank
    else:
        match highest_rank_count:
            case 5:
                return "flush_five" if isFlush else nOfRank
            case 3:
                # assert num_pairs != 2 #i think this is true
                if num_pairs == 1:
                    return "flush_house" if isFlush else "full_house"
                else:  # num_pairs == 0, so no two-pair
                    return nOfRank
            case 1:
                if isFlush:
                    return "straight_flush" if isStraight else "flush"
                else:
                    return "straight" if isStraight else nOfRank
            case 2:
                return "two_pair" if num_pairs == 2 else nOfRank
            case _:
                return nOfRank


if __name__ == "__main__":
    # Example usage
    all_hands = [
        ["12H", "13D", "12D", "12H"],
        ["12H", "12H", "12H", "12H", "12H"],
        ["12H", "12H", "12H", "13H", "13H"],
        ["12H", "12H", "13H", "13H", "14H"],
        ["09H", "10H", "11H", "12H", "13H"],
        ["09H", "10H", "11H", "12H", "13C"],
        ["09H", "09H", "09C", "12D", "12D"],
        ["14H", "14D", "13D", "11H"],  # returns `pair`
        ["14H", "14D", "11D", "11H"],  # returns `two_pair`
    ]

    for hand in all_hands:
        parsed = [fromStr(i) for i in hand]
        print(
            f"The highest ranking hand within {hand} is a: {determine_highest_hand_ranking(parsed)}")
