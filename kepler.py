# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:11:59 2022

Author(s): Troy Pelczarski and Feras Natsheh 

Acnkowledgements and Citations: 
    https://github.com/katiebreivik/Keplers_Laws/blob/master/Graphing%20Kepler's%20Laws%20with%20Python.ipynb
    We used this resource to fetch data on orbital periods and eccentrecities of solar planets
    We also consulted their model approach in generating our orbits. 
"""

from graphics import *
from time import sleep
from math import cos, sin, pow 
from button import *
import numpy as np
        
class Star:
    """Object which represents the star"""
    def __init__(self, center, radius):
        self.circle = Circle(center, radius)
        self.circle.setFill("Yellow")
        
    def draw(self, win):
        """Draws star"""
        self.circle.draw(win)

class Orbit:
    """Creates orbit"""
    def __init__(self, e, p):
        self.e  = e 
        self.p  = p 
        self.steps = 500
        self.theta = [] 
    
    def periodToSemiMajorAxis(self):
        """converts orbital period value into semi-major axis"""
        aCubed = self.p ** 0.5
        a = pow(aCubed, 0.3333333333)
        return a
    
    def generatePolarCoordinates(self):
        """generates theta, a list of angles along the orbit"""
        dt = np.linspace(0.0, self.p, self.steps) #return evenly spaced numbers over a specified interval
  
        for time in dt:
            psi = 1.0
            temp = 2 * np.pi * time / self.p
            psiOld = temp 
            
            while psi > 1e-10:
                psiNew = temp + self.e * np.sin(psiOld)
                psi = psiNew - psiOld
                psiOld = psiNew

            angle = 2 * np.arctan(((1+self.e)/(1-self.e)) ** (0.5) * np.tan(psiOld/2))
            self.theta.append(angle)  

        return self.theta
    
    def makeOrbit(self):
        """returns position in (x,y) form"""
        self.generatePolarCoordinates() 

        a = self.periodToSemiMajorAxis()
        coords = []

        for angle in self.theta: 
            r = (a * (1-(self.e ** 2))) / (1+ self.e * cos(angle))
            x = r * cos(angle)
            y = r * sin(angle)
            coords.append((x, y))
        return coords

class Planet:
    """Object which represents the planet"""
    def __init__(self, position: Point, orbit: Orbit, r: int):

        self.position = position
        self.planet = Circle(Point(0,0), 5)
        self.orbit = orbit 
        self.X = position.getX() 
        self.Y = position.getY()
        self.path = orbit.makeOrbit() 
        self.step = 0 
        self.r = r
        self.planet.setFill("white")
        
    def draw(self, win):
        """draws the planet"""
        self.planet.draw(win)

    def updatePosition(self):
        """updates position for each iteration in the positions list"""        
        
        self.step += 1 
        if self.step == 499:
            self.step = 0
        dX, dY = tuple(np.subtract(self.path[self.step + 1], self.path[self.step]))
        
        self.planet.move(dX *self.r, dY*self.r)
        
class orbitWin:
    """Creates the display and generates the objects within it."""
    def __init__(self, star: Star, planet: Planet, width = 900, length = 700):
        self.orbitWin = GraphWin("Orbit", width, length)
        self.orbitWin.setBackground("Black")
        self.orbitWin.setCoords(-600, -350, 300, 350)

        #declare bodies and their stats
        self.star = star
        self.planet = planet

        #draw Sun
        self.star.draw(self.orbitWin)
        self.planet.draw(self.orbitWin)

    def infoText(self):
        """Creates text for orbitWin"""
        instructions = Text(Point(250,300), "q: quit \np: pause")
        instructions.setSize(12)
        instructions.setTextColor("white")
        instructions.draw(self.orbitWin)

        infographic = Text(Point(0,-265), "The distance to the Sun and the speed of the planet are not to scale \n \nOur \
simulation depends on the eccentricity and the orbital period of the planet \n \nPlanets further than Jupiter are scaled down to fit within the screen")
        infographic.setSize(14)
        infographic.setFace('helvetica')
        infographic.setTextColor("white")
        infographic.draw(self.orbitWin)

    def close(self):
        """closes the window"""
        self.orbitWin.close()
        
    def mainLoop(self):
        """The main loop in which planetary movements will update."""
        
        paused = False
 
        while True:
            sleep(1/90)
            
            key = self.orbitWin.checkKey()
            if key == 'q':
                print("Quitting...")
                return
            if key == 'p':
                paused = not paused
                print("Paused:" + str(paused))

            if not paused: 
                self.planet.updatePosition()

class mainWin:
    def __init__(self, width = 600, length = 600):
        self.mainWin = GraphWin("Kepler's Planetary Orbits", width, length)
        self.mainWin.setBackground("slate Gray")
        self.mainWin.setCoords(-250, -250, 250, 250)

    def close(self):
        """closes window"""
        self.mainWin.close()

    def showText(self):
        """displays text on window"""
        welcome = Text(Point(0,200), "Welcome to Kepler's Planetary Orbits Simulation \n  \nBy \
✨Troy Pelczarski✨ and ✨Feras Natsheh✨ \n \nWhat planet would you like see orbit the Sun?")
        welcome.setFace("courier")
        welcome.setSize(13)
        welcome.setTextColor("white")
        welcome.draw(self.mainWin)

        quitText = Text(Point(0, -225), "Press anywhere on the screen or the 'q' key to quit the program")
        quitText.setFace("courier")
        quitText.setSize(12)
        quitText.setTextColor("black")
        quitText.draw(self.mainWin)

    def showButtons(self):
        """displays buttons on windows"""
        self.mercuryButton = Button(Point(-30,150), Point(30,120), "Mercury")
        self.mercuryButton.draw(self.mainWin)
    
        self.venusButton = Button(Point(-30,110), Point(30,80), "Venus")
        self.venusButton.draw(self.mainWin)

        self.earthButton = Button(Point(-30, 70), Point(30,40), "Earth")
        self.earthButton.draw(self.mainWin)

        self.marsButton = Button(Point(-30,30), Point(30,0),"Mars")
        self.marsButton.draw(self.mainWin)

        self.jupiterButton = Button(Point(-30,-10), Point(30,-40), "Jupiter")
        self.jupiterButton.draw(self.mainWin)

        self.saturnButton = Button(Point(-30,-50), Point(30,-80), "Saturn")
        self.saturnButton.draw(self.mainWin)

        self.uranusButton = Button(Point(-30,-90), Point(30,-120), "Uranus")
        self.uranusButton.draw(self.mainWin)

        self.neptuneButton = Button(Point(-30,-130), Point(30,-160), "Neptune")
        self.neptuneButton.draw(self.mainWin)

        self.plutoButton = Button(Point(-30, -170), Point(30,-200), "Pluto")
        self.plutoButton.draw(self.mainWin)

    def mainLoop(self):
        """The main loop in which interface updates."""
        
        while True:
            mouseClick = self.mainWin.getMouse() 
            x,y  = mouseClick.getX(), mouseClick.getY() 

            if self.mercuryButton.clicked(x, y):
                mercuryOrbit = Orbit(0.21, 0.48)
                mercury = Planet(Point(0,0), mercuryOrbit, 75)
                sun = Star(Point(-75,0), 15)
                self.mainWin.close()
                simulation = orbitWin(sun, mercury, width= 900, length = 700)
                simulation.infoText()
                simulation.mainLoop()
                simulation.close()
    
            elif self.venusButton.clicked(x, y):
                venusOrbit = Orbit(0.01, 0.62)
                venus = Planet(Point(0,0), venusOrbit, 100)
                sun = Star(Point(-100,0), 15)
                self.mainWin.close()
                simulation = orbitWin(sun, venus, width= 900, length = 700)
                simulation.infoText()
                simulation.mainLoop()
                simulation.close()

            elif self.earthButton.clicked(x, y):
                earthOrbit = Orbit(0.02, 1)
                earth = Planet(Point(0,0), earthOrbit, 125)
                sun = Star(Point(-125,0), 15)
                self.mainWin.close()
                simulation = orbitWin(sun, earth, width= 900, length = 700)
                simulation.infoText()
                simulation.mainLoop()
                simulation.close()

            elif self.marsButton.clicked(x, y):
                marsOrbit = Orbit(0.09, 1.88)
                mars = Planet(Point(0,0), marsOrbit, 150)
                sun = Star(Point(-180,0), 15)
                self.mainWin.close()
                simulation = orbitWin(sun, mars, width= 900, length = 700)
                simulation.infoText()
                simulation.mainLoop()
                simulation.close()

            elif self.jupiterButton.clicked(x, y):
                jupiterOrbit = Orbit(0.05, 11.86)
                jupiter = Planet(Point(0,0), jupiterOrbit, 175)
                sun = Star(Point(-250,0), 9)
                self.mainWin.close()
                simulation = orbitWin(sun, jupiter, width= 1125, length = 875)
                simulation.infoText()
                simulation.mainLoop()
                simulation.close()

            elif self.saturnButton.clicked(x, y):
                saturnOrbit = Orbit(0.05, 29.46)
                saturn = Planet(Point(0,0), saturnOrbit, 175)
                sun = Star(Point(-275,0), 8)
                self.mainWin.close()
                simulation = orbitWin(sun, saturn, width= 1125, length = 875)
                simulation.infoText()
                simulation.mainLoop()
                simulation.close()

            elif self.uranusButton.clicked(x, y):
                uranusOrbit = Orbit(0.05, 27)
                uranus = Planet(Point(0,0), uranusOrbit, 175)
                sun = Star(Point(-250,0), 7)
                self.mainWin.close()
                simulation = orbitWin(sun, uranus, width= 1125, length = 875)
                simulation.infoText()
                simulation.mainLoop()
                simulation.close()

            elif self.neptuneButton.clicked(x, y):
                neptuneOrbit = Orbit(0.01, 35)
                neptune = Planet(Point(0,0), neptuneOrbit, 150)
                sun = Star(Point(-275,0), 7)
                self.mainWin.close()
                simulation = orbitWin(sun, neptune, width= 1125, length = 875)
                simulation.infoText()
                simulation.mainLoop()
                simulation.close()

            elif self.plutoButton.clicked(x, y):
                plutoOrbit = Orbit(0.25, 25)
                pluto = Planet(Point(0,0), plutoOrbit, 175)
                sun = Star(Point(-350,0), 7)
                self.mainWin.close()
                simulation = orbitWin(sun, pluto, width= 1125, length = 875)
                simulation.infoText()
                simulation.mainLoop()
                simulation.close()
            return
        return 
        
        
        