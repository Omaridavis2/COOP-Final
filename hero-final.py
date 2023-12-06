hero.py

class Superhero:
    def __init__(self, name, power_level=100):
        # Public attribute: name
        self.name = name
        # Protected attribute: power_level
        self._power_level = power_level
        # Public attribute: flight_power
        self.flight_power = True

    def fly(self):
        # Public method modifying a class attribute
        print(f"{self.name} is soaring through the sky!")

    def use_power(self):
        # Public method using a class attribute
        print(f"{self.name} uses their superpower!")


class Spartan(Superhero):
    def __init__(self, name, weapon="Sword", power_level=120):
        # Inheriting from the Superhero class
        super().__init__(name, power_level)
        # Composition: Spartan has a Weapon
        self.weapon = weapon

    def use_power(self):
        # Overriding the use_power method of the superclass
        # Protected method of the superclass called within the subclass
        super().use_power()
        print(f"{self.name} uses their flight power to maneuver quickly.")

    def attack(self):
        # Public method using class attributes
        print(f"{self.name} attacks using {self.weapon}!")


# Instantiate a Spartan object
spartan_hero = Spartan("Spartan")
