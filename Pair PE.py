import turtle as trtl
import keyboard

pnt = trtl.Turtle()

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
wn = trtl.Screen()
wn.bgpic('./Snow.gif')
wn.mainloop()

""" TODO:  
        -Make Tree & star (Aiden)
        -Snow w/ button (Caden)
        -Name w/ box 
        -Presents
        -Godly message
        X-Key down events(Caden)-X
        X-Background (Caden)-X
    
    Credit:
        -Snow (Background)-https://imgs.search.brave.com/d4QyAFytVCoj-nVQSR6nq4k85BTYOFE0AJY4g93Qt7k/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly8xLmJw/LmJsb2dzcG90LmNv/bS8tR05neFRoV2Jt/cE0vVUk2akt6X0FQ/eEkvQUFBQUFBQUFN/aXMvZjVobV9QOWhH/UWsvczE2MDAvU25v/dytEZXNrdG9wK1dh/bGxwYXBlcnMrYW5k/K0JhY2tncm91bmRz/KzEuanBn

        """





'''
import turtle as trtl

pnt = trtl.Turtle()

pnt.speed(0)
#---- leaves of the tree size ----

First_leaves = 200
Second_leaves = 180
Third_leaves = 160
Fourth_leaves = 140

#---- base of the tree vaule( bottom center of the canvas ) ----

center_x= 0
cenetr_y= -300

first_triangle_x = -110
second_triangle_x = -100
third_triangle_x = -90
fourth_triangle_x = -80

first_triangle_y = -272
second_triangle_y = -190
third_triangle_y = - 100
fourth_triangle_y = -20

#---- tree colors ----
background_color = "blue"
tree_color = "green"
trunk_color = "brown"

#---- creates the tree trunk and trasports the turtle to the bottom center of the canvas ----

pnt.penup()
pnt.goto(center_x,cenetr_y)
pnt.pendown()
pnt.left(45)
pnt.fillcolor(trunk_color)
pnt.begin_fill()
pnt.circle(20,360,4)
pnt.end_fill()

#---- triangle function ----

def make_triangle():
    pnt.begin_fill()
    pnt.fillcolor(tree_color)
    pnt.right(45)
    pnt.forward(200)
    pnt.right(240)
    pnt.forward(200)
    pnt.right(240)
    pnt.forward(200)
    pnt.end_fill()

#---- lines up tree leaves

pnt.penup()
pnt.goto(first_triangle_x,first_triangle_y)
pnt.pendown()

#---- make tree leaves ----

def tree_leaves():
    pnt.begin_fill()
    pnt.fillcolor(tree_color)
    pnt.right(45)
    pnt.forward(First_leaves)
    pnt.right(240)
    pnt.forward(First_leaves)
    pnt.right(240)
    pnt.forward(First_leaves)
    pnt.end_fill()

    pnt.penup()
    pnt.left(120)
    pnt.goto(second_triangle_x,second_triangle_y)
    pnt.pendown()

    pnt.begin_fill()
    pnt.fillcolor(tree_color)
    pnt.forward(Second_leaves)
    pnt.right(240)
    pnt.forward(Second_leaves)
    pnt.right(240)
    pnt.forward(Second_leaves)
    pnt.end_fill()
    
    pnt.penup()
    pnt.left(120)
    pnt.goto(third_triangle_x,third_triangle_y)
    pnt.pendown()

    pnt.begin_fill()
    pnt.fillcolor(tree_color)
    pnt.forward(Third_leaves)
    pnt.right(240)
    pnt.forward(Third_leaves)
    pnt.right(240)
    pnt.forward(Third_leaves)
    pnt.end_fill()

    pnt.penup()
    pnt.left(120)
    pnt.goto(fourth_triangle_x,fourth_triangle_y)
    pnt.pendown()

    pnt.begin_fill()
    pnt.fillcolor(tree_color)
    pnt.forward(Fourth_leaves)
    pnt.right(240)
    pnt.forward(Fourth_leaves)
    pnt.right(240)
    pnt.forward(Fourth_leaves)
    pnt.end_fill()

#---- makes star for the tree ----

def make_star():
    pnt.penup()
    pnt.goto(center_x+4 ,95)
    pnt.pendown()
    pnt.color("yellow")
    pnt.begin_fill()
    pnt.right(95)
    pnt.forward(45)
    for i in range(4):
        pnt.right(144)
        pnt.forward(45)
    pnt.end_fill()
    pnt.penup()

#---- creates the background ----








#---- prints the code ----

tree_leaves()
make_star()







'''
