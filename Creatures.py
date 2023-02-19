# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:45:36 2023

@author: Justus v. Samson-Himmelstjerna
"""

from abc import ABCMeta, abstractmethod

class Creature(metaclass=ABCMeta):
   pass 
  

# define a class representing a fish
class Fish(Creature):
    pass


# define a class representing a bear
class Bear(Creature):
    pass
