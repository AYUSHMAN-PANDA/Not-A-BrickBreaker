import getInputs
import subprocess as sp
from parent_board import parent_board
import global_vars
import time
from board_elements import board_elements
import os
if __name__== '__main__':
    
    sp.call('clear',shell=True)
    print("Not A Brick-Breaker\n")
    global_vars.player=input("Player name: ")
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

    # fool_loop=1
    # while(fool_loop!=500):
    #     sp.call('clear',shell=True)
    #     print("Loading game ...")
    #     fool_loop+=1
    os.system('aplay -q ./start.wav&')
    while(1):
        
        t+=0.1
        sp.call('clear',shell=True)
        print("\t\t\t\t\tNot A Brick-Breaker\n")
        print('\x1b[1;31;40m')
        print("[Remaining Life:",global_vars.lives,"], \t[Score:",global_vars.score,"],\t[Player Name:",global_vars.player,"],\t[time spent=",int(t),"]Current Level:",global_vars.current_level)
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
                os.system('aplay -q ./gameover.wav&')
                print("quitters never win,",global_vars.player,"!_!")
                print("Your Score:",global_vars.score,"\nTime played:",int(t),"seconds")
                break
                
            if key_pressed=='s':#skip level
                global_vars.current_level+=1
                if global_vars.current_level==4:
                    global_vars.game_over=1
                sp.call('clear',shell=True)
                b.prepare_board()
               # b.print_board()
            
            if key_pressed=='f':#trigger falling bricks
                global_vars.falling_bricks=1
            
            if key_pressed==' ':#space bar for shooting paddle
                if global_vars.shoot_active==1:
                    global_vars.bullet_active=1
        
        if(global_vars.bullet_active==1):
            b.shoot()

                
            
        #randomly add powerups at random time
        b.expand_paddle_powerup()
        b.shrink_paddle_powerup()
        b.grab_ball_powerup()
        b.through_ball_powerup()
        b.shoot_paddle_powerup()

        if global_vars.ball_flag==1:
           b.ball_movement()

        if global_vars.game_over==1:
            #sp.call('clear',shell=True)
            os.system('aplay -q ./gameover.wav&')
            input_char.orTerm()
            print("Game o'vr ,",global_vars.player,"!")
            print("Your Score:",global_vars.score,"\nTime played:",int(t),"seconds")
            break

        if int(t) ==15:
            global_vars.fall_activate=1

        print('\x1b[1;31;40m')
        print("Enter q to quit")
        print('\x1b[1;36;40m')

        if global_vars.grabbed==1:
            print("Active powerup: Grab Ball")
        if global_vars.t_active==1:
            print("Active powerup: Through Ball")
        if global_vars.fall_activate==1:
            print("Active : Bricks Falling")
        if global_vars.shoot_active==1:
            print("Active : Paddle Shooting, Time remaining:",100-int((global_vars.shoot_duration/500)*100),"%")
            # print(global_vars.shoot_duration/500*100,"%")

        if global_vars.falling_bricks==1:
            b.fall_bricks()
            global_vars.falling_bricks=0
        
        # print(input_char.getCh())

        time.sleep(s)

        