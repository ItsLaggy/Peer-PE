import turtle as trtl
import keyboard
import random
import time

#----Turtle and Window Settings----
pnt = trtl.Turtle()
wn = trtl.Screen()
wn.title('You Received A Christmas Card!')
wn.tracer(0,0)


#----Background----
wn.bgpic('./Snow.gif')
wn.addshape('./Snowflake.gif')


#----Constants----
#           ___Key Constants___
FORWARD_KEY, LEFT_KEY, BACKWARD_KEY, RIGHT_KEY = 'w', 'a', 's', 'd'  
USER_MOVEMENT, USER_TURN, USER_COLOR= 30, 30, 'red'
STAMP_TIMER = 30
#           ___Snow Constants___
FLAKE_AMOUNT,  REFRESH_TIMER = 300, 20
X_MIN, X_MAX, Y_MIN, Y_MAX = -400, 400, -350, 400
YMIN_END, YMAX_END = -350, -400
FALL_1, FALL_2, WIND_1, WIND_2 = 5, 10, 0, 5
#           ___Message Constants___
MESSAGE_X, MESSAGE_Y = 0, 250 
MESSAGE_COLOR, FONT, FONT_SIZE = 'dark red', 'Brush Script MT', 20
#           ___Tree Constants__
CENTER_X, CENTER_Y, TRIANGLE_TURN = 0, -300, 240
FIRST_TRIANGLE_X, FIRST_TRIANGLE_Y = -110, -272
SECOND_TRIANGLE_X, SECOND_TRIANGLE_Y = -100, -190
THIRD_TRIANGLE_X, THIRD_TRIANGLE_Y = -90, -100
FOURTH_TRIANGLE_X, FOURTH_TRIANGLE_Y = -80, -20
FIRST_LEAVES, SECOND_LEAVES, THIRD_LEAVES, FOUTH_LEAVES  = 200, 180, 160, 140
STAR_LENGTH, STAR_X, STAR_Y = 45, CENTER_X+5, 90
TREE_COLOR, TRUNK_COLOR, STAR_COLOR, OUT_LINE_PRESENT = "green","brown", "yellow","blue"
#           ___Night Constants___
COLLISION_X1, COLLISION_X2, COLLISION_Y1, COLLISION_Y2 =  CENTER_X-15, CENTER_X+15, 100, 130
#           ___Orna & Presents Constants___
ORNA_RADIUS = 10
ORNA_COLORS=['blue','red','pink','purple','orange', 'dark red', 'dark green', 'fuchsia', 'dark blue']
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

'''_______________________________________________________________________________________Caden_______________________________________________________________________________________'''

#----Misc Lists & Vars----
snowflakes = []
current_x = []
current_y = []
start_x = []
start_y = []
night = False



#----Functions----
#           ___Key Functions___
def Turtle_Stamp(): 
    pnt.stamp()
    
def Forward_KeyDown(event):
    pnt.forward(USER_MOVEMENT)
    pnt.clear()
    wn.ontimer(Turtle_Stamp, STAMP_TIMER)
    Star_Collision()
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
#            ___Collision___
def Star_Collision():
    global night
    user_x, user_y = pnt.xcor(), pnt.ycor()
    print(f'{user_x},{user_y}')
    if (user_x <= COLLISION_X2 and user_x >= COLLISION_X1) and (user_y <= COLLISION_Y2 and user_y >= COLLISION_Y1):
        pnt.backward(USER_MOVEMENT)
        if night:
            wn.bgpic('./Snow.gif')
            night = False
        else:
            wn.bgpic('./SnowNight.gif')
            night = True
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
        fall_speed = random.randint(FALL_1, FALL_2)
        wind_speed = random.randint(WIND_1, WIND_2)
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

#           ___Card Message___
def Make_Message(name):
    if name.lower() == 'scrooge':
        exit()
    else:
        pnt.goto(MESSAGE_X,MESSAGE_Y)
        pnt.color(MESSAGE_COLOR)
        pnt.write(f'Have a Merry Christmas {name}, Jesus loves you!', align=('center'), font=(FONT,FONT_SIZE,'bold'))

