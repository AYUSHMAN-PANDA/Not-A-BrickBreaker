from parent_board import parent_board
import global_vars
import random
from bricks import add_a_brick
from bricks import dont_add_rainbow_brick
from ball import ball
import os

class board_elements(parent_board):

    def __init__(self,rows,columns):
        super().__init__(rows,columns)

    def add_bricks(self):
        bricks_height=random.randint(10,12)
        bricks_width=random.randint(global_vars.console_breadth-20,global_vars.console_breadth-10)
        xpos=5
        ypos=5
        if global_vars.current_level==1:
            for x in range (bricks_height):
                for y in range (bricks_width):
                    if x%2==0 and y%11==0:
                        self.add_to_board(xpos+x,ypos+y,"B",add_a_brick())
        elif global_vars.current_level==2:
            for x in range (bricks_height):
                for y in range (bricks_width):
                    if y%17==0:
                        self.add_to_board(xpos+x,ypos+y,"B",add_a_brick())

        elif global_vars.current_level==3:
            for x in range (bricks_height):
                for y in range (bricks_width):
                    if y%23==0:
                        self.add_to_board(xpos+x,ypos+y,"B",add_a_brick())

    def fall_bricks(self):
        (r,c)=self.board_dimension()
        dumb=999
        for row in range (r):
            if row==dumb:
                continue
            for column in range (c):    
                    typ=self.get_element_type(row,column)
                    if "brick" in typ:
                        dumb=row+1
                        if dumb+2==global_vars.console_length:
                            global_vars.game_over=1
                            return
                        self.delete_from_board(row,column)
                        self.add_to_board(row+1,column,"B",typ)
                        



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
            if global_vars.shoot_active==1:
               self.add_to_board(r-2,c,"^","paddle")
            else: 
                self.add_to_board(r-2,c,"=","paddle")

    def add_ball(self,x,y):
            self.add_to_board(x,y,"*","ball")
    
    def expand_paddle_powerup(self):
        if global_vars.p_exp==1:
            global_vars.pt+=1
            if global_vars.pt%4==0:
                self.add_to_board(global_vars.px,global_vars.py," ","default")
                global_vars.px+=1
                if self.get_element_type(global_vars.px,global_vars.py) == "bwall":
                    global_vars.p_exp=0
                    global_vars.px=2
                    global_vars.py=52
                    global_vars.pt=0
                    return
                elif self.get_element_type(global_vars.px,global_vars.py) == "paddle":
                    os.system('aplay -q ./powerup.wav&')
                    global_vars.p_exp=0
                    global_vars.px=2
                    global_vars.py=52
                    global_vars.pt=0
                    global_vars.paddle_length+=1
                    self.add_paddle(global_vars.paddle_pos)
                    return
                else: 
                    self.add_to_board(global_vars.px,global_vars.py,"E","expand paddle")
                    return
        prob=random.randint(1,100)
        if prob==7:
            global_vars.p_exp=1
            self.add_to_board(global_vars.px,global_vars.py,"E","expand paddle")
    
    def shrink_paddle_powerup(self):
        if global_vars.p_sh==1:
            global_vars.st+=1
            if global_vars.st%4==0:
                self.add_to_board(global_vars.sx,global_vars.sy," ","default")
                global_vars.sx+=1
                if self.get_element_type(global_vars.sx,global_vars.sy) == "bwall":
                    global_vars.p_sh=0
                    global_vars.sx=2
                    global_vars.sy=45
                    global_vars.st=0
                    return
                elif self.get_element_type(global_vars.sx,global_vars.sy) == "paddle":
                    os.system('aplay -q ./powerup.wav&')
                    global_vars.p_sh=0
                    global_vars.sx=2
                    global_vars.sy=45
                    global_vars.st=0
                    if global_vars.paddle_length-1 > 3:
                        global_vars.paddle_length-=1
                    self.add_paddle(global_vars.paddle_pos)
                    return
                else: 
                    self.add_to_board(global_vars.sx,global_vars.sy,"S","shrink paddle")
                    return
        prob=random.randint(1,100)
        if prob==7:
            global_vars.p_sh=1
            self.add_to_board(global_vars.sx,global_vars.sy,"S","shrink paddle")

    def grab_ball_powerup(self):
        global_vars.duration+=1
        if global_vars.duration == 500:
            global_vars.duration=0
            global_vars.grabbed=0
            return  
        if global_vars.grab==1:
            global_vars.gt+=1
            if global_vars.gt%4==0:
                self.add_to_board(global_vars.gx,global_vars.gy," ","default")
                global_vars.gx+=1
                if self.get_element_type(global_vars.gx,global_vars.gy) == "bwall":
                    global_vars.grab=0
                    global_vars.gx=2
                    global_vars.gy=17
                    global_vars.gt=0
                    return
                elif self.get_element_type(global_vars.gx,global_vars.gy) == "paddle":
                    os.system('aplay -q ./powerup.wav&')
                    global_vars.grab=0
                    global_vars.gx=2
                    global_vars.gy=17
                    global_vars.gt=0
                    global_vars.grabbed=1
                    return
                else: 
                    self.add_to_board(global_vars.gx,global_vars.gy,"G","grab ball")
                    return
        prob=random.randint(1,100)
        if prob==7:
            global_vars.grab=1
            self.add_to_board(global_vars.gx,global_vars.gy,"G","grab ball")
    
    def through_ball_powerup(self):
        global_vars.t_duration+=1
        if global_vars.t_duration == 500:
            global_vars.t_duration=0
            global_vars.t_active=0
            return  
        if global_vars.through==1:
            global_vars.tt+=1
            if global_vars.tt%4==0:
                self.add_to_board(global_vars.tx,global_vars.ty," ","default")
                global_vars.tx+=1
                if self.get_element_type(global_vars.tx,global_vars.ty) == "bwall":
                    global_vars.through=0
                    global_vars.tx=2
                    global_vars.ty=10
                    global_vars.tt=0
                    return
                elif self.get_element_type(global_vars.tx,global_vars.ty) == "paddle":
                    os.system('aplay -q ./powerup.wav&')
                    global_vars.through=0
                    global_vars.tx=2
                    global_vars.ty=10
                    global_vars.tt=0
                    global_vars.t_active=1
                    return
                else: 
                    self.add_to_board(global_vars.tx,global_vars.ty,"T","through ball")
                    return
        prob=random.randint(1,100)
        if prob==7:
            global_vars.through=1
            self.add_to_board(global_vars.tx,global_vars.ty,"T","through ball")

    def shoot_paddle_powerup(self):
        global_vars.shoot_duration+=1
        if global_vars.shoot_duration == 500:
            global_vars.shoot_duration=0
            global_vars.shoot_active=0
            self.add_paddle(global_vars.paddle_pos)
            return  
        if global_vars.shoot==1:
            global_vars.shoot_t+=1
            if global_vars.shoot_t%4==0:
                self.add_to_board(global_vars.shoot_x,global_vars.shoot_y," ","default")
                global_vars.shoot_x+=1
                if self.get_element_type(global_vars.shoot_x,global_vars.shoot_y) == "bwall":
                    global_vars.shoot=0
                    global_vars.shoot_x=2
                    global_vars.shoot_y=63
                    global_vars.shoot_t=0
                    return
                elif self.get_element_type(global_vars.shoot_x,global_vars.shoot_y) == "paddle":
                    os.system('aplay -q ./powerup.wav&')
                    global_vars.shoot=0
                    global_vars.shoot_x=2
                    global_vars.shoot_y=63
                    global_vars.shoot_t=0
                    global_vars.shoot_active=1
                    self.add_paddle(global_vars.paddle_pos)
                    return
                else: 
                    self.add_to_board(global_vars.shoot_x,global_vars.shoot_y,"!","Shoot paddle")
                    return
        prob=random.randint(1,100)
        if prob==7:
            global_vars.shoot=1
            self.add_to_board(global_vars.shoot_x,global_vars.shoot_y,"!","Shoot Paddle")

    def shoot(self):
        if global_vars.set_shoot_pos==0:
            global_vars.set_shoot_pos=1
            global_vars.bullet_x=global_vars.console_length-3
            global_vars.bullet_y1=global_vars.paddle_pos
            global_vars.bullet_y2=global_vars.paddle_pos+global_vars.paddle_length-1
        self.add_to_board(global_vars.bullet_x,global_vars.bullet_y1,"|","Bullet")
        self.add_to_board(global_vars.bullet_x,global_vars.bullet_y2,"|","Bullet")
        self.add_to_board(global_vars.bullet_x,global_vars.bullet_y1," ","default")
        self.add_to_board(global_vars.bullet_x,global_vars.bullet_y2," ","default")
        global_vars.bullet_x-=1
        self.add_to_board(global_vars.bullet_x,global_vars.bullet_y1,"|","Bullet")
        self.add_to_board(global_vars.bullet_x,global_vars.bullet_y2,"|","Bullet")
        if global_vars.bullet_x==1:
            self.add_to_board(global_vars.bullet_x,global_vars.bullet_y1," ","default")
            self.add_to_board(global_vars.bullet_x,global_vars.bullet_y2," ","default")
            global_vars.bullet_x=global_vars.console_length-3
            global_vars.bullet_active=0
            global_vars.set_shoot_pos=0


    def ball_movement(self):

        ball_class=ball(self)
        
        ball_class.ball_bricks()
        ball_class.update_ball_pos()
        ball_class.ball_score()
    
            
        if self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='twall':
            ball_class.ball_collision("twall")
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='lwall':
            ball_class.ball_collision("lwall")
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='rwall':
            ball_class.ball_collision("rwall")
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) in ["brick1","brick2","brick3","brick4"]:
            ball_class.ball_collision("brick")
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=="brick5":
            self.add_to_board(global_vars.ball_xpos,global_vars.ball_ypos,"B",dont_add_rainbow_brick())
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='bwall':
            ball_class.ball_collision("bwall")
        elif self.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos)=='paddle':
            ball_class.ball_collision("paddle")

        ball_class.add_ball_updated_pos()
    
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