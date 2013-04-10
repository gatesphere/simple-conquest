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
#@+<< declarations >>
#@+node:peckj.20130410095550.1565: ** << declarations >>
#@-<< declarations >>
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

  def __str__(self):
    return "Army (%s infantry, %s archers, %s knights)" % (self.infantry, self.archers, self.knights)
  
  def __repr__(self):
    return self.__str__()
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
  global player_army
  # build army
  build_army()
  # determine terrain
  pass
#@+node:peckj.20130410095550.1566: *3* build_army
def build_army():
  global player_army
  print "Building Army:"
  points = 200
  inf = 0
  arc = 0
  kni = 0
  while points > 0:
    print ""
    print "Your army consists of:\n  %s infantry\n  %s archers\n  %s knights" % (inf, arc, kni)
    print "You have %s points left to spend." % points
    print "Infantry cost 1 point, Archers cost 2, and Knights cost 4."
    print "Input format: <n><t>, where n is a number, and t is a\ntype (i,a,k).  Example: 30i."
    purchase = raw_input("Your purchase order? ")
    t = purchase[-1]
    try:
      n = int(purchase[:-1])
      if n < 1:
        print "Number must be at least 1"
        continue
      if t == 'i':
        if n * 1 > points:
          print "Can't afford that many infantry!"
        else:
          inf += n
          points -= (n * 1)
      elif t == 'a':
        if n * 2 > points:
          print "Can't afford that many archers!"
        else:
          arc += n
          points -= (n * 2)        
      elif t == 'k':
        if n * 4 > points:
          print "Can't afford that many knights!"
        else:
          kni += n
          points -= (n * 4)
      else:
        print "Unknown unit type '%s'" % t
    except Exception as e:
      print "Invalid number entry."
  player_army = Army(inf, arc, kni)
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
