# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:45:36 2023

@author: Justus v. Samson-Himmelstjerna
"""

import random
from abc import ABCMeta, abstractmethod

class Creature(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass 

    def choose_new_position(self, i, new_positions):
        if i == 0:  # for the first position in the river, fish/bear can only move right or stay in the same position
            new_positions[i] = random.choice([i, i + 1])
        elif i == len(self.river) - 1:  # for the last position in the river, fish/bear can only move left or stay in the same position
            new_positions[i] = random.choice([i - 1, i])
        else:  # for all other positions in the river, fish/bear can move left, right or stay in the same position
            new_positions[i] = random.choice([i - 1, i, i + 1])

        return new_positions

    def move_creature(self, i, new_positions):
        # If the new position is empty, move the fish/bear to that position.
        if self.river[new_positions[i]] is None:
            self.river[new_positions[i]] = self.river[i]
            self.river[i] = None

    def create_new_creature(self, creature_type, ecosystem):
        # Create a new creature and add it to a random empty position in the river.
        new_creature = creature_type()
        # check if their is space available for a new creature, if so create a creature for random location
        for i in range(len(ecosystem.river)):
            if ecosystem.river[i] is None:
                empty_idx = random.choice([j for j in range(len(self.river)) if self.river[j] is None])
                self.river[empty_idx] = new_creature
            else:
                pass # skip creating a new creature if no space is available    

# define a class representing a fish
class Fish(Creature):
    def move(self):
        new_positions = self.choose_new_position()
        self.move_creature()
        # If the new position is occupied by another fish, keep both fish at its original position.
        if isinstance(self.river[new_positions[i]], Fish):
            self.river[i] = None
            self.create_new_creature(Fish)

# define a class representing a bear
class Bear(Creature):
    def move(self, i):
        new_positions = self.choose_new_position()
        self.move_creature()
        # If the new position is occupied by another bear, create a new bear and add it to a random empty position in the river.
        if isinstance(self.river[new_positions[i]], Bear):
            self.create_new_creature(Bear)

        # If the new position is occupied by a fish, remove the fish from its position.
        if isinstance(self.river[new_positions[i]], Fish):
            self.river[i] = None