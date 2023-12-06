game.py

from hero import Spartan
from villain import ZMan

# Instantiate hero and villain objects
spartan_hero = Spartan("Spartan")
z_man_villain = ZMan("Z-Man")

# Test the game
spartan_hero.fly()
spartan_hero.use_power()
spartan_hero.attack()

z_man_villain.fly()
z_man_villain.use_power()
z_man_villain.attack()
