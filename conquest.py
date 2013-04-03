#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:peckj.20130403092722.1556: * @file conquest.py
#@@first
#@@language python
#@+<< imports >>
#@+node:peckj.20130403092722.1557: ** << imports >>
import math
import random
#@-<< imports >>
#@+others
#@+node:peckj.20130403092722.1558: ** army class
class Army:
  def __init__(self, infantry, archers, knights):
    self.infantry = infantry
    self.archers = archers
    self.knights = knights
  
  #@+others
  #@+node:peckj.20130403092722.1559: *3* fighting values
  def infantry_fighting_value(self):
    return math.floor(self.infantry * 0.5)

  def archer_fighting_value(self):
    return math.floor(self.archers * 2)

  def knight_fighting_value(self):
    return math.floor(self.knights * 4)
  #@+node:peckj.20130403092722.1560: *3* deltas
  # infantry
  def _delta_infantry(self, delta):
    self.infantry += delta

  def lose_infantry(self, value):
    self._delta_infantry(-value)

  def gain_infantry(self, value):
    self._delta_infantry(value)

  # archers
  def _delta_archers(self, delta):
    self.archers += delta

  def lose_archers(self, value):
    self._delta_archers(-value)

  def gain_archers(self, value):
    self._delta_archers(value)

  # knights
  def _delta_knights(self, delta):
    self.knights += delta

  def lose_knights(self, value):
    self._delta_knights(-value)

  def gain_knights(self, value):
    self._delta_knights(value)
  #@-others
#@+node:peckj.20130403092722.1561: ** army definitions
def make_small_army():
  return Army(10, 5, 3)

def make_medium_army():
  return Army(25, 20, 5)

def make_large_army():
  return Army(40, 12, 8)

def make_bandits():
  return Army(random.randint(1,6)*2, random.randint(1,6)*2, 0)
#@+node:peckj.20130403092722.1564: ** set_up_game
def set_up_game():
  # build army
  # determine terrain
  pass
#@+node:peckj.20130403092722.1562: ** gameloop
def gameloop():
  # Move
  # Terrain bonus
  # Roll Enemy Army
  # Fight Enemy Army
  # Check for win/lose
  # Roll for Adjacent Terrain
  pass
#@+node:peckj.20130403092722.1563: ** __main__
if __name__ == "__main__":
  # set up game
  set_up_game()
  # gameloop
  gameloop()
  # exit
#@-others
#@-leo
