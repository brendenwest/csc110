**Reading**

- Zelle, Chapter 4 - Graphics Programming
- [http://mcsp.wartburg.edu/zelle/python/ppics2/slides/Chapter04.ppt](http://mcsp.wartburg.edu/zelle/python/ppics2/slides/Chapter04.ppt)

 

**Summary**

- Python graphics setup
- Graphics window
- Graphic objects
- Object methods

 

**Python setup** 

The tkinter library ([https://docs.python.org/2/library/tkinter.html (Links to an external site.)](https://docs.python.org/2/library/tkinter.html)) enables Python to interact with a computer's graphical user interface (GUI). Some versions of Python include tkinter, but you may need to install it on your computer.

This class uses a custom Python library - [http://mcsp.wartburg.edu/zelle/python/ppics2/code/graphics.py (Links to an external site.)](http://mcsp.wartburg.edu/zelle/python/ppics2/code/graphics.py) - which depends on tkinter and simplifies some of its drawing commands. You'll need to download **graphics.py** to a folder your python programs can access.

 

**Graphics Window**

A GUI is made up of basic elements (objects) that have properties and can interact with each other. These objects are drawn on the computer display for user interaction.

 

- Drawing takes place within a graphics 'window':

from graphics import *  
win = graphics.GraphWin()  

- Graphics windows have a defined size (in pixels). Default is 200 x 200
    - All points in the window have horizonal (x) and vertical (y) coordinatesic
    - Coordinate system begins with the upper left corner (0,0)
    - X values increase from left to right, Y values increase from top to bottom
    - You can set custom title and window size like so:

win = GraphWin("Window Title",600,600)

- Graphics windows can be manipulated and closed

tkinter provides classes for a basic set of graphic objects, that serve as building blocks for a more complex GUI. Each class has a constructor methods to create instances of that class. 

Once defined, a graphic object is drawn to the graphics window with the draw() method.

 

**Point**

Points are the simplest graphical objects and are defined by their x & y coordinates:

p = Point(50, 60)  
p.draw(win) 

Points are used as input parameters for other shape constructors.  
  

**Line**

l = Line(&lt;point1&gt;, &lt;point2&gt;)  
l = Line(Point(10,10), Point(50,50))

**Circle**

c = Circle(&lt;center_point&gt;, &lt;radius&gt;)  
c = Circle(p, 30)

**Oval**

o = Oval(&lt;point1&gt;, &lt;point2&gt;)  
o = Oval(Point(10,10), Point(50,50))

**Rectangle**

r = Rectangle(&lt;point_upper_left&gt;, &lt;point_lower_right&gt;)  
r =  Rectangle(Point(10,10), Point(100,100))

**Polygon** - takes any number of points and connects them into a closed shape:

t = Polygon(&lt;point1&gt;,&lt;point2&gt;,&lt;point3&gt;)

**Entry** - creates a text-entry object:

e = Entry(&lt;point&gt;,&lt;num_chars&gt;)

**Text**

label = Text(&lt;center_point&gt;, “text”)

 

**Graphic Object methods**

Each class has accessor (getter) methods to access instance variables (properties). For example:

p.getX()  
p.getY()

Each class also has mutator methods to change the object’s state. For example:

p.move(dx, dy) # erase & redraw (move) p a distance of dx & dy  
c.setFill(‘yellow’) # fills shape with a color  
c.setOutline(‘red’)  
label.setText(“new text”)

As with other Python objects, a copy of an object refers to the same instance:

c2 = c # both circles share the same attributes  

But objects can be cloned to a new instance:

c2 = c.clone()  
c2.move(30,0) # c2 has different attributes that c

The graphics window can capture user interaction, such as a mouse click, as an event object.

p = win.getMouse()  
print("You clicked", p.getX(), p.getY())