player="Lucifer"
score= 0
lives=3
console_length=40
console_breadth=100
paddle_pos=50   
paddle_length=11

ball_xpos=console_length-3
ball_ypos=55
ball_xdir=1
ball_ydir=-1
ball_flag=0
ball_speed=1

degub=1 #not used so much so far

#powerup flags:

#paddle expand - E
p_exp=0
px=2
py=52
pt=0

#paddle shrirnk - S
p_sh=0
sx=2
sy=45
st=0

#grab ball - G
grab=0
gx=2
gy=18
gt=0
grabbed=0
duration=0 #in terms of frames

#through ball - T
through=0
tx=2
ty=10
tt=0
t_active=0
t_duration=0 #in terms of frames

#falling bricks
fall_activate=0
falling_bricks=0

#shoot paddle - !
shoot=0
shoot_active=0
shoot_x=2
shoot_y=63
shoot_duration=0
shoot_t=0

# bullet_t=0
bullet_x=console_length-3
bullet_y1=paddle_pos
bullet_y2=paddle_pos+paddle_length-1
bullet_active=0
set_shoot_pos=0

#game - level
current_level=1 #can be 1, 2 or 3[boss_level]

game_over=0
