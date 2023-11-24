import os
import numpy as np
import math
import matplotlib.pyplot as plt
#from matplotlib.widgets import Button
from maze import Maze
from distutils.util import strtobool
from run import Run

#ファイルの読み取り
class read_maze():
    def __init__(self,name):
        #name = '35_AllJapan_Student_maze'
        path = os.getcwd()
        extension = '.txt'
        self.filename = path+'\\maze_data\\'+name+extension 
        self.f = open(self.filename,'r')
        self.s = self.f.read()
        self.f.close()
        
        self.x_cnt, self.y_cnt = 0,0 
        self.data1 = self.s.split('\n')
        while self.data1[self.y_cnt] != 'Maze_Start_Goal_Data': self.y_cnt = self.y_cnt+1
        del self.data1[0]
        del self.data1[self.y_cnt-2]
        self.y_cnt = self.y_cnt-2
        

        data2 = self.data1[0].split(',')
        del data2[len(data2)-1]
        
        self.x_cnt = int(len(data2)/4)
        self.read()
    
    #迷路チE�Eタの読み取り
    def read(self):
        self.maze_wall_data = np.zeros((self.x_cnt,self.y_cnt,4),dtype= bool)
        for yy in range(self.y_cnt):
            data3 = self.data1[yy].split(',')
            del data3[len(data3)-1]
            xx = 0
            for cnt in range(len(data3)):
                if cnt%4 == 0 and cnt > 0:
                    xx = xx + 1
                self.maze_wall_data[xx][yy][cnt%4] = strtobool(data3[cnt])

        data4 = self.data1

        while data4[0] != 'Maze_Start_Goal_Data':
            del data4[0]
        del data4[0]

        del data4[len(data4)-1]
        del data4[len(data4)-1]
        s_cnt,g_cnt = 0,0
        s_max_x,s_max_y = 0,0
        g_max_x,g_max_y = 0,0
        for i in range(len(data4)):
            data4[i] = data4[i].split(',')
            if data4[i][2] == 'S':
                s_cnt = s_cnt + 1
                if int(data4[i][0]) > s_max_x:
                    s_max_x = int(data4[i][0])
                if int(data4[i][1]) > s_max_y:
                    s_max_y = int(data4[i][1])

            if data4[i][2] == 'G':
                g_cnt = g_cnt + 1
                if int(data4[i][0]) > g_max_x:
                    g_max_x = int(data4[i][0])
                if int(data4[i][1]) > s_max_y:
                    g_max_y = int(data4[i][1])

        s_cnt = int(math.sqrt(s_cnt))
        g_cnt = int(math.sqrt(g_cnt))
              
        self.sx,self.sy = np.zeros(s_cnt,dtype=int),np.zeros(s_cnt,dtype=int)
        self.gx,self.gy = np.zeros(g_cnt,dtype=int),np.zeros(g_cnt,dtype=int)

        for i in range(s_cnt):
            self.sx[i] = s_max_x - i
            self.sy[i] = s_max_y - i
        for i in range(g_cnt):
            self.gx[i] = g_max_x - i
            self.gy[i] = g_max_y - i

        print(self.sx,self.sy,self.gx,self.gy)

