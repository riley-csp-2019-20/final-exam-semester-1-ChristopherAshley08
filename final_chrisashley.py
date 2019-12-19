#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name Christopher Ashley
#
#Date 12-19-19
#


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#===================import===================

import turtle as trtl
import turtle as player
import turtle as sc

#===================create turtle===================

sc=sc.Turtle()
player=player.Turtle()
player._delay(0)

#===================setup===================

ps=1                      #pensize
player.pencolor("black")
player.pensize(ps)
player.speed(0)
player.turtlesize(1)
eraser=0
pup=0                     #penup/down
sc.ht()
                
#===================title===================

def title():
    sc.penup()
    sc.goto(-100,350)
    font = ("roboto", 25, "bold")
    sc.write("Etch-A-Sketch", font=font)

def title2():
    sc.penup()
    sc.goto(-70,330)
    font = ("roboto", 10, "bold")
    sc.write("Created By: Chris Ashley", font=font)

title()
title2()

#===================instructions===================

def rule_clear():
    sc.penup()
    sc.goto(-300,100)
    font = ("roboto", 50, "bold")
    sc.write("space=clear", font=font)

def rule_penlarge():
    sc.penup()
    sc.goto(-300,0)
    font = ("roboto", 50, "bold")
    sc.write("o=bigger,p=smaller", font=font)

def rule_pendown():
    sc.penup()
    sc.goto(-300,-100)
    font = ("roboto", 50, "bold")
    sc.write("u=pendown/up", font=font)

def rule_changecolor():
    sc.penup()
    sc.goto(-300,-200)
    font = ("roboto", 50, "bold")
    sc.write("c=changecolor", font=font)

def rule_movement():
    sc.penup()
    sc.goto(-300,200)
    font = ("roboto", 50, "bold")
    sc.write("Arrows=movement", font=font)

def rule_clear_rules():
    sc.penup()
    sc.goto(-300,-300)
    font = ("roboto", 50, "bold")
    sc.write("space to go back", font=font)

def write_rule():
    sc.penup()
    sc.goto(-475,-390)
    font = ("roboto", 15, "bold")
    sc.write("r=rules", font=font)

write_rule()

#===================rulepopup===================

def rulepopup():
    clearscreen()
    player.ht()
    player.penup()
    rule_changecolor()
    rule_clear()
    rule_movement()
    rule_pendown()
    rule_penlarge()
    rule_clear_rules()

#===================pencolor===================

def changecolor():
    playercolor = input("please enter the color you would like to change to:")
    player.pencolor(playercolor)

#===================movement===================

def up():
    #player.setheading(90)
    player.forward(5)

def right():
    player.right(10)
    #player.forward(10)

def left():
    player.left(10)
    #player.forward(10)

def down():
    #player.setheading(90*3)
    player.forward(5)

#===================eraser===================

def erase():
    global eraser
    if eraser == 0:
        player.pencolor("white")
        eraser = 1
    else:
        player.pencolor("black")
        eraser = 0

#===================clearscreen===================

def clearscreen():
    player.st()
    player.setheading(0)
    player.penup()
    player.speed(0)
    player.goto(0,0)
    player.pendown()
    player.pensize(1000)
    player.pencolor("white")
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.setheading(180)
    player.penup()
    player.speed(0)
    player.goto(0,0)
    player.pendown()
    player.pensize(1000)
    player.pencolor("white")
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.forward(1000)
    player.right(90)
    player.penup()
    player.pensize(ps)
    player.pencolor("black")
    player.goto(0,0)
    title()
    title2()
    write_rule()
    player.pendown()

#===================pensize===================

def penlarger():
    global ps
    ps += 1
    player.pensize(ps)

def pensmaller():
    global ps
    ps -= 1
    player.pensize(ps)
    if ps == 0:
        ps = 1

#===================penup/down===================

def pdown():
    global pup
    if pup == 0:
        player.penup()
        pup = 1
    else:
        player.pendown()
        pup = 0

#===================create screen===================

wn = trtl.Screen()

#===================keypresses===================

wn.onkeypress(up,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(erase,"e")
wn.onkeypress(clearscreen,"space")
wn.onkeypress(penlarger,"o")
wn.onkeypress(pensmaller,"p")
wn.onkeypress(pdown,"u")
wn.onkeypress(changecolor,"c")
wn.onkeypress(rulepopup,"r")

#===================listen===================

wn.listen()

#===================mainloop===================

wn.mainloop()