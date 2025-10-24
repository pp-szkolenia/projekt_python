from utils import dice_roll


expected_dice_roll = 3.5


class Character:
    max_hp = 10.0

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.hp = 8.0
        self.strength = 4
        self.intelligence = 4
        self.faith = 4

    def to_json(self):
        return self.__dict__

    @property
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} - {self.race} {self.__class__.__name__}"

    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)

    def heal(self, amount):
        self.hp = min(amount + self.hp, self.max_hp)


class Warrior(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength += 2
        self.intelligence -= 1

    def expected_contribution(self, task_type):
        if task_type == 'combat':
            return self.strength + expected_dice_roll
        else:
            return 2 + expected_dice_roll

    def contribute(self, task_type):
        if task_type == 'combat':
            return self.strength + dice_roll()
        else:
            return 2 + dice_roll()


class Wizard(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength -= 1
        self.intelligence += 2
        self.faith += 1

        self.mana = 5.0

    def expected_contribution(self, task_type):
        if task_type == 'magic':
            return self.mana // 2 + self.intelligence + expected_dice_roll
        else:
            return 2 + expected_dice_roll

    def contribute(self, task_type):
        if task_type == 'magic':
            return self.mana // 2 + self.intelligence + dice_roll()
        else:
            return 2 + dice_roll()

    def __spend_mana(self):
        self.mana = max(self.mana - 1, 0)


class Priest(Character):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.strength -= 2
        self.intelligence += 1
        self.faith += 3
        self.mana = 5.0

    def expected_contribution(self, task_type):
        if task_type in ("holly", "support"):
            return self.faith + expected_dice_roll
        else:
            return 1 + expected_dice_roll

    def contribute(self, task_type):
        if task_type in ("holy", "support"):
            return self.faith + dice_roll()
        else:
            return 1 + dice_roll()

    def heal_ally(self, ally):
        if self.mana > 0:
            heal_amount = self.faith / 5
            ally.hp += heal_amount
            self.mana = max(0, self.mana - heal_amount / 10)