from professions import Character


warrior = Character("Boromir", "Elf")
print(repr(warrior))
print(warrior)

print(warrior.hp)
warrior.take_damage(12)
print(warrior.hp)

print("czy żywy:", warrior.is_alive)
warrior.heal(4)
print(warrior.hp)
print("po uzdrowieniu:", warrior.is_alive)

print(warrior.to_json())
