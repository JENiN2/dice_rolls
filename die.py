from random import randint


class Die:
    """Класс, обрабатывающий броски кубиков."""
    def __init__(self, num_sides=6, dices=3, rolls=10):
        """По умолчанию используется шестигранный кубик."""
        self.num_sides = num_sides
        self.dices = dices
        self.rolls = rolls
        self.results = []

    def roll(self):
        """Возвращает список с результатами бросков."""
        if self.dices == 1:
            for i in range(self.rolls):
                roll = (randint(1, self.num_sides))
                self.results.append(roll)
        if self.dices == 2:
            for i in range(self.rolls):
                roll1 = (randint(1, self.num_sides))
                roll2 = (randint(1, self.num_sides))
                roll = roll1 + roll2
                self.results.append(roll)
        if self.dices == 3:
            for i in range(self.rolls):
                roll1 = (randint(1, self.num_sides))
                roll2 = (randint(1, self.num_sides))
                roll3 = (randint(1, self.num_sides))
                roll = roll1 + roll2 + roll3
                self.results.append(roll)
        return self.results
