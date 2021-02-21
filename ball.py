import global_vars

class ball():
    def __init__(self,board):
        self.b=board

    def ball_bricks(self):
        if self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) not in ["twall","lwall","rwall","paddle"]:
            if global_vars.t_active==1:
                if "brick" in self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos):
                    self.b.add_to_board(global_vars.ball_xpos,global_vars.ball_ypos," ","default")
                elif "ball" in self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos):
                    self.b.add_to_board(global_vars.ball_xpos,global_vars.ball_ypos," ","default")
            else:
                if self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) == "brick1":
                    self.b.add_to_board(global_vars.ball_xpos,global_vars.ball_ypos," ","default")
                elif self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) == "brick2":
                    self.b.add_to_board(global_vars.ball_xpos,global_vars.ball_ypos,"B","brick1")
                elif self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) == "brick3":
                    self.b.add_to_board(global_vars.ball_xpos,global_vars.ball_ypos,"B","brick2")
                elif self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) == "brick4":
                    a="do nothing..lol"
                else:
                    self.b.add_to_board(global_vars.ball_xpos,global_vars.ball_ypos," ","default")
                
    def  ball_score(self):
        if "brick" in self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos):
            global_vars.score+=5

    def update_ball_pos(self):
        global_vars.ball_xpos+=global_vars.ball_xdir
        global_vars.ball_ypos+=global_vars.ball_ydir
    
    def add_ball_updated_pos(self):
        if global_vars.grabbed==0:    
            if self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) not in ["paddle","twall","lwall","rwall","brick1","brick2","brick3","brick4"]:
                self.b.add_ball(global_vars.ball_xpos,global_vars.ball_ypos)
        else:
            if self.b.get_element_type(global_vars.ball_xpos,global_vars.ball_ypos) not in ["twall","lwall","rwall","brick1","brick2","brick3","brick4"]:
                self.b.add_ball(global_vars.ball_xpos,global_vars.ball_ypos)

    def ball_collision(self,type):
        if type=="twall":
            global_vars.ball_xdir=global_vars.ball_speed
            if global_vars.ball_ypos>global_vars.ball_ypos-global_vars.ball_ydir:
                global_vars.ball_ydir=global_vars.ball_speed
            else:
                global_vars.ball_ydir=-global_vars.ball_speed
        elif type=="lwall":
            global_vars.ball_ydir=global_vars.ball_speed
            if global_vars.ball_xpos>global_vars.ball_xpos-global_vars.ball_xdir:
                global_vars.ball_xdir=global_vars.ball_speed
            else:
                global_vars.ball_xdir=-global_vars.ball_speed
        elif type=="rwall":
            global_vars.ball_ydir=-global_vars.ball_speed
            if global_vars.ball_xpos>global_vars.ball_xpos-global_vars.ball_xdir:
                global_vars.ball_xdir=global_vars.ball_speed
            else:
                global_vars.ball_xdir=-global_vars.ball_speed
        elif type=="brick":
            if global_vars.t_active!=1:
                if global_vars.ball_ypos>global_vars.ball_ypos-global_vars.ball_ydir:
                    global_vars.ball_ydir=-global_vars.ball_speed
                else:
                    global_vars.ball_ydir=global_vars.ball_speed
                if global_vars.ball_xpos>global_vars.ball_xpos-global_vars.ball_xdir:
                    global_vars.ball_xdir=global_vars.ball_speed
                else:
                    global_vars.ball_xdir=-global_vars.ball_speed
        elif type=="bwall":
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
            self.b.add_paddle(global_vars.paddle_pos)
            self.b.add_ball(global_vars.ball_xpos,global_vars.ball_ypos)
        elif type=="paddle":
            if global_vars.grabbed==1:
                global_vars.ball_flag=0
                global_vars.ball_xpos
            global_vars.ball_xdir+=10
            global_vars.ball_xdir=-global_vars.ball_speed
            if global_vars.ball_ypos>global_vars.ball_ypos-global_vars.ball_ydir:
                global_vars.ball_ydir=global_vars.ball_speed
            else:
                global_vars.ball_ydir=-global_vars.ball_speed
