import random
from card import Card

class CardDeck:
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self):
        self._cards = []
        self._make_deck()

    def _make_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if len(self) == 0:
            raise ValueError("No more cards")
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards
    
    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"CardDeck-{len(self)}"

    def __repr__(self):
        return "CardDeck()"

if __name__ == "__main__":
    cd1 = CardDeck()
    cd2 = CardDeck()
    print(f"{cd1 = }")
    cd1.shuffle()
    print(f"{cd1.cards = }")
    for _ in range(10):
        card = cd1.draw()
        print(f"{card = !s}")
    print(cd1)
    print(cd2)
