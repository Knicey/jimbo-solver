from cards import PlayingCard, fromStr


def numericRank(rank: str, aceHigh: bool = False) -> int:
    faceOrder = ("j", "q", "k")
    if rank == "a": return 14 if aceHigh else 1
    elif rank in faceOrder: return faceOrder.index(rank) + 11
    else: return int(rank)

def determine_highest_hand_ranking(hand: list[PlayingCard]):
    """
    Calculate what the highest ranked hand available is.

    Args:
        hand (list): A list of cards in the hand. Each card is represented as a string.
        Cards strings are in the format RRS where RR is the rank (01, 02, ..., 13) and S is the suit (H, D, C, S).
    Returns:
        str: The name of the highest ranked hand.
    """

    if not hand:
        return 0

    ranks = [numericRank(card.rank, False) for card in hand]
    for _ in range(ranks.count(1)): ranks.append(numericRank("a", True))
    suits = [card.suit for card in hand]

    rank_counts = {rank: ranks.count(rank) for rank in set(ranks)}
    suit_counts = {suit: suits.count(suit) for suit in set(suits)}

    highest_rank_count = max(rank_counts.values())
    highest_suit_count = max(suit_counts.values())

    num_pairs = list(rank_counts.values()).count(2)

    isStraight = max(ranks) - min(ranks) == len(ranks) - 1 and len(set(ranks)) == len(ranks)
    #TODO: verify detection of ace-low straights (A2345) and ace-high straights (10JQKA)

    match len(hand):
        case 0:
            ### If no cards are played, no score is given
            return 0
        case 1:
            ### If there is only one card in the hand, it can only score as "High Card"
            return "high_card"

        case 2:
            ### If the are only two cards played, it can either be a pair or still high card
            if highest_rank_count == 2:
                return "pair"
            
            else:
                return "high_card"


        case 3:
            ### If there are three cards played, it can either be a three of a kind or any of the previous options
            if highest_rank_count == 3:
                return "three_of_a_kind"
            
            elif highest_rank_count == 2:
                return "pair"
            
            else:
                return "high_card"
            
        case 4:
            ### If there are four cards played, it can either be a four of a kind, two pair or any of the previous options
            if highest_rank_count == 4:
                return "four_of_a_kind"
            
            ### If there are two ranks that have a count of 2, then it is a two pair
            elif num_pairs == 2:
                return "two_pair"
            
            elif highest_rank_count == 3:
                return "three_of_a_kind"
            
            elif highest_rank_count == 2:
                return "pair"
            
            else:
                return "high_card"
            
        case 5:
            ### If there are five cards played, it can be anything

            ### Balatro has 3 hands that are possible to achieve in traditional poker

            # Flush Five: All 5 cards have matching ranks and suits
            if highest_suit_count == 5 and highest_rank_count == 5:
                return "flush_five"
            
            # Flush House: All 5 cards have matching suits, but a full house for the ranks
            elif highest_suit_count == 5 and highest_rank_count == 3 and num_pairs == 1:
                return "flush_house"
            
            # Five of a Kind: All 5 cards have matching ranks
            elif highest_rank_count == 5:
                return "five_of_a_kind"
            
            ### These are the rest of the traditional possible poker hands

            elif highest_suit_count == 5 and isStraight:
                return "straight_flush"

            elif highest_suit_count == 5:
                return "flush"
            
            elif isStraight:
                return "straight"
            
            elif highest_rank_count == 3 and num_pairs == 1:
                return "full_house"
            
            
            elif highest_rank_count == 4:
                return "four_of_a_kind"
            
            elif highest_rank_count == 3:
                return "three_of_a_kind"
            
            elif num_pairs == 2:
                return "two_pair"
            
            elif highest_rank_count == 2:
                return "pair"
            
            else:
                return "high_card"
    
    return 0

if __name__ == "__main__":
    # Example usage
    #hand1 = ["12H", '13D', '12D', '12H']
    hand1 = [fromStr("jh"), 
             fromStr("qd"), 
             fromStr("jd"), 
             fromStr("jh")]
    #hand2 = ['12H', '12H', '12H', '12H', '12H']
    hand2 = [fromStr("jh"), 
             fromStr("jh"), 
             fromStr("jh"), 
             fromStr("jh"), 
             fromStr("jh")]
    #hand3 = ['12H', '12H', '12H', '13H', '13H']
    hand3 = [fromStr("jh"), 
             fromStr("jh"), 
             fromStr("jh"), 
             fromStr("qh"),
             fromStr("qh")]
    #hand4 = ['12H', '12H', '13H', '13H', '14H']
    hand4 = [fromStr("jh"), 
             fromStr("jh"), 
             fromStr("qh"), 
             fromStr("qh"),
             fromStr("kh")]
    #hand5 = ['09H', '10H', '11H', '12H', '13H']
    hand5 = [fromStr("9h"), 
             fromStr("10h"), 
             fromStr("jh"), 
             fromStr("qh"),
             fromStr("kh")]
    #hand6 = ['09H', '10H', '11H', '12H', '13C']
    hand6 = [fromStr("9h"), 
             fromStr("10h"), 
             fromStr("jh"), 
             fromStr("qh"),
             fromStr("kc")]
    #hand7 = ['09H', '09H', '09C', '12D', '12D']
    hand7 = [fromStr("9h"), 
             fromStr("9h"), 
             fromStr("9c"), 
             fromStr("qd"),
             fromStr("qd")]

    all_hands = [hand1, hand2, hand3, hand4, hand5, hand6, hand7]

    for hand in all_hands:
        print(f"The highest ranking hand within {hand} is a: {determine_highest_hand_ranking(hand)}")
