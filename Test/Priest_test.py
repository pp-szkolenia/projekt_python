from characters.professions import Priest

priest = Priest("HealMan", "Human")

print(f"Hp start -> {priest.hp}")
priest.take_damage(2)
print(f"After damage -> {priest.hp}")
priest.heal(2)
print(f"After heal -> {priest.hp}")

print(f"Expected contribution -> {priest.expected_contribution("holly")}")
print(f"Contribute -> {priest.contribute("holly")}")