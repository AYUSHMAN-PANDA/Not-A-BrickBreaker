from parent_board import parent_board
import global_vars
import random

class board_elements(parent_board):

    def __init__(self,rows,columns):
        super().__init__(rows,columns)

    def add_bricks(self):
        bricks_height=random.randint(10,20)
        bricks_width=random.randint(global_vars.console_breadth-20,global_vars.console_breadth-10)
        xpos=5
        ypos=10
        for x in range (bricks_height):
            for y in range (bricks_width):
                if y%7==0:
                    self.add_to_board(xpos+x,ypos+y,"B","brick")

    def add_walls(self):
        (r,c)=self.board_dimension()
        if global_vars.degub==1:
            print(r,c)

        for row in range (r):
            self.add_to_board(row,0,"|","wall")
            for column in range (c):
                if row==0:
                    self.add_to_board(row,column,"-","wall")
                elif(column!=0 & column!=c-1):
                    self.add_to_board(row,column," ","default")
            self.add_to_board(row,column,"|","wall")
    
    def add_paddle(self,x):
        y=x+global_vars.paddle_length
        (r,c)=self.board_dimension()
        if(x>c or y>c):
            return
        for c in range (1,c):
            self.add_to_board(r-1,c," ","default")
        for c in range (x,y):
            self.add_to_board(r-1,c,"~","paddle")

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