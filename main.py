import getInputs
import subprocess as sp
from parent_board import parent_board
import global_vars
import time
from board_elements import board_elements
if __name__== '__main__':
    
    sp.call('clear',shell=True)
    print("Not A Brick-Breaker")

    input_char=getInputs.NBInput()
    input_char.nbTerm()
    input_char.flush()
    input_char.orTerm()
    


    b=board_elements(global_vars.console_length,global_vars.console_breadth)
    b.prepare_board()
    while(1):
        
        sp.call('clear',shell=True)
        b.print_board()

        time.sleep(0.1)
























    #     a=parent_board(global_vars.console_length,global_vars.console_breadth)
    #     (r,c)=a.board_dimension()
    #     print(r,c)
    #     for row in range (0,r):
    #         a.add_to_board(row,0,"|","wall")
    #         for column in range (0,c):
    #             if(row==0):
    #                 a.add_to_board(row,column,"-","wall")
    #             elif(column!=0 & column!=c-1):
    #                 a.add_to_board(row,column," ","default")
    #         a.add_to_board(row,column,"|","wall")
        
    #     str=''
    #     for row in range (0,r):
    #         for column in range (0,c):
    #             str+=a.printxy(row,column)
    #         str+="\n"
    #     print(str)

    #    
    # #setting up the environment
    
        