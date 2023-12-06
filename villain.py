villain.py

class Villain:
    def __init__(self, name, evil_level=80):
        # Public attribute: name
        self.name = name
        # Protected attribute: evil_level
        self._evil_level = evil_level
        # Public attribute: flight_power
        self.flight_power = True

    def fly(self):
        # Public method modifying a class attribute
        print(f"{self.name} is flying menacingly!")

    def use_power(self):
        # Public method using a class attribute
        print(f"{self.name} uses their villainous power!")


class ZMan(Villain):
    def __init__(self, name, weapon="Dark Energy", evil_level=100):
        # Inheriting from the Villain class
        super().__init__(name, evil_level)
        # Composition: ZMan has a Weapon
        self.weapon = weapon

    def use_power(self):
        # Overriding the use_power method of the superclass
        # Protected method of the superclass called within the subclass
        super().use_power()
        print(f"{self.name} uses their flight power to outmaneuver the hero.")

    def attack(self):
        # Public method using class attributes
        print(f"{self.name} attacks using {self.weapon}!")


# Instantiate a ZMan object
z_man_villain = ZMan("Z-Man")
