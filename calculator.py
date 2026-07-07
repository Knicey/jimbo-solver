

def determine_highest_hand_ranking(hand):
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
    
    match len(hand):
        case 0:
            ### If no cards are played, no score is given
            return 0
        case 1:
            ### If there is only one card in the hand, it can only score as "High Card"
            return "high_card"

        case 2:
            ### If the are only two cards played, it can either be a pair or still high card
            rank1 = int(hand[0][:2])
            rank2 = int(hand[1][:2])

            ### If the ranks match, it's a pair
            if rank1 == rank2:
                return "pair"

            ### Otherwise, it's still high card
            else:
                return "high_card"


        case 3:
            ### If there are three cards played, it can either be a three of a kind, a pair, or still high card
            rank1 = int(hand[0][:2])
            rank2 = int(hand[1][:2])
            rank3 = int(hand[2][:2])

            ### If all three ranks match, it's a three of a kind
            if rank1 == rank2 == rank3:
                return "three_of_a_kind"
            
            ### If two of the ranks match, it's a pair
            elif rank1 == rank2 or rank1 == rank3 or rank2 == rank3:
                return "pair"
            
            ### Otherwise, it's still high card
            else:
                return "high_card"
            
        case 4:
            ### If there are four cards played, it can either be a four of a kind, a three of a kind, a pair, or still high card
            pass
        case 5:
            pass
        
    
    
    return 0

if __name__ == "__main__":
    # Example usage
    hand = ["12H", '12D']
    print(f"The hand {hand} is a: {determine_highest_hand_ranking(hand)}")