import turtle as trtl
import keyboard
import random
import time

#----Turtle and Window Settings----
pnt = trtl.Turtle()
wn = trtl.Screen()
wn.title('You Received A Christmas Card!')
wn.tracer(0,0)

#----Constants----
#           ___Key Constants___
FORWARD_KEY, LEFT_KEY, BACKWARD_KEY, RIGHT_KEY = 'w', 'a', 's', 'd'  
USER_MOVEMENT, USER_TURN, USER_COLOR= 30, 30, 'red'
STAMP_TIMER = 30
#           ___Snow Constants___
FLAKE_AMOUNT,  REFRESH_TIMER = 300, 20
X_MIN, X_MAX, Y_MIN, Y_MAX = -400, 400, -350, 400
YMIN_END, YMAX_END = -350, -400
#           ___Tree Constants__
CENTER_X, CENTER_Y, TRIANGLE_TURN = 0, -300, 240
FIRST_TRIANGLE_X, FIRST_TRIANGLE_Y = -110, -272
SECOND_TRIANGLE_X, SECOND_TRIANGLE_Y = -100, -190
THIRD_TRIANGLE_X, THIRD_TRIANGLE_Y = -90, -100
FOURTH_TRIANGLE_X, FOURTH_TRIANGLE_Y = -80, -20
FIRST_LEAVES, SECOND_LEAVES, THIRD_LEAVES, FOUTH_LEAVES  = 200, 180, 160, 140
STAR_LENGTH, STAR_X, STAR_Y = 45, CENTER_X+5, 90
TREE_COLOR, TRUNK_COLOR, STAR_COLOR = "green","brown", "yellow"
#           ___Night Constants___
COLLISION_X1, COLLISION_X2, COLLISION_Y1, COLLISION_Y2 =  CENTER_X-20, CENTER_X+20, CENTER_Y-20, CENTER_Y+20

#----Snow Lists----
snowflakes = []
current_x = []
current_y = []
start_x = []
start_y = []


#----Functions----
#           ___Key Functions___
def Turtle_Stamp():
    #pnt.stamp()
    pnt.stamp()
    
def Forward_KeyDown(event):
    pnt.forward(USER_MOVEMENT)
    pnt.clear()
    wn.ontimer(Turtle_Stamp, STAMP_TIMER)
def Backward_KeyDown(event):
    pnt.back(USER_MOVEMENT)
    pnt.clear()
    wn.ontimer(Turtle_Stamp, REFRESH_TIMER)
def Left_KeyDown(event):
    pnt.left(USER_TURN)
    pnt.clear()
    wn.ontimer(Turtle_Stamp, REFRESH_TIMER)
def Right_KeyDown(event):
    pnt.right(USER_TURN)
    pnt.clear()
    wn.ontimer(Turtle_Stamp, REFRESH_TIMER)

def Star_Collision():
    user_x, user_y = pnt.xcor(), pnt.ycor()
    if (user_x <= X_MAX and user_x >= X_MIN) and (user_y <= Y_MAX and user_y >= Y_MIN):
        x=1

#           ___Snow Functions___
def Make_Snow():
    for i in range(FLAKE_AMOUNT):   
        snowflakes.append(trtl.Turtle())
        current_x.append(random.randint(X_MIN, X_MAX))
        current_y.append(random.randint(Y_MIN, Y_MAX))
        start_x.append(current_x[i])
        start_y.append(current_y[i])
        snowflakes[i].speed(0)
        snowflakes[i].shape('./Snowflake.gif')
        snowflakes[i].up()
def Update_Position():
    global current_x, current_y
    for i in range(FLAKE_AMOUNT):
        snowflakes[i].speed(0)
        fall_speed = random.randint(5,10)
        wind_speed = random.randint(0,5)
        current_x[i] += wind_speed
        current_y[i] -= fall_speed
def Draw_Snow():
    global snowflakes, current_x, current_y
    for i in range(FLAKE_AMOUNT):
        snowflakes[i].goto(current_x[i],current_y[i])
        snowflakes[i].clear()
        snowflakes[i].stamp()
