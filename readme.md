# Not A Brick-Breaker
Classic brick breaker game playable in a terminal. The game is designed in basic python without the help of any external modules. 

## Features :
* 4 Different kinds of bricks : which breaks in 1 , 2 , 3 ,unbreakable hits respectively
* Bricks change colour on every hit to show updated strength
* ball-wall collision
* ball-paddle collision
* ball-brick collision
* Score and other game stats display
* Powerups : GrabBall,ThroughBall,ExpandPaddle,ShrinkPaddle
  
## Game Play:
```
python3 main.py
```
* move paddle left  : a
* move paddle right : d
* quit game         : q

## Game design:
The game is entirely modular for further updates .It follows a simplistic class-object-member approach for all the elements on screen. New features can be added by making a class for it and adding it to the game board ( ``` board_elements.py ``` )
### Following OOPs concepts are used:
* Encapsulation
* Abstraction
* Polymorphism
* Inheritance 