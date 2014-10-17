#!/usr/bin/python


#pos1 is the position that guarded the player in the first quarter
#pos2 is the position that guarded the player in the second quarter


class Activity:
   sport = 'Basketball'

   def __init__(self, pos1, pos2):
      self.pos1 = pos1
      self.pos2 = pos2
	  

Kobe_Bryant = Activity('Guard', 'Forward')
Steve_Nash = Acitivty('Guard', 'Guard')

print "In first quarter The 2 Guard Was Defended by a" Kobe_Bryant.pos1
print "In second quarter The 1 Guard Was Defended by a" Steve_Nash.pos2	  
