class Card:  #  inherits from object
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):   #  getter property
        return self._rank
    
    @rank.setter
    def rank(self, value):
        # validate the value and raise error if invalid
        self._rank = value

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        self._suit = value

    # responds to repr(obj)
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    # responds to str(obj)
    def __str__(self):
        return f"{self.rank}-{self.suit}"

if __name__ == "__main__":
    c1 = Card("5", "Diamonds")
    print(f"{c1 = }")  # uses repr()  via __repr__()
    print(c1)          # uses str() via __str__()
    print(f"{c1.rank = }")    #  NOT c1.rank()
    print(f"{c1.suit = }")
    c1.rank = "8"  # c1.rank("8") (setter)
