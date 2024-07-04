# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:31:23 2022

Author(s): Troy Pelczarski and Feras Natsheh 
"""

from kepler import * 
from graphics import * 

def main():

    window = mainWin(600, 600)
    window.showButtons()
    window.showText()
    window.mainLoop()
    window.close()
    
    
if __name__ == "__main__":
    main()