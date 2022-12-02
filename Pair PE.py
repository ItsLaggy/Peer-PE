import turtle as trtl
import keyboard

pnt = trtl.Turtle()
wn = trtl.Screen()

backGround = open('Snow+Desktop+Wallpapers+and+Backgrounds+1.png', 'r')
wn.bgpic(backGround)

#----Constants----
FORWARD_KEY, LEFT_KEY, BACKWARD_KEY, RIGHT_KEY = 'w', 'a', 's', 'd'  
USER_MOVEMENT, USER_TURN = 15, 15 

#----Functions----
def Forward_KeyDown(event):
    pnt.penup()
    pnt.forward(USER_MOVEMENT)
def Backward_KeyDown(event):
    pnt.penup()
    pnt.back(USER_MOVEMENT)
def Left_KeyDown(event):
    pnt.penup()
    pnt.left(USER_TURN)
def Right_KeyDown(event):
    pnt.penup()
    pnt.right(USER_TURN)
    
#----Keydown Movement----
keyboard.on_press_key(FORWARD_KEY, Forward_KeyDown)
keyboard.on_press_key(BACKWARD_KEY, Backward_KeyDown)
keyboard.on_press_key(LEFT_KEY, Left_KeyDown)
keyboard.on_press_key(RIGHT_KEY, Right_KeyDown)

#----Window Control----
wn.mainloop()


""" TODO:  
        -Make Tree & star (Aiden)
        -Snow w/ button (Caden)
        -Name w/ box 
        -Presents
        -Godly message
        X-Key down events(Caden-X
        -Background (Caden)
    
    Credit:
        -https://imgs.search.brave.com/d4QyAFytVCoj-nVQSR6nq4k85BTYOFE0AJY4g93Qt7k/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly8xLmJw/LmJsb2dzcG90LmNv/bS8tR05neFRoV2Jt/cE0vVUk2akt6X0FQ/eEkvQUFBQUFBQUFN/aXMvZjVobV9QOWhH/UWsvczE2MDAvU25v/dytEZXNrdG9wK1dh/bGxwYXBlcnMrYW5k/K0JhY2tncm91bmRz/KzEuanBn

        """
