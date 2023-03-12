#By Tamas Borbely

from turtle import Turtle
import random 
import math

t = Turtle()
t.speed(100)

listofgraphs = ["Linear", "SinX", "Parablola", "Absolute Value"]
options = ["1", "2", "3", "4", "5", "6"]

t.getscreen().tracer(0)

def basegraph(width, height):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.goto(0, height)
    t.goto(0,0)
    t.goto(width, 0)

def basegraphlabel(width, height):
    t.penup()
    t.goto(0, (height + 1))
    t.pendown()
    t.write("Y, 100")
    t.penup()
    t.goto((width + 1), 0)
    t.pendown()
    t.write("X, 100")
    t.penup()
    t.goto(0, (-height - 10))
    t.pendown()
    t.write("-100")
    t.penup()
    t.goto((-width - 20), 0)
    t.pendown()
    t.write("-100")



def quadgraph(width, height):
    basegraph(width, height)
    basegraph(-width, -height)

def graph1():
    t.penup()
    t.pensize(3)
    t.goto(-90,-90)
    r = 0.2  
    g = 1  
    b = 0.2 
    col = (r,g,b)
    t.color(col)
    t.pendown()
    t.goto(90,90)
    t.write("Linear line")
    t.hideturtle()

def curve():
    for i in range(50):
        t.right(float(2.5))
        t.forward(1)

def lcurve():
    for i in range(50):
        t.left(float(2.5))
        t.forward(1)

def sinx():
    t.reset
    t.penup()
    t.pensize(3)
    t.goto(-100,0)
    r = 1  
    g = 0.2  
    b = 0.2 
    col = (r,g,b)
    t.color(col)
    t.pendown()
    t.goto(-75,50)
    t.left(50)
    curve()
    t.goto(-25,0)
    t.goto(0,-75)
    lcurve()
    t.goto(60,0)
    t.write("SinX")
    t.right(50)
    t.hideturtle()
    t.reset

def paracurve():
    
    t.circle(-15,180)

def parabola():
    t.left(90)
    t.penup()
    t.pensize(3)
    t.goto(-50,-100)
    r = 0.2  
    g = 0.2  
    b = 1 
    col = (r,g,b)
    t.color(col)
    t.pendown()
    t.goto(-15,75)
    #curve()
    paracurve()
    t.goto(50,-100)
    t.penup()
    t.goto(60,-100)
    t.pendown()
    t.write("Parabola")
    t.right(270)
    t.hideturtle()

def absolutevalue():
    t.penup()
    t.pensize(3)
    t.goto(-25,75)
    r = 1  
    g = 0.2  
    b = 1 
    col = (r,g,b)
    t.color(col)
    t.pendown()
    t.goto(0,0)
    t.goto(25,75)
    t.write("Absolute Value")
    t.hideturtle()

a = 100
b = 100

def clear():
    t.getscreen().update()
    t.clear()
    r = 0  
    g = 0 
    b = 0 
    col = (r,g,b)
    t.color(col)
    t.reset
    t.showturtle

def all():
    quadgraph(a,b)
    basegraphlabel(a,b)
    graph1()
    sinx()
    parabola()
    absolutevalue()
    t.getscreen().update()

def startprogram():
    global user_input
    global wantgraph
    print("=============================")
    print("Hello and welcome to my program, The programs functionality is to display what diffrent line graphs look like")
    print("=============================")
    print("This was made by Tamas Borbely")
    wantgraph = True
    while wantgraph == True:
        clear()
        print("=============================")
        print("This is the selection of graphs the program has avalivle:")
        print(listofgraphs)
        print("=============================")
        for i in range(len(listofgraphs)):
            print("To Veiw the: " + listofgraphs[i] + " Press: " + str(i+1))
        print("To Veiw all of the above Press 5")
        print("To Compare 2 Graphs of your choice Press 6")
        print("=============================")
        user_input = input("Please Select a graph you would like to see ")
        if user_input in (options):
            selection()
            groph = True
            while groph == True:
                answer = input("Would you like to see another Graph? (yes/no)  ")
                if answer == "no":
                    wantgraph = False
                    groph = False
                elif answer == "yes":
                    wantgraph = True
                    groph = False
                else:
                    print("Please choose between yes or no")
        else:
            print("That is not a valid input please choose again")
    
