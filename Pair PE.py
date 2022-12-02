import turtle as trtl
import keyboard
import random
import time

trtl.speed(0)
wn = trtl.Screen()
pnt = trtl.Turtle()
#wn.tracer(0)


#----Constants----
#           ___Key Constants___
FORWARD_KEY, LEFT_KEY, BACKWARD_KEY, RIGHT_KEY = 'w', 'a', 's', 'd'  
USER_MOVEMENT, USER_TURN = 15, 15 
#           ___Snow Constants___
FLAKE_AMOUNT, FLAKE_COLOR, REFRESH_TIMER = 30, 'white', 30
X_MIN, X_MAX, Y_MIN, Y_MAX = -400, 400, 300, 400
YMIN_END, YMAX_END = -350, -400

#----Variables----
snowflakes = []
current_x = []
current_y = []
end_y = []


#----Functions----
#           ___Key Events___
def Forward_KeyDown(event):
    pnt.up()
    pnt.forward(USER_MOVEMENT)
def Backward_KeyDown(event):
    pnt.up()
    pnt.back(USER_MOVEMENT)
def Left_KeyDown(event):
    pnt.up()
    pnt.left(USER_TURN)
def Right_KeyDown(event):
    pnt.up()
    pnt.right(USER_TURN)

#           ___Snow Events___
def Make_Snow():
    for i in range(FLAKE_AMOUNT):
        snowflakes.append(trtl.Turtle())
        current_x.append(random.randint(X_MIN, X_MAX))
        current_y.append(random.randint(Y_MIN, Y_MAX))
        snowflakes[i].hideturtle()
        snowflakes[i].speed(0)
        snowflakes[i].shape('./Snowflake.gif')
        snowflakes[i].up()
        #end_y.append(random.randint(YMIN_END, YMAX_END))

    for flake in snowflakes:
        flake.hideturtle()
        flake.penup()
def Update_Position():
    global current_x, current_y
    for i in range(FLAKE_AMOUNT):
        snowflakes[i].speed(0)
        fall_speed = random.randint(1,10)
        wind_speed = random.randint(-10,10)
        current_x[i] += wind_speed
        current_y[i] -= fall_speed
        
def Draw_Snow():
    global snowflakes, current_x, current_y
    for i in range(FLAKE_AMOUNT):
        #snowflakes[i].color(FLAKE_COLOR)
        
        snowflakes[i].goto(current_x[i],current_y[i])
        snowflakes[i].clear()
        snowflakes[i].stamp()
def Update_Complete():
    #global showsnow
    Update_Position()
    wn.update()
   
    wn.ontimer(Update_Complete, REFRESH_TIMER)
    wn.ontimer(Draw_Snow, REFRESH_TIMER)
    #Draw_Snow()
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
tree_color = "green"
trunk_color = "brown"
#---- creates the tree trunk and trasports the turtle to the bottom center of the canvas ----
def make_tree_trunk():
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
def postion():
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
    pnt.penup()
    pnt.end_fill()
    

#---- prints the code ----
make_tree_trunk()
postion()
tree_leaves()
make_star()

    

#----Background----
wn.bgpic('./Snow.gif')
wn.addshape('./Snowflake.gif')

#----Keydown Movement----
keyboard.on_press_key(FORWARD_KEY, Forward_KeyDown)
keyboard.on_press_key(BACKWARD_KEY, Backward_KeyDown)
keyboard.on_press_key(LEFT_KEY, Left_KeyDown)
keyboard.on_press_key(RIGHT_KEY, Right_KeyDown)

#----Snow----
Make_Snow()
showsnow = 'yes'
#while showsnow == 'yes':
Update_Complete()
    #if keyboard.is_pressed('esc') == True:
    #    showsnow = 'no'




#----Window Control----

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
        -snowflake -https://imgs.search.brave.com/5w-dcs-urHRlKohdLLuZWT7EO8qsvW43C1PgKl7sw-g/rs:fit:866:1000:1/g:ce/aHR0cHM6Ly9hc3Nl/dHMub25saW5lbGFi/ZWxzLmNvbS9pbWFn/ZXMvY2xpcC1hcnQv/QXJ2aW42MXI1OC9T/bm93Zmxha2UlMjA3/LTE4OTU4Ni5wbmc
        -https://www.google.com/search?client=opera-gx&q=photo+inside+santas+house&sourceid=opera&ie=UTF-8&oe=UTF-8#imgrc=1sMoIFbkLpKHlM
        """
