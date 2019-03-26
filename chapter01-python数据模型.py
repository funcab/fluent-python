# 一摞有序的纸牌

import collections

# namedtuple用来构建只有少数属性但是没有方法的对象，比如数据库条目
# 与tuple不同的是，namedtuple不仅可以通过index来访问item，还可通过name来访问
# 如下，我们可以轻松得到一个纸牌对象

Card = collections.namedtuple('card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # 前后双下划綫：dunder
    def __init__(self):
        self._cards = [(Card(rank, suit) for suit in self.suits
                        for rank in self.ranks)]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)
