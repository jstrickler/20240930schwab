import random

class Knight(object):
    def __init__(self, requested_name: str):
        with open('../DATA/knights.txt') as knights_in:
            raw_line: str
            for raw_line in knights_in:
                line: str = raw_line.rstrip('\n\r')
                name: str
                title: str
                (name, title, color, quest, comment) = line.split(":")
                if name.lower() == requested_name.lower():
                    self._name = name
                    self._title = title
                    self._favorite_color = color
                    self._quest = quest
                    self._comment = comment
                    break

    @property
    def name(self) -> str:
        return self._name

    @property
    def title(self) -> str:
        return self._title

    @property
    def favorite_color(self) -> str:
        return self._favorite_color

    @property
    def quest(self) -> str:
        return self._quest

    @property
    def comment(self) -> str:
        return self._comment
    
    def joust(self, opponent: "Knight") -> "Knight":
        """
        Simulate a jousting match between this knight and an opponent

        :param opponent: The opposing knight
        :type opponent: Knight
        :return: The winner
        :rtype: Knight
        """
        self_score = random.randint(1, 10)
        opponent_score = random.randint(1, 10)
        if self_score >= opponent_score:
            return self
        else:
            return opponent


if __name__ == "__main__":
    k1 = Knight("Arthur")
    print(k1.name, k1.favorite_color, k1.comment, k1.title)

    k2 = Knight('Bedevere')
    print(k2.name)
    print()

    winner = k1.joust(k2)
    print(f"{winner.name} wins the jousting tournament!")
