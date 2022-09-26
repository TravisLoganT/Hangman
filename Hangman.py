# Possible Libraries that will be needed
import sys
import turtle
import time
import time

# Variable Declarations for hangman
win_flag = False
lose_flag = False
flag_a = False
flag_wr = False
game_flag = True
incorrect_count = 0
hmTC = (0, 0)
hm = turtle.Turtle()
hm.speed(0)
state = turtle.Turtle()
state.ht()


def is_correct():
    state.clear()
    state.color("green")
    state.write("This is correct!", font=("Arial", 50, "bold"))


def lost():
    """
    state.clear()
    state.color("white")
    state.write("You have lost!", font=("Arial", 50, "bold"))
    xy_coordinates = letter[0].pos()
    temp = turtle.Turtle()
    temp.ht()
    temp.speed()
    temp.color("white")
    temp.penup()
    temp.setpos(xy_coordinates[0], xy_coordinates[1] + 40)
    temp.pendown()
    temp.write("this was the Movie:", align="left", font=("Arial", 30, "bold"))

    for i in range(len(movie)):
        if movie[i] not in user_list_correct):
            letter[i].color("red")
            letter[i].write(movie[i], align="left", font=("Arial", 20, "bold"))

    """


def winning():
    state.clear()
    state.color("white")
    state.write("You have won!", font=("Arial", 50, "bold"))


def already_used():
    state.clear()
    state.color("green")
    state.write("You have already pressed that key!", font=("Arial", 50, "bold"))


def is_wrong():
    state.clear()
    state.color("red")
    state.write("This is wrong", font=("Arial", 50, "bold"))


if __name__ == '__main__':
    winning()
