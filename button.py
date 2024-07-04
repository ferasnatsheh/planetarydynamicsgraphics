#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 13:41:42 2022

@author: davisj
"""
from graphics import Point, Rectangle, Text, Image, GraphWin

class Button:

    def __init__(self, p1, p2, label=""):
        """Create a button.
        
        Parameters: 
                p1:   the top left point
                p2:   the bottom right point
                text: a string object, defaults to ""
        """
        
        #assert p1.getX() < p2.getX()
        #assert p1.getY() < p2.getY()
        
        self.rect = Rectangle(p1, p2)
        self.text = Text(self.rect.getCenter(), label)
        
        self.drawn = False
        self.win = None
        self.image = None
                 
    def draw(self, win):
        """Draw this button in the given GraphWin."""
        
        self.drawn = True
        self.win = win
        self.rect.draw(win)
        self.text.draw(win)
        if self.image:
            self.image.draw()
        
    def undraw(self):
        """Undraw this button."""
        
        self.rect.undraw()
        self.text.undraw()
        if self.image:
            self.image.undraw()
        self.drawn = False
            
    def setFill(self, color):
        """Set the button fill color."""
        
        self.rect.setFill(color)
        
    def setTextColor(self, color):
        """Set the button text color."""
        
        self.text.setTextColor(color)
        
    def setText(self, label):
        """Set the button text."""
        
        self.text.setText(label)
        
    def setImage(self, filename):
        """Set the button image to one loaded from the given filename."""
        
        
        if self.image and self.drawn:
            self.image.undraw()    
        self.image = Image(self.getCenter(), filename)
        if self.drawn:
            self.image.draw(self.win)    
            
    def getP1(self):
        """Get a point representing the upper left corner of the button."""
        
        return self.rect.getP1()
    
    def getP2(self):
        """Get a point representing the lower right corner of the button."""
        
        return self.rect.getP2()
    
    def getCenter(self):
        """Get a point representing the center of the button."""
        
        return self.rect.getCenter()
    
    def getText(self):
        """Get the text of the button."""
        
        return self.text.getText()
    
    def getImage(self):
        """Get a copy of the button image, or None if the button has no image."""
        
        if self.image:
            return self.image.clone()
        return None
        
    def contains(self, p):
        """Determine if the point p is contained within this button."""
        
        return p.getX() > self.rect.getP1().getX() and \
               p.getY() > self.rect.getP1().getY() and \
               p.getX() < self.rect.getP2().getX() and \
               p.getY() < self.rect.getP2().getY()

    def clicked(self, x, y):
        p1, p2 = self.rect.p1, self.rect.p2 
        x1, y1 = p1.getX(), p1.getY()
        x2, y2 = p2.getX(), p2.getY()
        return (x >= x1 and x <= x2) and (y >= y2 and y <= y1)

        
def main():
    win = GraphWin("Click Me!", 200, 200)
    button = Button(Point(50, 50), Point(150, 100), "Click Me!")
    button.draw(win)
    counter = 0
    
    while True:
        click = win.getMouse()
        if button.contains(click):
            counter = counter + 1
            button.setText(str(counter))
    
if __name__ == '__main__':
    main()