#Aiden paste ur code here so i can integrate it
import turtle as trtl
import random
pnt = trtl.Turtle()
wn = trtl.Screen()



CENTER_X, CENTER_Y, TRIANGLE_TURN = 0, -300, 240
FIRST_TRIANGLE_X, FIRST_TRIANGLE_Y = -110, -272
SECOND_TRIANGLE_X, SECOND_TRIANGLE_Y = -100, -190
THIRD_TRIANGLE_X, THIRD_TRIANGLE_Y = -90, -100
FOURTH_TRIANGLE_X, FOURTH_TRIANGLE_Y = -80, -20
FIRST_LEAVES, SECOND_LEAVES, THIRD_LEAVES, FOUTH_LEAVES  = 200, 180, 160, 140
TREE_COLOR, TRUNK_COLOR, STAR_COLOR, OUT_LINE_PRESENT = "green","brown", "yellow","blue"

ORNA_RADIUS = 10
ORNA_COLORS=['blue','red','pink','purple','orange']
PRESENT_COLORS=['green','pink','purple','orange']
FIRST_DECORATION_X, FIRST_DECORATION_Y = 0, -210
SECOND_DECORATION_X, SECOND_DECORATION_Y = 0, 35
THIRD_DECORATION_X, THIRD_DECORATION_Y = -50, 0
FOURTH_DECORATION_X, FOURTH_DECORATION_Y = -60, -250
FIFTH_DECORATION_X, FIFTH_DECORATION_Y = -60, -80
SIXTH_DECORATION_X, SIXTH_DECORATION_Y = 0, -60
SEVENTH_DECORATION_X, SEVENTH_DECORATION_Y = -55, -155
EIGHTH__DECORATION_X, EIGHTH_DECORATION_Y = 0, -140
LEFT_PRESENT = -75,-300
RIGHT_PRESENT = 80, -300
PRESENT_RADIUS = 15
RIGHT_PRESENT_CENTER = 70, -300
LEFT_PRESENT_CENTER = -85, -300
RIGHT_PRESENT_CENTER_HORZ = 60, -290
LEFT_PRESENT_CENTER_HORZ = -95, -290
WRAPING_PAPER_LENGTH = 20

#---- ordament function ----
def MAKE_ORNA():
    pnt.penup()
    pnt.goto(FIRST_DECORATION_X, FIRST_DECORATION_Y)
    pnt.pendown()
    pnt.fillcolor(random.choice(ORNA_COLORS))
    pnt.begin_fill()
    pnt.circle(ORNA_RADIUS)
    pnt.end_fill()

    pnt.penup()
    pnt.goto(SECOND_DECORATION_X, SECOND_DECORATION_Y)
    pnt.pendown()
    pnt.fillcolor(random.choice(ORNA_COLORS))
    pnt.begin_fill()
    pnt.circle(ORNA_RADIUS)
    pnt.end_fill()

    pnt.penup()
    pnt.goto(THIRD_DECORATION_X, THIRD_DECORATION_Y)
    pnt.pendown()
    pnt.fillcolor(random.choice(ORNA_COLORS))
    pnt.begin_fill()
    pnt.circle(ORNA_RADIUS)
    pnt.end_fill()

    pnt.penup()
    pnt.goto(FOURTH_DECORATION_X, FOURTH_DECORATION_Y)
    pnt.pendown()
    pnt.fillcolor(random.choice(ORNA_COLORS))
    pnt.begin_fill()
    pnt.circle(ORNA_RADIUS)
    pnt.end_fill()
    
    pnt.penup()
    pnt.goto(FIFTH_DECORATION_X, FIFTH_DECORATION_Y)
    pnt.pendown()
    pnt.fillcolor(random.choice(ORNA_COLORS))
    pnt.begin_fill()
    pnt.circle(ORNA_RADIUS)
    pnt.end_fill()

    pnt.penup()
    pnt.goto(SIXTH_DECORATION_X, SIXTH_DECORATION_Y )
    pnt.pendown()
    pnt.fillcolor(random.choice(ORNA_COLORS))
    pnt.begin_fill()
    pnt.circle(ORNA_RADIUS)
    pnt.end_fill()
    
    pnt.penup()
    pnt.goto(SEVENTH_DECORATION_X, SEVENTH_DECORATION_Y )
    pnt.pendown()
    pnt.fillcolor(random.choice(ORNA_COLORS))
    pnt.begin_fill()
    pnt.circle(ORNA_RADIUS)
    pnt.end_fill()

    pnt.penup()
    pnt.goto(EIGHTH__DECORATION_X, EIGHTH_DECORATION_Y )
    pnt.pendown()
    pnt.fillcolor(random.choice(ORNA_COLORS))
    pnt.begin_fill()
    pnt.circle(ORNA_RADIUS)
    pnt.end_fill()