class adachi():
    SEARCH_MASK = 0x01
    NOWALL,WALL,UNKNOWN,VWALL = range(4)
    North,East,South,West = range(4)
    front,right,rear,left = range(4)
    
    #run_mode定義
    straight_HSTEP,turn_R90,turn180,turn_L90 = range(1,5,1)
    diag_R,diag_L = range(5,7,1)
    in_R45,out_R45,in_L45,out_L45 = range(7,11,1)
    in_R135,out_R135,in_L135,out_L135 = range(11,15,1)
    v_R90,v_L90 = range(15,17,1)
    goal = 0xff

    def __init__(self,size_x,size_y,sx,sy,gx,gy,wall_data):
        self.size_x  , self.size_y = size_x,size_y
        
        self.start_x , self.start_y = sx,sy
        self.goal_x  , self.goal_y = gx,gy
        
        plt.text(0,0,'S',ha='center', va='center')
        
        for xx in range(len(self.goal_x)):
            for yy in range(len(self.goal_y)):
                plt.text(self.goal_x[xx],self.goal_y[yy],'G',ha='center', va='center')

        self.mypos_x,self.mypos_y = self.start_x,self.start_y 
        self.mypos_dir = adachi.North
        self.next_dir  = adachi.North
        self.rmypos_x,self.rmypos_y = self.start_x,self.start_y

        self.wall = np.zeros((size_x,size_y,4),dtype=bool)
        self.wall = wall_data
        self.is_wall = np.zeros((size_x,size_y,4),dtype=int)
        self.tmp_dir = np.zeros((size_x,size_y),dtype=int)
        
        self.end_search = 0
        self.run_mode = 0

        for xx in range(self.size_x):
            for yy in range(self.size_x):
                self.is_wall[xx][yy][adachi.North] = adachi.UNKNOWN
                self.is_wall[xx][yy][adachi.East] = adachi.UNKNOWN
                self.is_wall[xx][yy][adachi.South] = adachi.UNKNOWN
                self.is_wall[xx][yy][adachi.West] = adachi.UNKNOWN

        for xx in range(self.size_x):
            self.is_wall[xx][0][adachi.South] = adachi.WALL
            self.is_wall[xx][self.size_y-1][adachi.North] = adachi.WALL


        for yy in range(self.size_y):
            self.is_wall[0][yy][adachi.West] = adachi.WALL
            self.is_wall[self.size_x-1][yy][adachi.East] = adachi.WALL

        self.is_wall[0][0][adachi.East] = self.is_wall[1][0][adachi.West] = adachi.WALL
    

        self.map = np.zeros((size_x,size_y),dtype=int)
        self.pre_map = np.zeros((size_x,size_y),dtype=int)
        self.map_goal = np.zeros((size_x,size_y),dtype=int)

    def is_unknwon(self,x,y):
        if self.is_wall[x][y][adachi.North] == adachi.UNKNOWN or self.is_wall[x][y][adachi.East] == adachi.UNKNOWN or self.is_wall[x][y][adachi.South]== adachi.UNKNOWN or self.is_wall[x][y][adachi.West]== adachi.UNKNOWN:
            return True
        else:
            return False

    def init_map(self,x,y):
        for xx in range(self.size_x):
            for yy in range(self.size_y):
                self.map[xx][yy] = 999
        #self.map[x][y] = 0
        
        for i in range(len(x)):
            for j in range(len(y)):
                self.map[x[i]][y[j]] = 0
            
    def make_map(self,x,y,mask):
        change_flag = False 
        self.init_map(x,y)
        while True:    
            change_flag = False 
            for xx in range(self.size_x):
                for yy in range(self.size_y):
                    if self.map[xx][yy] == 999:
                        continue
                    if yy < self.size_y - 1 :
                        if (self.is_wall[xx][yy][adachi.North] & mask)  == adachi.NOWALL:
                            if self.map[xx][yy+1] == 999:
                                self.map[xx][yy+1] = self.map[xx][yy] + 1
                                change_flag = True
                    if xx < self.size_x - 1 :
                        if (self.is_wall[xx][yy][adachi.East] & mask)  == adachi.NOWALL:
                            if self.map[xx+1][yy] == 999:
                                self.map[xx+1][yy] =self.map[xx][yy] + 1
                                change_flag = True
                    if yy > 0 :
                        if (self.is_wall[xx][yy][adachi.South] & mask)  == adachi.NOWALL:
                            if self.map[xx][yy-1] == 999:
                                self.map[xx][yy-1] = self.map[xx][yy] + 1
                                change_flag = True
                    if xx > 0 :
                        if (self.is_wall[xx][yy][adachi.West] & mask)  == adachi.NOWALL:
                            if self.map[xx-1][yy] == 999:
                                self.map[xx-1][yy] = self.map[xx][yy] + 1
                                change_flag = True
            #self.disp_step()
            if change_flag != True:
                break

    def set_wall(self,x,y):
        if self.wall[x][y][adachi.North] == True:
            self.is_wall[x][y][adachi.North]    = adachi.WALL
        else:
            self.is_wall[x][y][adachi.North]    = adachi.NOWALL
        
        if self.wall[x][y][adachi.East] == True:
            self.is_wall[x][y][adachi.East]    = adachi.WALL
        else:
            self.is_wall[x][y][adachi.East]    = adachi.NOWALL

        if self.wall[x][y][adachi.South] == True:
            self.is_wall[x][y][adachi.South]    = adachi.WALL
        else:
            self.is_wall[x][y][adachi.South]    = adachi.NOWALL

        if self.wall[x][y][adachi.West] == True:
            self.is_wall[x][y][adachi.West]    = adachi.WALL
        else:
            self.is_wall[x][y][adachi.West]    = adachi.NOWALL

        if y < self.size_y - 1:
            if self.wall[x][y][adachi.North] == True:
                self.is_wall[x][y+1][adachi.South]    = adachi.WALL
            else:
                self.is_wall[x][y+1][adachi.South]    = adachi.NOWALL        
        
        if x < self.size_x - 1:
            if self.wall[x][y][adachi.East] == True:
                self.is_wall[x+1][y][adachi.West]    = adachi.WALL
            else:
                self.is_wall[x+1][y][adachi.West]    = adachi.NOWALL        

        if y > 0:
            if self.wall[x][y][adachi.South] == True:
                self.is_wall[x][y-1][adachi.North]    = adachi.WALL
            else:
                self.is_wall[x][y-1][adachi.North]    = adachi.NOWALL    
 
        if x > 0:
            if self.wall[x][y][adachi.West] == True:
                self.is_wall[x-1][y][adachi.East]    = adachi.WALL
            else:
                self.is_wall[x-1][y][adachi.East]   = adachi.NOWALL    

    def get_priority(self,x,y,dir):
        priority = 0
        if self.mypos_dir == dir:
            priority = 2
        elif ((4+self.mypos_dir - dir)%4) == 2:
            priority = 0
        else:
            priority = 1
        
        if self.is_unknwon(x,y) == True:
            priority = priority+4
        
        return priority
    
    def get_nextdir(self,x,y,mask):
        little,priority,tmp_priority = 0,0,0

        self.make_map(x,y,mask)

        little = 999

        if (self.is_wall[self.mypos_x][self.mypos_y][adachi.North] & mask)  == adachi.NOWALL:
            tmp_priority = self.get_priority(self.mypos_x,self.mypos_y+1,adachi.North)
            if self.map[self.mypos_x][self.mypos_y+1] < little:
                little = self.map[self.mypos_x][self.mypos_y+1]
                self.next_dir = adachi.North
                priority = tmp_priority
            elif self.map[self.mypos_x][self.mypos_y+1] == little:
                if priority < tmp_priority:    
                    self.next_dir = adachi.North
                    priority = tmp_priority 


        if (self.is_wall[self.mypos_x][self.mypos_y][adachi.East] & mask)  == adachi.NOWALL:
            tmp_priority = self.get_priority(self.mypos_x+1,self.mypos_y,adachi.East)
            if self.map[self.mypos_x+1][self.mypos_y] < little:
                little = self.map[self.mypos_x+1][self.mypos_y]
                self.next_dir = adachi.East
                priority = tmp_priority
            elif self.map[self.mypos_x+1][self.mypos_y] == little:
                if priority < tmp_priority:    
                    self.next_dir = adachi.East
                    priority = tmp_priority

        if (self.is_wall[self.mypos_x][self.mypos_y][adachi.South] & mask)  == adachi.NOWALL:
            tmp_priority = self.get_priority(self.mypos_x,self.mypos_y-1,adachi.South)
            if self.map[self.mypos_x][self.mypos_y-1] < little:
                little = self.map[self.mypos_x][self.mypos_y-1]
                self.next_dir = adachi.South
                priority = tmp_priority
            elif self.map[self.mypos_x][self.mypos_y-1] == little:
                if priority < tmp_priority:    
                    self.next_dir = adachi.South
                    priority = tmp_priority

        if (self.is_wall[self.mypos_x][self.mypos_y][adachi.West] & mask)  == adachi.NOWALL:
            tmp_priority = self.get_priority(self.mypos_x-1,self.mypos_y,adachi.West)
            if self.map[self.mypos_x-1][self.mypos_y] < little:
                little = self.map[self.mypos_x-1][self.mypos_y]
                self.next_dir = adachi.West
                priority = tmp_priority
            elif self.map[self.mypos_x-1][self.mypos_y] == little:
                if priority < tmp_priority:    
                    self.next_dir = adachi.West
                    priority = tmp_priority
        
        return (4+self.next_dir - self.mypos_dir) % 4

    def I_am_goal(self,x,y,gx,gy):
        flag = False
        for i in range(len(gx)):
            for j in range(len(gy)):
                if x == gx[i] and y == gy[j]:
                    flag = True
        return flag

    def search_adachi(self,gx,gy,mask):
        #elf.disp_walls()
        run = Run()
        #self.set_wall(self.mypos_x,self.mypos_y)
        self.run_mode = self.get_nextdir(gx,gy,mask)
        if self.run_mode == self.front:
            self.rmypos_x,self.rmypos_y = run.staright_HSTEP(self.rmypos_x,self.rmypos_y,self.mypos_dir)
        elif self.run_mode == self.right:
            self.rmypos_x,self.rmypos_y = run.staright_HSTEP(self.rmypos_x,self.rmypos_y,self.next_dir)
            #self.rmypos_x,self.rmypos_y = run.turn_R90(self.rmypos_x,self.rmypos_y,self.mypos_dir)
        elif self.run_mode == self.rear:
            #self.rmypos_x,self.rmypos_y = run.turn180(self.rmypos_x,self.rmypos_y,self.mypos_dir)
            self.rmypos_x,self.rmypos_y = run.staright_HSTEP(self.rmypos_x,self.rmypos_y,self.next_dir)
        elif self.run_mode == self.left:
            self.rmypos_x,self.rmypos_y = run.staright_HSTEP(self.rmypos_x,self.rmypos_y,self.next_dir)
            #self.rmypos_x,self.rmypos_y = run.turn_L90(self.rmypos_x,self.rmypos_y,self.mypos_dir)
        
        
        self.mypos_dir = self.next_dir
        if self.mypos_dir == adachi.North:
            self.mypos_y = self.mypos_y + 1
        elif self.mypos_dir == adachi.East:
            self.mypos_x = self.mypos_x + 1
        elif self.mypos_dir == adachi.South:
            self.mypos_y = self.mypos_y - 1
        elif self.mypos_dir == adachi.West:
            self.mypos_x = self.mypos_x - 1
        self.disp_walls()
        print(self.mypos_x,self.mypos_y,self.mypos_dir)

        while (self.I_am_goal(self.mypos_x,self.mypos_y,gx,gy) == False):
            self.set_wall(self.mypos_x,self.mypos_y)
            self.run_mode = self.get_nextdir(gx,gy,mask)
            if self.run_mode == self.front:
                self.rmypos_x,self.rmypos_y = run.staright_STEP(self.rmypos_x,self.rmypos_y,self.mypos_dir)
            elif self.run_mode == self.right:
                self.rmypos_x,self.rmypos_y = run.turn_R90(self.rmypos_x,self.rmypos_y,self.mypos_dir)
            elif self.run_mode == self.rear:
                self.rmypos_x,self.rmypos_y = run.turn180(self.rmypos_x,self.rmypos_y,self.mypos_dir)
            elif self.run_mode == self.left:
                self.rmypos_x,self.rmypos_y = run.turn_L90(self.rmypos_x,self.rmypos_y,self.mypos_dir)
            
            self.mypos_dir = self.next_dir
            if self.mypos_dir == adachi.North:
                self.mypos_y = self.mypos_y + 1
            elif self.mypos_dir == adachi.East:
                self.mypos_x = self.mypos_x + 1
            elif self.mypos_dir == adachi.South:
                self.mypos_y = self.mypos_y - 1
            elif self.mypos_dir == adachi.West:
                self.mypos_x = self.mypos_x - 1
            self.disp_walls()
            print(self.mypos_x,self.mypos_y,self.mypos_dir)
        
        self.set_wall(self.mypos_x,self.mypos_y)
        self.rmypos_x,self.rmypos_y = run.staright_HSTEP(self.rmypos_x,self.rmypos_y,self.mypos_dir)

    def disp_step(self):
        for yy in reversed(range(self.size_y)):
            for xx in range(self.size_x):
                print(self.map[xx][yy],',',end='')
            print()
        print()
    
    def disp_walls(self):
        for yy in range(self.size_y - 1 , -1 , -1):
            for xx in range(self.size_x):
                if self.is_wall[xx][yy][adachi.North] == adachi.WALL:
                    print("+---",end='')
                else:
                    print("+   ",end='')

                if xx == self.size_x - 1:
                    print("+")
                    
            for xx in range(self.size_x):
                if self.is_wall[xx][yy][adachi.West] == adachi.WALL:
                    print("|%3d"%self.map[xx][yy],end='')
                else:
                    print(" %3d"%self.map[xx][yy],end='')
                if xx == self.size_x - 1:
                    if self.is_wall[xx][yy][adachi.East] == adachi.WALL:
                        print("|")
                    else:
                        print(" ")

        for xx in range(self.size_x):
            print("+---",end='')
        print("+")

    def draw_steps(self):
        for xx in range(self.size_x):
            for yy in range(self.size_y):
                 plt.text(xx,yy,self.map[xx][yy],ha='center', va='center')
        plt.draw()
    
    def draw_steps_clear(self):
        for xx in range(self.size_x):
            for yy in range(self.size_y):
                 plt.text(xx,yy,' ',ha='center', va='center')
        plt.draw()

    def setup(self):
        self.mypos_x,self.mypos_y = self.start_x,self.start_y 
        self.mypos_dir = adachi.North
        self.next_dir  = adachi.North
        self.rmypos_x,self.rmypos_y = self.start_x,self.start_y

if __name__ == "__main__":
    read = read_maze('AllJapan_012_1991_Classic_Freshman_Class')
    maze = Maze(read.x_cnt,read.y_cnt)
    maze.wall = read.maze_wall_data
    maze.disp_map()
    maze.draw_maze()
    search = adachi(read.x_cnt,read.y_cnt,0,0,read.gx,read.gy,maze.wall)

    search.search_adachi(read.gx,read.gy,0x01)
    x = np.array([0])
    y = np.array([0])
    search.search_adachi(x,y,0x01)
    
    search.setup()
    search.search_adachi(read.gx,read.gy,0x03)

    plt.show()

