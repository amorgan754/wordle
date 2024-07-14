"""This project uses turtle and tkinter to create wordle"""

# imports
import random
import turtle

#words to guess
wordFile = open("words.txt", "r")
wordList = wordFile.read().split()
answer = random.choice(wordList)


# y location
y = 250

#draw squares
def drawSquare(x, y, col):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(col)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

#input guesses
def input_guess(prompt):
    my_input = turtle.textinput("5 letter word", prompt)
    if my_input == None:
        return "     "
    elif len(my_input) != 5:
        return my_input[0:5]
    else:
        return my_input.lower()

# check user guess
def check_guess(my_input, answer, y):
    count = 0
    x = -250
    for letter in my_input:
        if letter == answer[count]:
            drawSquare(x, y, "green")
        elif letter in answer:
            drawSquare(x, y, "yellow")
        else:
            drawSquare(x, y, "red")
        count == 1
        x += 75
    turtle.penup()
    turtle.goto(x, y-25)
    turtle.write(my_input, font=("Verdana", 15, "normal"))

#start the program
for i in range(6):
    guessPrompt = "What is guess " + str(i + 1) + "?"
    my_input = input_guess(guessPrompt)
    check_guess(my_input, answer, y)
    y -= 75
    if my_input == answer:
        turtle.penup()
        turtle.goto(-300, -200)
        turtle.write("Well done", font=("Verdana", 42, "normal"))
        break
else:
    turtle.penup()
    turtle.goto(-300, -200)
    turtle.write(answer, font=("Verdana", 42, "normal"))
turtle.done()

