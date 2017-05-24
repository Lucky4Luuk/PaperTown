#-----------------------#
#-  Standard Libraries -#
#-----------------------#
import tkinter as tk
import math
import random
import ast

#-----------------------#
#-   Custom Libraries  -#
#-----------------------#
from classlib import *

#-----------------------#
#-      Variables      -#
#-----------------------#
camx = 0
camy = 0
cutscene = "intro"
in_menu = False

#-----------------------#
#-     Functions       -#
#-----------------------#
def toNextScene(curscene) :
    global cutscene
    if curscene == "intro" :
        if player.isAt(400,300-64,32) :
            cutscene = ""

def move(event) :
    if cutscene == "" :
        player.moveto(event.x,event.y)
    if in_menu == True :
        print(event.x,event.y)
    elif cutscene != "" :
        toNextScene(cutscene)

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
    def __init__(self,x,y,filename,n_filename,name,size=(64,64)) :
        self.x = x
        self.y = y
        self.file = tk.PhotoImage(file=filename)
        self.n_file = tk.PhotoImage(file=n_filename)
        self.name = name
        self.size = size

    def draw(self) :
        w.create_image(self.x+self.size[0]/2,self.y+self.size[1]/2,image=self.file)

class Player() :
    def __init__(self,x,y,name) :
        self.x = x
        self.y = y
        self.gotox = 400
        self.gotoy = 300
        self.name = name
        self.file = tk.PhotoImage(file="textures/basic_player.gif")
        self.l_file = tk.PhotoImage(file="textures/basic_player_left.gif")
        self.speed = 1
        self.state = "right"

        #Fight Variables
        self.attack = False
        self.dmg = 1

        #Inventory
        self.items = []

    def isAt(self,x,y,r) :
        if abs(self.x - x) < r :
            if abs(self.y - y) < r :
                return True
        return False

    def moveto(self,x,y) :
        self.gotox = x
        self.gotoy = y

    def hasItem(self,itemname) :
        if itemname in self.items :
            return True
        else :
            return False

    def getName(self) :
        return self.name

    def giveItem(self,itemname) :
        self.items.append(itemname)

    def getVar(self,varname) :
        return ast.literal_eval("self.{0}".format(varname))

    def setVar(self,varname,value) :
        return ast.literal_eval("self.{0} = value".format(varname))

    def update(self) :
        if self.gotox > self.x+32 :
            self.mright()
        elif self.gotox < self.x+32 :
            self.mleft()
        if self.gotoy > self.y+64 :
            self.mdown()
        elif self.gotoy < self.y+64 :
            self.mup()

    def draw(self) :
        if self.state == "right" :
            w.create_image(self.x+32,self.y+32,image=self.file)
        elif self.state == "left" :
            w.create_image(self.x+32,self.y+32,image=self.l_file)
        w.create_text(self.x+32,self.y-12,text=self.name)

    def mup(self) :
        self.y -= self.speed

    def mdown(self) :
        self.y += self.speed

    def mright(self) :
        self.state = "right"
        self.x += self.speed

    def mleft(self) :
        self.state = "left"
        self.x -= self.speed

#-----------------------#
#-       Setup         -#
#-----------------------#
root = tk.Tk()
w = tk.Canvas(root,width=800,height=600)
w.pack()

#-----------------------#
#-        Code         -#
#-----------------------#

player = Player(-64,300-64,"Luuk")
#stone001 = Object(0,0,"stone.gif","n_stone.gif","stone001")
map_main = Map(0,0,"maps/main_map.gif","main_map")

def gameloop() :
    w.delete("all")
    map_main.draw()
    player.update()
    player.draw()
    w.after(1,gameloop)

gameloop()

root.bind("<Button-1>",move)

root.mainloop()
