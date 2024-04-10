# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец делает выстрел из лука.")

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
    def fight(self):
        print(self.weapon.attack())

class Monster:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
    def fight(self):
        print(self.weapon.attack())
        print("Монстр побежден!")

bow1 = Bow()
sword1 = Sword()
monster = Monster(sword1)

fighter = Fighter(bow1)
fighter.fight()
monster.fight()

fighter.changeWeapon(bow1)
fighter.fight()
monster.fight()
