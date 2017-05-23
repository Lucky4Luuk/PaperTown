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
#-     Functions       -#
#-----------------------#


#-----------------------#
#-       Classes       -#
#-----------------------#
class Map() :
    def __init__(self,x,y,filename,name,size=(1024,512)) :
        self.x = x
        self.y = y
        self.file = tk.PhotoImage(file=filename)
        self.name = name
        self.size = size

    def draw(self) :
        w.create_image(self.x+self.size[0]/2,self.y+self.size[1]/2,image=self.file)

class Object() :
    def __init__(self,x,y,filename,name,size=(64,64)) :
        self.x = x
        self.y = y
        self.file = tk.PhotoImage(file=filename)
        self.name = name
        self.size = size

    def draw(self) :
        w.create_image(self.x+self.size[0]/2,self.y+self.size[1]/2,image=self.file)

class Player() :
    def __init__(self,x,y,name) :
        self.x = x
        self.y = y
        self.name = name
        self.file = tk.PhotoImage(file="textures/basic_player.gif")

    def draw(self) :
        w.create_image(self.x+32,self.y+32,image=self.file)
        w.create_text(self.x+32,self.y-12,text=self.name)

#-----------------------#
#-       Setup         -#
#-----------------------#
root = tk.Tk()
w = tk.Canvas(root,width=800,height=600)
w.pack()

#-----------------------#
#-        Code         -#
#-----------------------#

player = Player(0,20,input("Name: "))
#stone001 = Object(0,0,"stone.gif","stone001")
map_main = Map(0,0,"maps/main_map.gif","main_map")

def gameloop() :
    w.delete("all")
    map_main.draw()
    player.draw()
    w.after(1,gameloop)

gameloop()

root.mainloop()
