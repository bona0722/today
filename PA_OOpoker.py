suits = 'CDHS'
ranks = '23456789TJQKA'

from abc import ABCMeta, abstractmethod

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit
        
    def __repr__(self):
        return self.card
    
    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()


class PKCard(Card):

    def value(self):
        order = dict(zip(ranks, range(2, 2 + len(ranks))))
        for i in order.keys():
            if self.card[0] == i: return order[i]

if __name__ == '__main__':
    c1 = PKCard('QC')
    c2 = PKCard('9D')
    c3 = PKCard('9C')
    print(f'{c1} {c2} {c3}')

    # comparison
    print(c1 > c2 == c3)

    # sorting
    cards = [c1, c2, c3, PKCard('AS'), PKCard('2D')]
    sorted_cards = sorted(cards)
    print(sorted_cards)
    cards.sort()
    print(cards)



import random
class Deck():
    def __init__(self, cls):
        self.deck = [cls(r+s) for r in ranks for s in suits] 

    def shuffle(self):
        return random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()

    def __str__(self):
        return f'{self.deck}'

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, index):
        return self.deck[index]

if __name__ == '__main__':
    deck = Deck(PKCard)  # deck of poker cards
    deck.shuffle()
    c = deck[0]
    print('A deck of', c.__class__.__name__)
    print(deck)
    #testing __getitem__ method
    print(deck[-5:])

    while len(deck) >= 10:
        my_hand = []
        your_hand = []
        for i in range(5):
            for hand in (my_hand, your_hand):
                card = deck.pop()
                hand.append(card)
        my_hand.sort(reverse=True)
        your_hand.sort(reverse=True)
        print(my_hand, '>', your_hand, '?', my_hand > your_hand)


# 위의 예에서 my_hand와 your_hand는 단순히 rank value가 가장 큰 것이 이긴다는 'high card' 족보만으로 따졌을 때이다. Poker의 패는 [List of poker hands](https://en.wikipedia.org/wiki/List_of_poker_hands)에서 보듯이 다양한 족보가 있다.
# 
# ## Poker Hands
# 지난 Programming Assignement를 object-oriented로 설계 구현해 보자.
# 
# [List of poker hands](https://en.wikipedia.org/wiki/List_of_poker_hands)의 Hand rank category 표에 열거된 패의 rank 0..9 을 역순으로 9..0의 integer로 나열하면 hand ranking의 높고 낮음을 알수 있다. 이 수를 혼동하지 않도록 이라 하자.
# 
# Straight, flush, straight flush와 같이 rank가 다른 5장으로 패가 이뤄지는 경우, 
# hand ranking이 같으면
# 1. 5장끼리 rank value를 비교해서 판단해야 한다. 즉, reverse(decreading) order로 sorting하여 rank value를 비교하면 된다.
# 
# Hand ranking이 같다면, 예를 들어 둘 다 two pair로 동률 이루고 있다면
# 1. 높은 수 one pair의 rank value를 비교하고
# 2. 같으면, 낮은 one pair의 rank value를 비교하고
# 3. 같으면, 나머지 1장 끼리 value를 비교해서 승부를 가른다. 
# 
# 따라서, 패가 이뤄지는지 찾는 method들은 (hand_ranking, five_cards) tuple로 return한다면
# tuple 비교하는 Python rule에 따라 행하면 충분하게 된다.
# 이때, 이어지는 five_cards는 rank가 높은 순서로 sorting하거나, rank가 같은 것이 있다면(find_a_kind의 경우)
# tie-breaking이 먼저 일어날 카드들을 앞으로 배치해야 list간 비교로 간편히 비교 가능히다. (four cards, tripple cards, high pair)
# 
# Q. *PA. Find poker hands* 문제에서 function으로 구현한 것들을 OOP로 rewriting하라.
# 
# 중요: hand ranking 찾기, hand ranking이 같을 때 tie-break이 제대로 적용되는지를 검증하기 위한
# 가능한 모든 test case를 20개 이상을 작성함으로써, unit test가 *거의* 모든 경우를 포함하고 있음을
# 보여야 한다.


# class Hands:
#     def __init__(self, cards):
#         if len(cards) != 5:
#             raise ValueError('not 5 cards')
#         self.cards = sorted(cards, reverse=True)
#     ...
    
# if __name__ == '__main__':
#     import sys
#     def test(did_pass):
#         """  Print the result of a test.  """
#         linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
#         if did_pass:
#             msg = "Test at line {0} ok.".format(linenum)
#         else:
#             msg = ("Test at line {0} FAILED.".format(linenum))
#         print(msg)

#     # your test cases here
#     pass