def doneprogram():    
    if wantgraph == False:
        print("=============================")
        print("Thank you for trying out my program")
        print("=============================")

def selection():
    if user_input == "1":
        quadgraph(a,b)
        basegraphlabel(a,b)
        graph1()
        t.getscreen().update()

        window = input(" ")
    elif user_input == "2":
        quadgraph(a,b)
        basegraphlabel(a,b)
        sinx()
        t.getscreen().update()

        window = input(" ")
    elif user_input == "3":
        quadgraph(a,b)
        basegraphlabel(a,b)
        t.reset
        parabola()
        t.getscreen().update()

        window = input(" ")
    elif user_input == "4":
        quadgraph(a,b)
        basegraphlabel(a,b)
        absolutevalue()
        t.getscreen().update()

        window = input(" ")
    elif user_input == "5":
        quadgraph(a,b)
        basegraphlabel(a,b)
        all()
        t.getscreen().update()

        window = input(" ")
    elif user_input == "6":
        pick1= True
        compare()

oc = []

def compare():
    pick1= True
    while pick1 == True:
        global comp1
        print("=============================")
        for i in range(len(listofgraphs)):
            print("To Veiw the: " + listofgraphs[i] + " Press: " + str(i+1))
        print("==============================")
        comp1 = input("What is the first graph you would like to see on screen?")
        if comp1 == "1":
            quadgraph(a,b)
            basegraphlabel(a,b)
            graph1()
            oc.append("1")
            t.getscreen().update()

            window = input(" ")
            pick1 = False
            pick2 = True
            compare2()
        elif comp1 == "2":
            quadgraph(a,b)
            basegraphlabel(a,b)
            sinx()
            oc.append("2")
            t.getscreen().update()

            window = input(" ")
            pick1 = False
            pick2 = True
            compare2()
        elif comp1 == "3":
            quadgraph(a,b)
            basegraphlabel(a,b)
            t.reset
            parabola()
            oc.append("3")
            t.getscreen().update()

            window = input(" ")
            pick1 = False
            pick2 = True
            compare2()
        elif comp1 == "4":
            quadgraph(a,b)
            basegraphlabel(a,b)
            absolutevalue()
            oc.append("4")
            t.getscreen().update()

            window = input(" ")
            pick1 = False
            pick2 = True
            compare2()
        else:
            print("That is not a valid input please choose again")


def compare2():
    pick2 = True
    while pick2 == True:
        print("=============================")
        for i in range(len(listofgraphs)):
            print("To Veiw the: " + listofgraphs[i] + " Press: " + str(i+1))
        print("=============================")
        comp2 = input("What is the Second graph you would like to see on screen?")
        if comp2 in (oc):
            print("=============================")
            print("You have already chosen that graph please choose another")
        else:
            if comp2 == "1":
                graph1()
                if comp1 in (oc):
                    oc.remove(comp1)
                t.getscreen().update()

                window = input(" ")
                pick2 = False
            elif comp2 == "2":
                sinx()
                if comp1 in (oc):
                    oc.remove(comp1)
                t.getscreen().update()

                window = input(" ")
                pick2 = False
            elif comp2 == "3":
                parabola()
                if comp1 in (oc):
                    oc.remove(comp1)
                t.getscreen().update()

                window = input(" ")
                pick2 = False
            elif comp2 == "4":
                absolutevalue()
                if comp1 in (oc):
                    oc.remove(comp1)
                t.getscreen().update()

                window = input(" ")
                pick2 = False
            else:
                print("That is not a valid input please choose again")

startprogram()
doneprogram()