#---- present function ----
def MAKE_GIFTS():
    pnt.penup()
    pnt.goto(LEFT_PRESENT)
    pnt.pendown()
    pnt.left(115)
    pnt.color(OUT_LINE_PRESENT)
    pnt.fillcolor(random.choice(PRESENT_COLORS))
    pnt.begin_fill()
    pnt.circle(PRESENT_RADIUS,360,4)
    pnt.end_fill()
    
    pnt.penup()
    pnt.goto(RIGHT_PRESENT)
    pnt.pendown()
    pnt.fillcolor(random.choice(PRESENT_COLORS))
    pnt.begin_fill()
    pnt.circle(PRESENT_RADIUS,360,4)
    pnt.end_fill()

    pnt.penup()
    pnt.goto(RIGHT_PRESENT_CENTER)
    pnt.pendown()
    pnt.pensize(2)
    pnt.left(45)
    pnt.forward(WRAPING_PAPER_LENGTH)

    pnt.penup()
    pnt.goto(LEFT_PRESENT_CENTER)
    pnt.pendown()
    pnt.pensize(2)
    pnt.forward(WRAPING_PAPER_LENGTH)

    pnt.penup()
    pnt.goto(RIGHT_PRESENT_CENTER_HORZ)
    pnt.right(135)
    pnt.pendown()
    pnt.pensize(2)
    pnt.left(45)
    pnt.forward(WRAPING_PAPER_LENGTH)

    pnt.penup()
    pnt.goto(LEFT_PRESENT_CENTER_HORZ)
    pnt.pendown()
    pnt.pensize(2)
    pnt.forward(WRAPING_PAPER_LENGTH)
#---- tree trunk function ----
def Make_Tree_Trunk():
    pnt.speed(0)
    pnt.penup()
    pnt.goto(CENTER_X,CENTER_Y)
    pnt.pendown()
    pnt.left(45)
    pnt.fillcolor(TRUNK_COLOR)
    pnt.begin_fill()
    pnt.circle(20,360,4)
    pnt.end_fill()
#---- triangle function ----
def Make_Triangle(leaf_length):
    pnt.speed(0)
    pnt.begin_fill(),pnt.fillcolor(TREE_COLOR)
    pnt.pendown()
    pnt.left(240)
    for i in range(3):
        pnt.right(TRIANGLE_TURN)
        pnt.forward(leaf_length)
    pnt.end_fill()
#---- lines up tree leaves
def Turtle_Position(turtle_x, turtle_y):
    pnt.speed(0)
    pnt.penup()
    pnt.goto(turtle_x,turtle_y)
    pnt.pendown()
    pnt.setheading(0)
#---- make tree leaves ----
def Tree_Leaves():
    Turtle_Position(FIRST_TRIANGLE_X,FIRST_TRIANGLE_Y)
    Make_Triangle(FIRST_LEAVES)
    Turtle_Position(SECOND_TRIANGLE_X,SECOND_TRIANGLE_Y)
    Make_Triangle(SECOND_LEAVES)
    Turtle_Position(THIRD_TRIANGLE_X,THIRD_TRIANGLE_Y)
    Make_Triangle(THIRD_LEAVES)
    Turtle_Position(FOURTH_TRIANGLE_X,FOURTH_TRIANGLE_Y)
    Make_Triangle(FOUTH_LEAVES)
#---- makes star for the tree ----
def Make_Star():
    pnt.speed(0)
    pnt.penup()
    pnt.goto(CENTER_X+5 ,90)
    pnt.pendown()
    pnt.color(STAR_COLOR)
    pnt.begin_fill()
    pnt.right(95)
    pnt.forward(45)
    for i in range(4):
        pnt.right(144)
        pnt.forward(45)
    pnt.penup()
    pnt.end_fill()
#                       ===Tree Mother Function===
def Tree_Creation():
    Make_Tree_Trunk()
    Tree_Leaves()
    Make_Star()
    MAKE_ORNA()
    MAKE_GIFTS()




Tree_Creation()






pnt.hideturtle()

wn.mainloop()


# start_monitoring.py
import tkinter as tk
import fishtank as tank
my_tank = tank.FishTank()
my_tank.mainloop()
#---- the one above is in a seperate file thing idk if that effects it ----
def monitor():
  try:
    
    val1 = 17
    val2 = 12

    alkilines = list(range(val1, val2+1))

    current = get_alkalinity()
    mesg = "Alkalinity OK"

    if (current < alkilines[0]):
      mesg = "Alkalinity too low!"
    elif (current > alkilines[5]):
      mesg = "Alkalinity too high!"
    
  except:
    print("Unexpected error") 
    
  return mesg

# Function to simulate actual fish tank monitoring
def get_alkalinity():
  return 9
