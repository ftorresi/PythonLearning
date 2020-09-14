
import random

class Deck:
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K']
        suits = ['C', 'D', 'H', 'S']
        self.deck = [s+r for s in suits for r in ranks]
        random.shuffle(self.deck)

    def hand(self, n=1):
        """Deal n cards. Return hand as list."""
        hand = [self.deck[i] for i in range(n)]  # pick cards
        del self.deck[:n]                        # remove cards
        return hand

    def deal(self, cards_per_hand, no_of_players):
        """Deal no_of_players hands. Return list of lists."""
        return [self.hand(cards_per_hand) for i in range(no_of_players)]

    def putback(self, card):
        """Put back a card under the rest."""
        self.deck.append(card)

    def __str__(self):
        return str(self.deck)
    
    
def same_rank(hand, n_of_a_kind):
    """
    Given a hand of cards, return the number of
    n_of_a_kind combinations of ranks.
    For example, with n_of_a_kind=2, the function
    returns the number of pairs in the hand.
    """
    ranks = [card[1:] for card in hand]
    counter = 0
    already_counted = []
    for rank in ranks:
        if rank not in already_counted and \
               ranks.count(rank) == n_of_a_kind:
            counter += 1
            already_counted.append(rank)
    return counter

def same_suit(hand):
    """
    Given a hand of cards, return the number of
    cards of the same suit, counter[suit], for each
    of the suits in the hand.
    """
    suits = [card[0] for card in hand]
    counter = {}   # counter[suit] = how many cards of suit
    for suit in suits:
        # Attention only to count > 1:
        count = suits.count(suit)
        if count > 1:
            counter[suit] = count
    return counter

n=int(input("Number of players? "))
deck = Deck()
players = deck.deal(5,n)
import pprint
pprint.pprint(players)

print("IDK poker rules so I can't make this exercise")
