import os
import sys
import datetime
import math
import numpy as np
from maze import Maze
import matplotlib.pyplot as plt
import time

class Run():
    North,East,South,West = range(4)
    sleeptime = 0.001
    #sleeptime = 1
    def staright_HSTEP(self,x,y,dir):   #x:初期位置，y:初期位置 ，dir:初期の向き
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x,y+1/2

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y

        elif dir == Run.South:
            c,=plt.plot(x,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x,y-1/2

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y
            
    def staright_STEP(self,x,y,dir):    #x:初期位置，y:初期位置 ，dir:初期の向き
        inx,iny = x,y
        inx,iny = self.staright_HSTEP(inx,iny,dir)
        inx,iny = self.staright_HSTEP(inx,iny,dir)
        return inx,iny
   
    def staright_STEP_ACCEL(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='red')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            #c,=plt.plot(x,y+1/2,marker='o',color='red') 
            #plt.draw()
            #plt.pause(Run.sleeptime)
            #c.remove()
            c,=plt.plot(x,y+1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x,y+1

        elif dir == Run.East:
            #c,=plt.plot(x+1/2,y,marker='o',color='red') 
            #plt.draw()
            #plt.pause(Run.sleeptime)
            #c.remove()
            c,=plt.plot(x+1,y,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y

        elif dir == Run.South:
            #c,=plt.plot(x,y-1/2,marker='o',color='red') 
            #plt.draw()
            #plt.pause(Run.sleeptime)
            #c.remove()
            c,=plt.plot(x,y-1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x,y-1

        elif dir == Run.West:
            #c,=plt.plot(x-1/2,y,marker='o',color='red') 
            #plt.draw()
            #plt.pause(Run.sleeptime)
            #c.remove()
            c,=plt.plot(x-1,y,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove() 
            return x-1,y             

    def in_R45(self,x,y,dir):   #x:初期位置，y:初期位置 ，dir:初期の向き
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y+1

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y-1/2

        elif dir == Run.South:
            c,=plt.plot(x,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y-1

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y+1/2

    def out_R45(self,x,y,dir):  #x:初期位置，y:初期位置 ，dir:初期の向き
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y+1/2

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y-1

        elif dir == Run.South:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y-1/2

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y+1

    def in_L45(self,x,y,dir):   #x:初期位置，y:初期位置 ，dir:初期の向き
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y+1

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y+1/2

        elif dir == Run.South:
            c,=plt.plot(x,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y-1

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y-1/2

    def out_L45(self,x,y,dir):  #x:初期位置，y:初期位置 ，dir:初期の向き
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y+1/2

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y+1

        elif dir == Run.South:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y-1/2

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y-1

    def R_V90(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x,y-1

        elif dir == Run.South:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x,y+1

    def L_V90(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x,y+1

        elif dir == Run.South:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x,y-1

    def R_Diagonal(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y+1/2

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y-1/2

        elif dir == Run.South:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y-1/2

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y+1/2

    def L_Diagonal(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y+1/2

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y+1/2

        elif dir == Run.South:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y-1/2

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y-1/2

    def R_Diagonal_ACCEL(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='red')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y+1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y+1

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y-1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y-1

        elif dir == Run.South:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y-1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y-1

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y+1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y+1

    def L_Diagonal_ACCEL(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='red')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y+1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y+1

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y+1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y+1

        elif dir == Run.South:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y-1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y-1

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y-1,marker='o',color='red') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y-1

    def in_R135(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y+1/2

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y-1

        elif dir == Run.South:
            c,=plt.plot(x,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y-1/2

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y+1

    def out_R135(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()

        if dir == Run.North:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y-1/2

        elif dir == Run.East:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y-1

        elif dir == Run.South:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y+1/2

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y+1

    def in_L135(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()
        
        if dir == Run.North:
            c,=plt.plot(x,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y+1/2
        
        elif dir == Run.East:
            c,=plt.plot(x+1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y+1
        
        elif dir == Run.South:
            c,=plt.plot(x,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y-1/2
        
        elif dir == Run.West:
            c,=plt.plot(x-1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y-1
    
    def out_L135(self,x,y,dir):
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()
        
        if dir == Run.North:
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1,y-1/2
        
        elif dir == Run.East:
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y+1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y+1
        
        elif dir == Run.South:
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1,y+1/2
        
        elif dir == Run.West:
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y-1,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y-1

    def turn_R90(self,x,y,dir):    #x:初期位置，y:初期位置 ，dir:初期の向き
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()
        
        if dir == Run.North:
            c,=plt.plot(x,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y+1/2
        
        elif dir == Run.East:
            c,=plt.plot(x+1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y-1/2
        
        elif dir == Run.South:
            c,=plt.plot(x,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y-1/2

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y+1/2

    def turn_L90(self,x,y,dir):    #x:初期位置，y:初期位置 ，dir:初期の向き
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()
        
        if dir == Run.North:
            c,=plt.plot(x,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y+1/2
        
        elif dir == Run.East:
            c,=plt.plot(x+1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y+1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y+1/2
        
        elif dir == Run.South:
            c,=plt.plot(x,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x+1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x+1/2,y-1/2

        elif dir == Run.West:
            c,=plt.plot(x-1/2,y,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            c,=plt.plot(x-1/2,y-1/2,marker='o',color='black') 
            plt.draw()
            plt.pause(Run.sleeptime)
            c.remove()
            return x-1/2,y-1/2

    def turn180(self,x,y,dir):
        self.staright_HSTEP(x,y,dir)
        c, =plt.plot(x,y,marker='o',color='black')
        plt.draw()
        plt.pause(Run.sleeptime)
        c.remove()
        return x,y

if __name__ == "__main__":  
    maze  = Maze(16,16)
    maze.draw_maze()
    test = Run()
    x,y=test.R_Diagonal_ACCEL(2,2+1/2,test.West)
    print(x,y)
    plt.show()