def Snow_Reset():
    global start_x, start_y, current_x, current_y
    for i in range(FLAKE_AMOUNT):
        if current_y[i] <= YMIN_END:
            current_x[i] = random.randint(X_MIN, X_MAX)
            current_y[i] = random.randint(Y_MIN, Y_MAX)
def Complete_Update():
    Update_Position()
    Snow_Reset()
    wn.ontimer(Complete_Update, REFRESH_TIMER)
    wn.ontimer(Draw_Snow, REFRESH_TIMER)

#           ___Tree Functions___
#---- creates the tree trunk and trasports the turtle to the bottom center of the canvas ----
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
    pnt.goto(STAR_X ,STAR_Y)
    pnt.pendown()
    pnt.color(STAR_COLOR)
    pnt.begin_fill()
    pnt.right(95)
    pnt.forward(STAR_LENGTH)
    for i in range(4):
        pnt.right(144)
        pnt.forward(STAR_LENGTH)
    pnt.penup()
    pnt.end_fill()

#                       ===Tree Mother Function===
def Tree_Creation():
    Make_Tree_Trunk()
    Tree_Leaves()
    Make_Star()

    



    

#----Background----
wn.bgpic('./Snow.gif')
wn.addshape('./Snowflake.gif')
""" wn.addshape('./Stand.gif')
wn.addshape('./Run1.gif')
wn.addshape('./Run2.gif') """
#---- prints the code ----
Tree_Creation()


#----Snow----
Make_Snow()
Complete_Update()

#----Keydown Movement----
pnt = trtl.Turtle()
#pnt.shape('./Stand.gif')
pnt.up()
pnt.goto(0,0)
pnt.shapesize(3)
pnt.color(USER_COLOR)
pnt.showturtle()
keyboard.on_press_key(FORWARD_KEY, Forward_KeyDown)
keyboard.on_press_key(BACKWARD_KEY, Backward_KeyDown)
keyboard.on_press_key(LEFT_KEY, Left_KeyDown)
keyboard.on_press_key(RIGHT_KEY, Right_KeyDown)



#----Window Control----

wn.mainloop()

""" TODO:  
        -Make Tree & star (Aiden)
        X-Snow (Caden)X
        -Name w/ box 
        -Presents
        -Godly message
        X-Key down events(Caden)-X
        X-Background (Caden)-X
    
    Credit:
        -Snow (Background)-https://imgs.search.brave.com/d4QyAFytVCoj-nVQSR6nq4k85BTYOFE0AJY4g93Qt7k/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly8xLmJw/LmJsb2dzcG90LmNv/bS8tR05neFRoV2Jt/cE0vVUk2akt6X0FQ/eEkvQUFBQUFBQUFN/aXMvZjVobV9QOWhH/UWsvczE2MDAvU25v/dytEZXNrdG9wK1dh/bGxwYXBlcnMrYW5k/K0JhY2tncm91bmRz/KzEuanBn
        -snowflake -https://imgs.search.brave.com/5w-dcs-urHRlKohdLLuZWT7EO8qsvW43C1PgKl7sw-g/rs:fit:866:1000:1/g:ce/aHR0cHM6Ly9hc3Nl/dHMub25saW5lbGFi/ZWxzLmNvbS9pbWFn/ZXMvY2xpcC1hcnQv/QXJ2aW42MXI1OC9T/bm93Zmxha2UlMjA3/LTE4OTU4Ni5wbmc
        -https://www.google.com/search?client=opera-gx&q=photo+inside+santas+house&sourceid=opera&ie=UTF-8&oe=UTF-8#imgrc=1sMoIFbkLpKHlM
        -https://media.istockphoto.com/id/884338460/vector/gingerbread-man-in-different-poses.jpg?s=612x612&w=0&k=20&c=77XrncZ1oUYnaztNGM4l4RB5ekZrkHk2wov0ZGZgUiM=
        """
