from utils import dice_roll

from races import Elf


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

        self._apply_race()

    def to_json(self):
        jsonified_object = self.__dict__
        jsonified_object["race"] = str(jsonified_object.get("race"))
        return jsonified_object

    def _apply_race(self):
        stats = {
            "strength": self.strength,
            "intelligence": self.intelligence,
            "faith": self.faith,
        }
        stats_modified = self.race.modify_statistics(stats)
        self.strength = stats_modified["strength"]
        self.intelligence = stats_modified["intelligence"]
        self.faith = stats_modified["faith"]

    @property
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} – {self.race} {self.__class__.__name__}"

    def take_damage(self, amount):
        self.hp = max([0, self.hp - max(0, amount)])

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)


class Warrior(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength += 2
        self.intelligence -= 1

    def contribute(self, task_type):
        if task_type == "combat":
            return self.strength + dice_roll(4)
        else:
            return 2 + dice_roll(4)

    def expected_contribution(self, task_type):
        if task_type == "combat":
            return self.strength + expected_dice_roll
        else:
            return 2 + expected_dice_roll


class Wizard(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength -= 1
        self.intelligence += 2
        self.faith += 1

        self.mana = 5

    def contribute(self, task_type):
        if task_type == "magic":
            contribution = self.mana // 2 + self.intelligence + dice_roll(4)
            self.__spend_mana()
            return contribution
        else:
            return 2 + dice_roll(4)

    def expected_contribution(self, task_type):
        if task_type == "magic":
            return self.mana // 2 + self.intelligence + expected_dice_roll
        else:
            return 2 + expected_dice_roll

    def __spend_mana(self):
        self.mana = max(0, self.mana - 1)


class Priest(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength -= 2
        self.intelligence += 1
        self.faith += 3

        self.mana = 5.0

    def contribute(self, task_type):
        if task_type in ("holy", "support"):
            return self.faith + dice_roll(4)
        return 1 + dice_roll(4)

    def expected_contribution(self, task_type):
        if task_type in ("holy", "support"):
            return self.faith + expected_dice_roll
        return 1 + expected_dice_roll

    def heal_ally(self, ally):
        if self.mana > 0:
            heal_amount = self.faith / 5
            ally.heal(heal_amount)
            self.mana = max(0, self.mana - heal_amount / 10)


# 2 8 5
elf_wizard = Wizard("Legolas", Elf())
print(elf_wizard.to_json())
