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
    
    


    b=board_elements(global_vars.console_length,global_vars.console_breadth)
    b.prepare_board()
    x=5
    y=10
    while(1):
        
        sp.call('clear',shell=True)
        b.print_board()

        if input_char.kbHit():

            key_pressed=input_char.getCh()

            if key_pressed=='d':
                if global_vars.paddle_pos+2+global_vars.paddle_length < global_vars.console_breadth:
                    global_vars.paddle_pos+=2
                else:
                    global_vars.paddle_pos=global_vars.console_breadth-global_vars.paddle_length
                b.add_paddle(global_vars.paddle_pos)
            
            if key_pressed=='a':
                if global_vars.paddle_pos-2 > 0:
                    global_vars.paddle_pos-=2
                else:
                    global_vars.paddle_pos=1
                b.add_paddle(global_vars.paddle_pos)
            
            if key_pressed=='t':
                global_vars.paddle_length+=1
                b.add_paddle(global_vars.paddle_pos)
                
            
            if key_pressed=='q':
                print("quitters never win :(")
                input_char.orTerm()
                break

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
    
        