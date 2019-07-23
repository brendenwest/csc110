
import random
from graphics import *
win = GraphWin("Jackpot",300,300)#Creates the graphics window


# rules
'''
- Display 3 cells in a row
- display button
- when user clicks button, randomly draw shapes in each cell (8 choices)
  - square
  - circle 
  - diamond
  - triangle
  - 4 text choices
- if all 3 cells show same choice, show 'winner' message
'''

r =  Rectangle(Point(10,10), Point(90,90))
r2 =  Rectangle(Point(100,10), Point(190,90))
r3 =  Rectangle(Point(200,10), Point(290,90))

slots = [r,r2,r3]
for slot in slots:
   slot.draw(win)

b = Rectangle(Point(100,100), Point(190,130))
b.draw(win)

message = Text(Point(140,115), "Spin!")
message.draw(win)

def square(slot):
   upper_left = Point(slot.p1.getX()+10,slot.p1.getY()+10)
   lower_right = Point(slot.p2.getX()-10,slot.p2.getY()-10)
   s = Rectangle(upper_left, lower_right)
   s.setFill("yellow")
   return s

def circle(slot):
   center = Point(slot.p1.getX() + (slot.p2.getX() - slot.p1.getX())/2,
                  slot.p1.getY() + (slot.p2.getY() - slot.p1.getY())/2
                 )
   c = Circle(center, 30)
   c.setFill("red")
   return c

def triangle(slot):
   # top
   p1 = Point(slot.p1.getX() + (slot.p2.getX() - slot.p1.getX())/2, slot.p1.getY()+10)
   # left
   p2 = Point(slot.p1.getX() + 10, slot.p2.getY()-10)
   # right
   p3 = Point(slot.p2.getX()-10,slot.p2.getY()-10)
   
   t = Polygon(p1,p2,p3)
   t.setFill("blue")
   return t

shapes = []
#Tracks mouse clicks
while True:
    p = win.getMouse()
    print("You clicked", p.getX(), p.getY())
    if p.getX() >= 100 and p.getX() <= 190 and p.getY() >= 100 and p.getY() <= 130:
       print('play on')

       # clear previously drawn shapes
       for i in range(len(shapes)):
          s = shapes.pop()
          s.undraw()

       for slot in slots:
          choice = random.randrange(3)
          if choice == 0:
             s = square(slot)
          elif choice == 1:
             s = circle(slot)
          elif choice == 2:
             s = triangle(slot)
          s.draw(win)
          shapes.append(s)
      
       if type(shapes[0]) == type(shapes[1]) == type(shapes[2]):
          print("winner!")
