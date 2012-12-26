"""
Hot Cold (hot-cold.py)
======================

Problem
-------
Build a two player hide and seek game!

Player 1 enters two numbers:

x his hiding x coordinate 0 - an integer  number between -100 and 100

y his hiding y coordinate 0 - an integer  number between -100 and 100

(The input x``=``0 and y``=``0 is not allowed)

The screen is cleared with the following command:

for i in range(100):
    print

Player 2 starts from 0, 0, and enters n,``s``,``w`` or e
to go north, south, west or east accordingly.

After entering the direction, the programs prints out one of the following options:

colder player 2 is getting far from player 1

warmer player 2 is getting closer to player 1

gotcha! player 2 found player 1 - and the game ends.

Sample Dialog
-------------
In this example player 1 hides here:

          |
          |
          |
          |
          |
          |
          |   @
----------+---------
          |
          |
          |
          |
          |

4
1
s
colder
n
warmer
n
warmer
n
colder
s
warmer
e
warmer
e
warmer
e
gotcha!

"""

x = int(raw_input("Enter your x-axis coordinate: "))
y = int(raw_input("Enter your y-axis coordinate: "))
for i in range(100):
    print
print "You are starting at the coordinates (0,0), please select n, s, e, w to get started: "
guessy = 0
guessx = 0
diffx = 0
diffx = 0
olddistance = abs(x)+abs(y)
# start = abs(x)+abs(y)
while True:
     
     z =  raw_input()
     
     if z == "n":
          guessy += 1
     if z == "s":
          guessy -= 1
     if z == "e":
          guessx += 1
     if z == "w":
          guessx -= 1
     
     if guessx == x and guessy == y:
          print "Gotcha! "
          break

     distance = abs(x-guessx)+abs(y-guessy)
     print "You are at %d, %d, and the distance is %d " % (guessx, guessy, distance)
     
     if distance < olddistance:
          print "Warmer! "
     else:
          print "Colder! "
     print "Try Again! "
     olddistance = distance
