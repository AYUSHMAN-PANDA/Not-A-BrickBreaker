import numpy as np
from colours import colour_this

class parent_board():

    def __init__(self,rows,columns):
        #inits the board with length,width and board matrix
        self._rows= rows
        self._columns= columns
        self._board= np.full((self._rows,self._columns,2),' '*10)

    def board_dimension(self):
        return (self._rows,self._columns)

    def add_to_board(self,x,y,character,element_type):
        self._board[x][y][0]= character
        self._board[x][y][1]= element_type

    def delete_from_board(self,x,y):
        self._board[x][y][0]=" "
        self._board[x][y][1]="default"

    def get_element_type(self,x,y):
        if self._board[x][y][1] in ["default"]: #looped to add different element types which shouldnt be seen as obstacle 
            return "default"
        else:
            return self._board[x][y][1] #some or other kind of article

    def printxy(self,x,y):
        return (colour_this(self._board[x][y][0],self._board[x][y][1])) #add colours according to type: _board[x][y][1] 


