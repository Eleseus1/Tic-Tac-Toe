import copy as c
import visuals as v
import field as f
import time as t
from sys import exit

def play():
    if v._1 == v.empty:
        choice_1 = "1"
    else:
        choice_1 = "/"
    if v._2 == v.empty:
        choice_2 = "2"
    else:
        choice_2 = "/"
    if v._3 == v.empty:
        choice_3 = "3"
    else:
        choice_3 = "/"

    if v._4 == v.empty:
        choice_4 = "4"
    else:
        choice_4 = "/"
    if v._5 == v.empty:
        choice_5 = "5"
    else:
        choice_5 = "/"
    if v._6 == v.empty:
        choice_6 = "6"
    else:
        choice_6 = "/"

    if v._7 == v.empty:
        choice_7 = "7"
    else:
        choice_7 = "/"
    if v._8 == v.empty:
        choice_8 = "8"
    else:
        choice_8 = "/"
    if v._9 == v.empty:
        choice_9 = "9"
    else:
        choice_9 = "/"
    
    choice = ""
    while choice not in ["1", "2", "3", "5", "6", "7", "8", "9"]:
        print("")
        choice = input(f"Player {v.turn}'s turn\n{choice_1}|{choice_2}|{choice_3}\n{choice_4}|{choice_5}|{choice_6}\n{choice_7}|{choice_8}|{choice_9}\nChoose a square: ")
        
        if choice == "1" and v._1 == v.empty:
            if v.turn == "x":
                v._1 = c.deepcopy(v.x)
                f.field = f.update_field()
                v.turn = "o"
                break
            elif v.turn == "o":
                v._1 = c.deepcopy(v.o)
                f.field = f.update_field()
                v.turn = "x"
                break

        elif choice == "2" and v._2 == v.empty:
            if v.turn == "x":
                v._2 = c.deepcopy(v.x)
                f.field = f.update_field()
                v.turn = "o"
                break
            elif v.turn == "o":
                v._2 = c.deepcopy(v.o)
                f.field = f.update_field()
                v.turn = "x"
                break

        elif choice == "3" and v._3 == v.empty:
            if v.turn == "x":
                v._3 = c.deepcopy(v.x)
                f.field = f.update_field()
                v.turn = "o"
                break
            elif v.turn == "o":
                v._3 = c.deepcopy(v.o)
                f.field = f.update_field()
                v.turn = "x"
                break

        elif choice == "4" and v._4 == v.empty:
            if v.turn == "x":
                v._4 = c.deepcopy(v.x)
                f.field = f.update_field()
                v.turn = "o"
                break
            elif v.turn == "o":
                v._4 = c.deepcopy(v.o)
                f.field = f.update_field()
                v.turn = "x"
                break

        elif choice == "5" and v._5 == v.empty:
            if v.turn == "x":
                v._5 = c.deepcopy(v.x)
                f.field = f.update_field()
                v.turn = "o"
                break
            elif v.turn == "o":
                v._5 = c.deepcopy(v.o)
                f.field = f.update_field()
                v.turn = "x"
                break

        elif choice == "6" and v._6 == v.empty:
            if v.turn == "x":
                v._6 = c.deepcopy(v.x)
                f.field = f.update_field()
                v.turn = "o"
                break
            elif v.turn == "o":
                v._6 = c.deepcopy(v.o)
                f.field = f.update_field()
                v.turn = "x"
                break

        elif choice == "7" and v._7 == v.empty:
            if v.turn == "x":
                v._7 = c.deepcopy(v.x)
                f.field = f.update_field()
                v.turn = "o"
                break
            elif v.turn == "o":
                v._7 = c.deepcopy(v.o)
                f.field = f.update_field()
                v.turn = "x"
                break

        elif choice == "8" and v._8 == v.empty:
            if v.turn == "x":
                v._8 = c.deepcopy(v.x)
                f.field = f.update_field()
                v.turn = "o"
                break
            elif v.turn == "o":
                v._8 = c.deepcopy(v.o)
                f.field = f.update_field()
                v.turn = "x"
                break

        elif choice == "9" and v._9 == v.empty:
            if v.turn == "x":
                v._9 = c.deepcopy(v.x)
                f.field = f.update_field()
                v.turn = "o"
                break
            elif v.turn == "o":
                v._9 = c.deepcopy(v.o)
                f.field = f.update_field()
                v.turn = "x"
                break

        else:
            print("Please sellect one of the options")
    print(f.field)
    win_check()

def win_check():
    if v._1 and v._5 and v._9 == "  x  ":
        v.winner = "x"
    elif v._3 and v._5 and v._7 == "  x  ":
        v.winner = "x"
    elif v._1 and v._2 and v._3 == "  x  ":
        v.winner = "x"
    elif v._4 and v._5 and v._6 == "  x  ":
        v.winner = "x"
    elif v._7 and v._8 and v._9 == "  x  ":
        v.winner = "x"
    elif v._1 and v._4 and v._7 == "  x  ":
        v.winner = "x"
    elif v._2 and v._5 and v._8 == "  x  ":
        v.winner = "x"
    elif v._3 and v._6 and v._9 == "  x  ":
        v.winner = "x"

    if v._1 and v._5 and v._9 == "  o  ":
        v.winner = "o"
    elif v._3 and v._5 and v._7 == "  o  ":
        v.winner = "o"
    elif v._1 and v._2 and v._3 == "  o  ":
        v.winner = "o"
    elif v._4 and v._5 and v._6 == "  o  ":
        v.winner = "o"
    elif v._7 and v._8 and v._9 == "  o  ":
        v.winner = "o"
    elif v._1 and v._4 and v._7 == "  o  ":
        v.winner = "o"
    elif v._2 and v._5 and v._8 == "  o  ":
        v.winner = "o"
    elif v._3 and v._6 and v._9 == "  o  ":
        v.winner = "o"

    if v.winner == "x":
        print("Player x wins this match")
    elif v.winner == "o":
        print("Player o wins this match")
    elif v._1 and v._2 and v._3 and v._4 and v._5 and v._6 and v._7 and v._8 and v._9 != v.empty:
        v.winner = "draw"
        print("It`s a draw")

def reset():
    if v.winner == "x":
        v.x_wins +=1
    elif v.winner == "o":
        v.o_wins +=1
    elif v.winner == "draw":
        v.draw += 1
    print(f"Player x`s wins:{v.x_wins}")
    print(f"Player o`s wins:{v.o_wins}")
    print(f"Draws: {v.draw}")
    v.restart_choice = input("Do you want to play again?[Y/n] ")
    if v.restart_choice == "y" or "Y":
        v._1 = v.empty
        v._2 = v.empty
        v._3 = v.empty
        v._4 = v.empty
        v._5 = v.empty
        v._6 = v.empty
        v._7 = v.empty
        v._8 = v.empty
        v._9 = v.empty

        v.turn = "x"
        v.winner = ""
        f.field = c.deepcopy(f.original_field)
    else:
        exit()
"""
play()
print(f.field)
win_check()
"""