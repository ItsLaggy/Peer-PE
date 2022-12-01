import turtle as trtl
import keyboard

pnt = trtl.Turtle()

#----Constants----


#----Functions----
def callback(event):
    userKey = str(event.name)
    if userKey == 'w':
        pnt.forward(5)



#----Execution----
keyboard.on_release(callback)
keyboard.wait('esc')


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
