import turtle as trtl
import keyboard

pnt = trtl.Turtle()

#----Constants----
FORWARD_KEY, LEFT_KEY, BACKWARD_KEY, RIGHT_KEY, USER_MOVEMENT, USER_TURN = 'w', 'a', 's', 'd', 15, 15   

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
wn = trtl.Screen()
wn.mainloop()


""" TODO:  
        -Make Tree & star (Aiden)
        -Snow w/ button (Caden)
        -Name w/ box 
        -Presents
        -Godly message
        -Key down events
        """
