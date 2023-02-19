"""
Created on Sun Feb 14 12:30:36 2023

@author: Justus v. Samson-Himmelstjerna
"""

import random

# define a class representing a fish
class Fish:
    pass

# define a class representing a bear
class Bear:
    pass

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

            # If the creature in this position is a fish, update its position accordingly.
            if isinstance(self.river[i], Fish):
                # Choose a new position for the fish by randomly selecting from the adjacent positions.
                if i == 0:  # for the first position in the river, fish can only move right or stay in the same position
                    new_positions[i] = random.choice([i, i + 1])
                elif i == len(self.river) - 1:  # for the last position in the river, fish can only move left or stay in the same position
                    new_positions[i] = random.choice([i - 1, i])
                else:  # for all other positions in the river, fish can move left, right or stay in the same position
                    new_positions[i] = random.choice([i - 1, i, i + 1])

                    # If the new position is empty, move the fish to that position.
                    if self.river[new_positions[i]] is None:
                        self.river[new_positions[i]] = self.river[i]
                        self.river[i] = None

                    # If the new position is occupied by another fish, keep both fish at its original position.
                    elif isinstance(self.river[new_positions[i]], Fish):
                        self.river[i] = None
                        # Create a new fish and add it to a random empty position in the river.
                        new_fish = Fish()
                        # check if their is space available for a new bear, if so create a bear for random location
                        for i in range(len(ecosystem.river)):
                            if ecosystem.river[i] is None:
                                empty_idx = random.choice([j for j in range(len(self.river)) if self.river[j] is None])
                                self.river[empty_idx] = new_fish
                            else:
                                pass # skip creating a new bear if no space is available    

                   # If the new position is occupied by a bear, the fish dies.
                    elif isinstance(self.river[new_positions[i]], Bear):
                        # Fish is eaten by the bear
                        self.river[i] = None

            # If the creature in this position is a bear, update its position accordingly.
            elif isinstance(self.river[i], Bear):
                # Choose a new position for the bear by randomly selecting from the adjacent positions.
                if i == 0:  # for the first position in the river, bear can only move right or stay in the same position
                    new_positions[i] = random.choice([i, i + 1])
                elif i == len(self.river) - 1:  # for the last position in the river, bear can only move left or stay in the same position
                    new_positions[i] = random.choice([i - 1, i])
                else:  # for all other positions in the river, bear can move left, right or stay in the same position
                    new_positions[i] = random.choice([i - 1, i, i + 1])

                    # If the new position is empty, move the bear to that position.
                    if self.river[new_positions[i]] is None:
                        self.river[new_positions[i]] = self.river[i]
                        self.river[i] = None

                    # If the new position is occupied by another bear, create a new bear and add it to a random empty position in the river.
                    elif isinstance(self.river[new_positions[i]], Bear):
                        new_bear = Bear()
                        # check if their is space available for a new bear, if so create a bear for random location
                        for i in range(len(ecosystem.river)):
                            if ecosystem.river[i] is None:
                                empty_idx = random.choice([j for j in range(len(self.river)) if self.river[j] is None])
                                self.river[empty_idx] = new_bear
                            else:
                                pass # skip creating a new bear if no space is available                       

                    # If the new position is occupied by a fish, remove the fish from its position.
                    elif isinstance(self.river[new_positions[i]], Fish):
                        self.river[i] = None

        # Return the updated list of creature positions.
        return self.river


# create an ecosystem with a river of length 20
ecosystem = Ecosystem(20)

# run the simulation for 10 time steps
for i in range(10):
    print("Time step:", i+1)
    # print the current state of the river
    for animal in ecosystem.river:
        if animal is None:
            print(".", end="")
        elif isinstance(animal, Fish):
            print("F", end="")
        elif isinstance(animal, Bear):
            print("B", end="")
    print()

    # move the creatures in the river and update their positions
    ecosystem.move_creatures()
    
    # print the final state of the river
print("Final state:")
for animal in ecosystem.river:
    if animal is None:
        print(".", end="")
    elif isinstance(animal, Fish):
        print("F", end="")
    elif isinstance(animal, Bear):
        print("B", end="")
print()
