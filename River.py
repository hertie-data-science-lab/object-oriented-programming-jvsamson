"""
Created on Sun Feb 14 17:56:53 2023

@author: Justus v. Samson-Himmelstjerna
"""
import random
from Creatures import Fish, Bear

# define the Ecosystem class, which contains the river and the simulation logic
class Ecosystem:
    def __init__(self, river_length):
        # create the river as a list of None objects of the given length
        self.river = [None] * river_length
        # populate the river with fish and bears, according to the initial ratio
        num_fish = river_length // 3
        num_bears = num_fish // 2
        for i in range(num_fish):
            # find a random empty location in the river and place a fish there
            empty_idx = random.choice([j for j in range(river_length) if self.river[j] is None])
            self.river[empty_idx] = Fish()
        for i in range(num_bears):
            # find a random empty location in the river and place a bear there
            empty_idx = random.choice([j for j in range(river_length) if self.river[j] is None])
            self.river[empty_idx] = Bear()
    # Create a new list to hold the updated positions of the creatures.
    def move_creatures(self):
        new_positions = [None] * len(self.river)

        # Loop through each position in the river.
        for i in range(len(self.river)):
            # If the creature in this position is a fish or a bear, update its position accordingly.
            if isinstance(self.river[i], Fish) or isinstance(self.river[i], Bear):
                self.river[i].move()

        # Return the updated list of creature positions.
        return self.river