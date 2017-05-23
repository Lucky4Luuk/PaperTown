#-----------------------#
#-  Standard Libraries -#
#-----------------------#
import tkinter as tk
import math
import random

#-----------------------#
#-   Custom Libraries  -#
#-----------------------#
from classlib import *

#-----------------------#
#-      Variables      -#
#-----------------------#
camx = 0
camy = 0

#-----------------------#
#-       Classes       -#
#-----------------------#
class Object() :
    def __init__(self,x,y,filename) :
        self.x = x
        self.y = y
        self.file = tk.PhotoImage(file=filename)

    def draw(self) :
        global camx, camy
        w.create_image(self.x-camx,self.y-camy,image=self.file)

class Map() :
    def __init__(self,x,y,filename,name) :
        self.x = x
        self.y = y
        self.file = tk.PhotoImage(file=filename)
        self.name = name

    def draw(self) :
        global camx, camy
        w.create_image(self.x-camx,self.y-camy,image=self.file)

#-----------------------#
#-     Functions       -#
#-----------------------#


#-----------------------#
#-       Setup         -#
#-----------------------#
root = tk.Tk()
w = tk.Canvas(root,width=800,height=600)
w.pack()

#-----------------------#
#-        Code         -#
#-----------------------#

player = Player(0,0,input("Name: "))
#stone001 = Object(0,0,"stone.gif")
map_main = Map(0,0,"maps/main_map.gif","main_map")

def gameloop() :
    w.delete("all")
    map_main.draw()
    w.after(1,gameloop)

gameloop()

root.mainloop()
