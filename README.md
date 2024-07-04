# planetarydynamicsgraphics
Interactive graphical simulation of planetary motions

This project was created for a course final project for CS-167: Computational Problem Solving at Whitman College, taken Fall 2022. 

In this folder, you will find four python files. The graphics package is the one used in class, we have based our graphics on it. 
The button.py file is a modified version of the button module we worked in class. It contains code to make buttons that detect press.
kepler is the main file where we compiled our code. It has all the classes neccessary for the program to run, but no main function is constructed nor called. 
runkepler contains the main function that executes and runs the program 

To run the simulation: 
    open runkepler.py 
    Run the file
    A main-menu window should show up, it will ask the user to click on the button for the planet they would like to see 
    a new pop-up window will show the graphics of the simulation along with infographic visual texts
    To run a new simulation or a different planet, quit the program by either pressing 'q' or retarting the kernel. Then run it again and choose your option.

The following is a (optional) detailed breakdown of the classes used in kepler.py:
    class Star: this class represents the star object. It sets the location and radius attributes of the star. Star in the program is commonly known as our solar Sun. 

    class Orbit: This class represents the orbit object. It contains most of the physics behind the orbital path each planet takes. 

        periodToSemiMajorAxis(self): this takes in the self.p values and converts them to semi-major axis values 'a', which is used in the following function
        
        generatePolarCoordinates(self): this function takes in the input self.p, self.e, and 'a' values and generates self.theta, a list that contains 500 angles evenly spaced out. 

        makeOrbit(self): this function takes in all previous functions and operates on the list self.theta, it takes in the 500 angles in self.theta and converts them into polar coordinates (r, theta). It then takes values of self.r and converts                           them into cartesian sets of coordinates (x,y). So this function returns 500 sets of (x,y) coordinates that planets take

    class Planet: This class represents the planet object. 

        draw(self, win): draws the planet on the chosen graphic window

        updatePosition(self): updates the planet's position by moving through the list of (x,y) coordinates generated in makeOrbit(self). 

    class orbitWin: this class represents the orbit simulation graphic window. It contains infographic texts under infoText() and its mainLoop() calls the updatePosition() function repeatedly, which causes the planet to move in designated orbit. 

    class mainWin: this class represents the main menu graphic window. it contains the meat of the program. 

        showText(self): displays the visual texts on the screen 

        showButtons(self): generates buttons for the 8 planets

        mainLoop(self): this is the mainloop that updates the main menu interface. It keeps the screen running until futher action. Action can be either clicking on one of the buttons or quitting by clicking anywhere that's not a button or pressing 'q' 
        This function contains the click detection for all buttons, each button has its own preset of coordinates, self.e, self.p, and sun radius values. Once a button is clicked, it fetches the preset outlined under each button and runs the orbitWin window showing that specific simulation. 
        

