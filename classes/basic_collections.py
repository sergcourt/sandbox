import collections

Cards= collections.namedtuple('Card', ['rank', 'suit'])




random_c= Cards ('Q', 'spades')
<<<<<<< Updated upstream
#print(random_c)

class Mazzo_di_mazzi :
    rank=[str(n) for n in range(2,11)] + list ('JOKA')
    suit='spades diamonds clubs hearts'.split()
=======
print(random_c)

class Mazzo_di_mazzi :
    rank=[str(n) for n in range(2,11)] + list ('JOKA')
    suit='pades diamonds clubs hearts'.split()
>>>>>>> Stashed changes

    def __init__(self):
        self._cards=[Cards(rank, suit) for rank in self.rank  for suit in self.suit]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]




<<<<<<< Updated upstream
m=Mazzo_di_mazzi()
print(len(m))
print(m[1])
=======
>>>>>>> Stashed changes
