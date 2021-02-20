from parent_board import parent_board
import global_vars
import random
from bricks import add_a_brick

class board_elements(parent_board):

    def __init__(self,rows,columns):
        super().__init__(rows,columns)

    def add_bricks(self):
        bricks_height=random.randint(10,12)
        bricks_width=random.randint(global_vars.console_breadth-20,global_vars.console_breadth-10)
        xpos=5
        ypos=5
        for x in range (bricks_height):
            for y in range (bricks_width):
                if y%11==0:
                    self.add_to_board(xpos+x,ypos+y,"B",add_a_brick())

    def add_walls(self):
        (r,c)=self.board_dimension()
        if global_vars.degub==1:
            print(r,c)

        for row in range (r):
            self.add_to_board(row,0,"]","lwall")#left wall
            for column in range (c):
                if row==0 or row==r-1:
                    if column>0:
                        if row==0:
                            self.add_to_board(row,column,"x","twall")#top wall
                        if row==r-1:
                            self.add_to_board(row,column,"x","bwall")#bottom wall
                elif(column!=0 & column!=c-1):
                    self.add_to_board(row,column," ","default")
            self.add_to_board(row,column,"[","rwall")#right wall
        
    
    def add_paddle(self,x):
        y=x+global_vars.paddle_length
        (r,c)=self.board_dimension()
        for c in range (1,c-1):
            self.add_to_board(r-2,c," ","default")
        for c in range (x,y):
            self.add_to_board(r-2,c,"=","paddle")

    def add_ball(self,x,y):
            self.add_to_board(x,y,"*","ball")

    def ball_movement(self):

        if self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) not in ["twall","lwall","rwall","paddle"]:
            self.add_to_board(global_vars.ball_xpos,global_vars.ball_ypos," ","default")
        
        global_vars.ball_xpos+=global_vars.ball_xdir
        global_vars.ball_ypos+=global_vars.ball_ydir
        

        if "brick" in self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos):
            global_vars.score+=5

        if self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='twall':
            global_vars.ball_xdir=global_vars.ball_speed
            if global_vars.ball_ypos>global_vars.ball_ypos-global_vars.ball_ydir:
                global_vars.ball_ydir=global_vars.ball_speed
            else:
                global_vars.ball_ydir=-global_vars.ball_speed
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='lwall':
            global_vars.ball_ydir=global_vars.ball_speed
            if global_vars.ball_xpos>global_vars.ball_xpos-global_vars.ball_xdir:
                global_vars.ball_xdir=global_vars.ball_speed
            else:
                global_vars.ball_xdir=-global_vars.ball_speed
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='rwall':
            global_vars.ball_ydir=-global_vars.ball_speed
            if global_vars.ball_xpos>global_vars.ball_xpos-global_vars.ball_xdir:
                global_vars.ball_xdir=global_vars.ball_speed
            else:
                global_vars.ball_xdir=-global_vars.ball_speed
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='bwall':
            global_vars.lives-=1
            global_vars.paddle_pos=50
            global_vars.ball_xpos=global_vars.console_length-3
            global_vars.ball_ypos=55
            global_vars.ball_flag=0
            global_vars.ball_xdir=-global_vars.ball_speed
            global_vars.ball_ydir=global_vars.ball_speed
            if(global_vars.lives==0):
                global_vars.game_over=1
                return
            self.add_paddle(global_vars.paddle_pos)
            self.add_ball(global_vars.ball_xpos,global_vars.ball_ypos)
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='paddle':
            global_vars.ball_xdir=-global_vars.ball_speed
            global_vars.ball_ydir=-global_vars.ball_speed
        else:
            #if self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) not in ["twall","lwall","rwall","paddle"]:
           self.add_ball(global_vars.ball_xpos,global_vars.ball_ypos)

    # def add_game_stats(self,x,y):
    #     # (r,c)=self.board_dimension()
    #     self.add_to_board(2,3,str(global_vars.lives),"default")
    
    def print_board(self):
        (r,c)=self.board_dimension()
        str=''
        for row in range (r):
            for column in range (c):
                str+=self.printxy(row,column)
            str+="\n"
        print(str)
    
    def prepare_board(self):
        self.add_walls()
        self.add_bricks()
        self.add_paddle(global_vars.paddle_pos)
        self.add_ball(global_vars.ball_xpos,global_vars.ball_ypos)
        # self.add_game_stats(global_vars.ball_xpos,global_vars.ball_ypos)