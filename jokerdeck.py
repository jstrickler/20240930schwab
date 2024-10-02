from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for i in range(1, 3):
            card = Card(f'Joker{i}', f'Joker{i}')
            self._cards.append(card)
    
    def evil_laugh(self):
        print("Mwah-ha-ha")

if __name__ == "__main__":
    j = JokerDeck()
    print(j)
    print(f"{j = }")
    j.shuffle()
    for _ in range(5):
        print(f"{j.draw() = }")
    print()
    print(j.cards)
    j.evil_laugh()