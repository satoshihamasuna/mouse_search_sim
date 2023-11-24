import os
import sys
import datetime
import math
import numpy as np
import matplotlib.pyplot as plt

class Maze():
    North,East,South,West = range(4)
    def __init__(self,x,y):
        #North,East,South,West = range(4)

        self.maze_size_x = x
        self.maze_size_y = y

        self.wall = np.zeros((self.maze_size_x,self.maze_size_y,4),dtype=bool)

        #self.steps = np.zeros((self.maze_size_x,self.maze_size_y))

        for xx in range(self.maze_size_x):
            for yy in range(self.maze_size_y):
                if yy == self.maze_size_y - 1:
                   self.wall[xx][yy][Maze.North] = True
                
                if yy == 0:
                   self.wall[xx][yy][Maze.South] = True
                
                if xx == self.maze_size_x - 1:
                   self.wall[xx][yy][Maze.East] = True
                
                if xx == 0:
                   self.wall[xx][yy][Maze.West] = True

        self.wall[0][0][Maze.East] = self.wall[1][0][Maze.West] = True

    def disp_map(self):
        for yy in range(self.maze_size_y - 1 , -1 , -1):
            for xx in range(self.maze_size_x):
                if self.wall[xx][yy][Maze.North] == True:
                    print("+---",end='')
                else:
                    print("+   ",end='')

                if xx == self.maze_size_x - 1:
                    print("+")
                    
            for xx in range(self.maze_size_x):
                if self.wall[xx][yy][Maze.West] == True:
                    print("|   ",end='')
                else:
                    print("    ",end='')
                if xx == self.maze_size_x - 1:
                    if self.wall[xx][yy][Maze.East] == True:
                        print("|")
                    else:
                        print(" ")

        for xx in range(self.maze_size_x):
            print("+---",end='')
        print("+")

    def draw_maze(self):
        #壁の描画
        for yy in range(self.maze_size_y - 1 , -1 , -1):
            for xx in range(self.maze_size_x):
                if self.wall[xx][yy][Maze.North] == True:
                    x =[xx-1/2,xx+1/2]
                    y =[yy+1/2,yy+1/2]
                    plt.plot(x,y,'r')
                    plt.plot(x,y,'r+')
                else:
                    x =[xx-1/2,xx+1/2]
                    y =[yy+1/2,yy+1/2]
                    plt.plot(x,y,'r+')
                    
                if self.wall[xx][yy][Maze.West] == True:
                    x =[xx-1/2,xx-1/2]
                    y =[yy-1/2,yy+1/2]
                    plt.plot(x,y,'r')
                    plt.plot(x,y,'r+')
                else:
                    x =[xx-1/2,xx-1/2]
                    y =[yy-1/2,yy+1/2]
                    plt.plot(x,y,'w')
                    plt.plot(x,y,'r+')
                if xx == self.maze_size_x - 1:
                    if self.wall[xx][yy][Maze.East] == True:
                        x =[xx+1/2,xx+1/2]
                        y =[yy-1/2,yy+1/2]
                        plt.plot(x,y,'r')
                        plt.plot(x,y,'r+')
                    else:
                        x =[xx+1/2,xx+1/2]
                        y =[yy-1/2,yy+1/2]
                        plt.plot(x,y,'w')
                        plt.plot(x,y,'r+')
                if yy == 0:
                    if self.wall[xx][yy][Maze.South] == True:
                        x =[xx-1/2,xx+1/2]
                        y =[yy-1/2,yy-1/2]
                        plt.plot(x,y,'r')
                        plt.plot(x,y,'r+')
                    else:
                        x =[xx-1/2,xx+1/2]
                        y =[yy-1/2,yy-1/2]
                        plt.plot(x,y,'w')
                        plt.plot(x,y,'r.')
 
        plt.xticks(range(0,self.maze_size_x+1,1))
        plt.yticks(range(0,self.maze_size_y+1,1))
        plt.xlim([-3/4,self.maze_size_x-1/4])
        plt.ylim([-3/4,self.maze_size_y-1/4])                     
        #plt.show()

    def attach_wall_toggle(self):
        plt.connect('button_press_event', self.button_press_event)
    
    def button_press_event(self,event):
        x , y = event.xdata,event.ydata
        xf, xi = math.modf(x)
        #xfが小数部分,xiが整数部分
        yf, yi = math.modf(y)

        if abs(xf-1/2) < abs(yf-1/2):
            xx , yy = int(round(x-1/2)),int(round(y))
            if xx >= 0 and yy >= 0:
                xp =[xx+1/2,xx+1/2]
                yp =[yy-1/2,yy+1/2]
                if  self.wall[xx][yy][Maze.East]:
                    self.wall[xx][yy][Maze.East] = False
                    self.wall[xx+1][yy][Maze.West] = False
                    plt.plot(xp,yp,'w',lw = 3)
                    plt.plot(xp,yp,'r+')
                
                else:
                    self.wall[xx][yy][Maze.East] = True
                    self.wall[xx+1][yy][Maze.West] = True
                    plt.plot(xp,yp,'r')
                    plt.plot(xp,yp,'r+')

        else:
            xx , yy = int(round(x)),int(round(y-1/2))
            if xx >= 0 and yy >= 0: 
                xp =[xx-1/2,xx+1/2]
                yp =[yy+1/2,yy+1/2]
                if  self.wall[xx][yy][Maze.North]:
                    self.wall[xx][yy][Maze.North] = False
                    self.wall[xx][yy+1][Maze.South] = False
                    plt.plot(xp,yp,'w',lw = 3)
                    plt.plot(xp,yp,'r+')
                else:
                    self.wall[xx][yy][Maze.North] = True
                    self.wall[xx][yy+1][Maze.South] = True
                    plt.plot(xp,yp,'r')
                    plt.plot(xp,yp,'r+')
        
        print(xx,yy,xi,yi)
        self.disp_map()
        plt.draw()

if __name__ == "__main__":


    test = Maze(16,16)
    #test.disp_map()
    test.draw_maze()
    test.attach_wall_toggle()

    plt.show()