import os
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.widgets import Button
from maze import Maze
import tkinter

#迷路サイズの設定
x_size = 16
y_size = 16

maze = Maze(x_size,y_size)

maze.draw_maze()
maze.attach_wall_toggle()

#スタート位置の設定[[x,y]]
start_position = [[0 , 0]]
#ゴール位置の設定[[x1,y1],[x2,y2],...]
goal_position = [[7,7],[7,8],[8,7],[8,8]]

for ps,t in [[start_position,'S'],[goal_position,'G']]:
    for p in ps:
        plt.text(p[0],p[1],t,ha='center', va='center')

plt.show()

def save():
    name = txt_1.get()
    path = os.getcwd()
    extension = '.txt'
    filename = path+'\\maze_data\\'+name+extension 
    f = open(filename,'w')
    
    f.write('Maze_Wall_Data\n')
    for yy in range(maze.maze_size_y):
        for xx in range(maze.maze_size_x):
            save_data =   str(maze.wall[xx][yy][maze.North]) + ',' \
                        + str(maze.wall[xx][yy][maze.East])  + ',' \
                        + str(maze.wall[xx][yy][maze.South]) + ',' \
                        + str(maze.wall[xx][yy][maze.West])  + ','
            f.write(save_data)
        f.write('\n')
    
    f.write('\nMaze_Start_Goal_Data\n')
    for ps,t in [[start_position,'S'],[goal_position,'G']]:
        for p in ps:
            save_data = str(p[0]) +',' + str(p[1]) +','+t + '\n'
            f.write(save_data)
    f.write('\n')
    f.close()
    print('save!->',filename)

if __name__ == "__main__":
    tki = tkinter.Tk()
    tki.geometry('300x200')
    tki.title('savebutton')

    lbl_1 = tkinter.Label(text='ファイル名')
    lbl_1.place(x=30, y=70)

    txt_1 = tkinter.Entry(width=20)
    txt_1.place(x=90, y=70)

    btn = tkinter.Button(tki, text='保存', command=save)
    btn.place(x=140, y=170)

    tki.mainloop()



