# Not A Brick-Breaker
Classic brick breaker game playable in a terminal. The game is designed in basic python without the help of any external modules. 

## Features :
* 4 Different kinds of bricks : which breaks in 1 , 2 , 3 ,unbreakable hits respectively
* Bricks change colour on every hit to show updated strength
* ball-wall collision
* ball-paddle collision
* ball-brick collision
* Score and other game stats display
* Powerups : GrabBall,ThroughBall,ExpandPaddle,ShrinkPaddle,ShootPaddle
* Sound on collision with Paddle,Brick,Boss Enemy
* Sound on Start up and Quit
* Rainbow Bricks
* Falling Bricks
* 3 Levels
  
## Game Play:

### Running the game:
```
python3 main.py
```

### Playing the game:
* move paddle left  : a
* move paddle right : d
* Shoot Bullets     : space_bar
* quit game         : q

### Powerups Explained:
* E : Expands the paddle by 1 unit
* S : Shrinks the paddle by 1 unit
* G : Grabs the ball ,every time the ball hits the paddle
* T : Ball passes thorugh all the balls ,destroying them,irrespective of their strength
* ! : Paddle shoots bullets

## Game design:
The game is entirely modular for further updates .It follows a simplistic class-object-member approach for all the elements on screen. New features can be added by making a class for it and adding it to the game board ( ``` board_elements.py ``` )

### Following OOPs concepts are used:
* Encapsulation
* Abstraction
* Polymorphism
* Inheritance 