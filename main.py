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
    flag=0
    s=0.05
    t=0
    while(1):
        
        t+=0.1
        sp.call('clear',shell=True)
        print("[Remaining Life:",global_vars.lives,"], \t[Score:",global_vars.score,"],\t[Player Name:",global_vars.player,"],\t[time spent=",int(t),"]")
        b.print_board()

        if input_char.kbHit():

            key_pressed=input_char.getCh()

            if key_pressed=='d':
                if global_vars.paddle_pos+2+global_vars.paddle_length < global_vars.console_breadth:
                    global_vars.paddle_pos+=2
                else:
                    global_vars.paddle_pos=global_vars.console_breadth-global_vars.paddle_length-1
                b.add_paddle(global_vars.paddle_pos)
                global_vars.ball_flag=1
            
            if key_pressed=='a':
                if global_vars.paddle_pos-2 > 0:
                    global_vars.paddle_pos-=2
                else:
                    global_vars.paddle_pos=1
                b.add_paddle(global_vars.paddle_pos)
                global_vars.ball_flag=1

            # if key_pressed=='e':
            #     global_vars.paddle_length+=1
            #     b.add_paddle(global_vars.paddle_pos)
            
            # if key_pressed=='s':
            #     global_vars.paddle_length-=1
            #     b.add_paddle(global_vars.paddle_pos)
            
            if key_pressed=='q':
                input_char.orTerm()
                print("quitters never win,",global_vars.player,"!_!")
                print("Your Score:",global_vars.score,"\nTime played:",int(t),"seconds")
                break
        
        #randomly add powerups at random time
        b.expand_paddle_powerup()
        b.shrink_paddle_powerup()
        b.grab_ball_powerup()
        b.through_ball_powerup()

        if global_vars.ball_flag==1:
           b.ball_movement()

        if global_vars.game_over==1:
            #sp.call('clear',shell=True)
            input_char.orTerm()
            print("Game o'vr ,",global_vars.player,"!")
            print("Your Score:",global_vars.score,"\nTime played:",int(t),"seconds")
            break

        if global_vars.grabbed==1:
            print("Active powerup: Grab Ball")
        if global_vars.t_active==1:
            print("Active powerup: Through Ball")

        time.sleep(s)

        