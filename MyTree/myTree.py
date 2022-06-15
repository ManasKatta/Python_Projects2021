import turtle
from turtle import *

MyTree = turtle.Turtle()
_screen = turtle.Screen()
MyTree.speed(50)
MyTree.fillcolor("blue")
MyTree.pencolor("brown")
def draw(MyTree, lineLen):
    if lineLen > 10:
        MyTree.forward(lineLen)
        MyTree.right(20)
        draw(MyTree, lineLen-15)
        MyTree.left(40)
        draw(MyTree,lineLen-15)
        MyTree.right(20)
        MyTree.backward(lineLen)
        
MyTree.left(100)
draw(MyTree,100)
MyTree.screen.exitonclick()