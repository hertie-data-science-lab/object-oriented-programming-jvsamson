# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 19:18:26 2023

@author: Justus v. Samson-Himmelstjerna
"""

# import the classes from Creature.py and the Ecosystem class from River.py
from Creatures import Fish, Bear
from River import Ecosystem

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
