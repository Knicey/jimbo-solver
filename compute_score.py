import json

def compute_high_card_score(hand):
    """
    Assuming that "High Card" is the highest tier for the hand, compute the score.

    Args:
        hand (list): A list containing a single card in the format "RankSuit".

    Returns:
        int: The score for the High Card hand.
    """

    ranks = [int(card[:2]) for card in hand]

    with open('hand_scores.json', 'r', encoding='utf-8') as file:
        hand_scores = json.load(file)

    chips = hand_scores["high_card"]['chips']
    mult = hand_scores["high_card"]['mult']

    score = (chips + max(ranks)) * mult

    return score


if __name__ == "__main__":
    hand = ["12H"]
    print(f"The score of the hand {hand} is: {score_simple_hand(hand)}")