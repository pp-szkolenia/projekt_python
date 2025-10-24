class Race:
    def __init__(self, name, strength_mod, intelligence_mod, faith_mod):
        self.name = name
        self.strength_mod = strength_mod
        self.intelligence_mod = intelligence_mod
        self.faith_mode = faith_mod

    def modify_statistics(self, stats):
        assert isinstance(stats, dict), "Stats data must be a dict"

        stats["strength"] = stats.get("strength", 0) + self.strength_mod
        stats["intelligence"] = stats.get("intelligence", 0) + self.intelligence_mod
        stats["faith"] = stats.get("faith", 0) + self.faith_mode
        return stats


class Human(Race):
    def __init__(self):
        super().__init__("Human", strength_mod=1, intelligence_mod=1, faith_mod=1)

    def __repr__(self):
        return "Human"


class Elf(Race):
    def __init__(self):
        super().__init__("Elf", strength_mod=-1, intelligence_mod=2, faith_mod=0)

    def __repr__(self):
        return "Elf"


class Orc(Race):
    def __init__(self):
        super().__init__("Orc", strength_mod=2, intelligence_mod=-1, faith_mod=-1)

    def __repr__(self):
        return "Orc"