'''_______________________________________________________________________________________Aiden_______________________________________________________________________________________'''
#           ___Tree Functions___
#---- creates the tree trunk and trasports the turtle to the bottom center of the canvas ----
#---- ordament function ----
def Make_Orna():
    pnt.speed(0)
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
    pnt.penup()
#----On click Orna----
def Click_Orna(filler1,filler2):
    print('New Lights')
    save_x, save_y, save_head = pnt.xcor(), pnt.ycor(), pnt.heading()
    pnt.seth(285)
    pnt.pencolor(STAR_COLOR)
    Make_Orna()
    pnt.goto(save_x, save_y), pnt.seth(save_head)
#---- present function ----
def Make_Gifts():
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
    pnt.penup()

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
    pnt.goto(turtle_x, turtle_y)
    pnt.pendown()
    pnt.setheading(0)
#---- make tree leaves ----
def Tree_Leaves():
    Turtle_Position(FIRST_TRIANGLE_X, FIRST_TRIANGLE_Y)
    Make_Triangle(FIRST_LEAVES)
    Turtle_Position(SECOND_TRIANGLE_X, SECOND_TRIANGLE_Y)
    Make_Triangle(SECOND_LEAVES)
    Turtle_Position(THIRD_TRIANGLE_X, THIRD_TRIANGLE_Y)
    Make_Triangle(THIRD_LEAVES)
    Turtle_Position(FOURTH_TRIANGLE_X, FOURTH_TRIANGLE_Y)
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
    Make_Orna()
    Make_Gifts()


#=====MAIN CODE======================================================================================================#
#----Background----
wn.bgpic('./Snow.gif')
wn.addshape('./Snowflake.gif')

#----Generation----
Tree_Creation()
Make_Snow()
Complete_Update()

#----Message----
user_name = trtl.textinput('What is your name?', 'Please enter your name')
Make_Message(user_name)

#----Keydown Movement----
pnt = trtl.Turtle()
pnt.up()
pnt.goto(0,0)
pnt.shapesize(3)
pnt.color(USER_COLOR)
pnt.showturtle()
wn.onclick(Click_Orna)
keyboard.on_press_key(FORWARD_KEY, Forward_KeyDown)
keyboard.on_press_key(BACKWARD_KEY, Backward_KeyDown)
keyboard.on_press_key(LEFT_KEY, Left_KeyDown)
keyboard.on_press_key(RIGHT_KEY, Right_KeyDown)




#----Window Control----

wn.mainloop()

""" TODO:  
        X-Make Tree & star (Aiden)X
        X-Snow (Caden)X
        X-Name w/ box X
        X-PresentsX
        X-Godly messageX
        X-Key down events(Caden)-X
        X-Background (Caden)-X
    
    Credit:
        -Snow (Background)-https://imgs.search.brave.com/d4QyAFytVCoj-nVQSR6nq4k85BTYOFE0AJY4g93Qt7k/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly8xLmJw/LmJsb2dzcG90LmNv/bS8tR05neFRoV2Jt/cE0vVUk2akt6X0FQ/eEkvQUFBQUFBQUFN/aXMvZjVobV9QOWhH/UWsvczE2MDAvU25v/dytEZXNrdG9wK1dh/bGxwYXBlcnMrYW5k/K0JhY2tncm91bmRz/KzEuanBn
        -snowflake -https://imgs.search.brave.com/5w-dcs-urHRlKohdLLuZWT7EO8qsvW43C1PgKl7sw-g/rs:fit:866:1000:1/g:ce/aHR0cHM6Ly9hc3Nl/dHMub25saW5lbGFi/ZWxzLmNvbS9pbWFn/ZXMvY2xpcC1hcnQv/QXJ2aW42MXI1OC9T/bm93Zmxha2UlMjA3/LTE4OTU4Ni5wbmc
        """
