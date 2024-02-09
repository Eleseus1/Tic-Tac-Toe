import copy as c
import visuals as v
import field as f
import random as r
from time import localtime as time
from time import sleep
from sys import exit
from os.path import exists

# This is the main code for the PvP games
def play():
    if v.start_time == "":
        v.start_time = time()
        v.start_time = str(v.start_time[3])+":"+str(v.start_time[4])

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
    
    choices = ""
    while choices not in ["1", "2", "3", "5", "6", "7", "8", "9"]:
        print("")
        choices = input(f"Player {v.turn}'s turn\n{choice_1}|{choice_2}|{choice_3}\n{choice_4}|{choice_5}|{choice_6}\n{choice_7}|{choice_8}|{choice_9}\nChoose a square: ")
        
        if choices == "1" and v._1 == v.empty:
            if v.turn == "x":
                v._1 = c.deepcopy(v.x)
                v.turn = "o"
                break
            elif v.turn == "o":
                v._1 = c.deepcopy(v.o)
                v.turn = "x"
                break

        elif choices == "2" and v._2 == v.empty:
            if v.turn == "x":
                v._2 = c.deepcopy(v.x)
                v.turn = "o"
                break
            elif v.turn == "o":
                v._2 = c.deepcopy(v.o)
                v.turn = "x"
                break

        elif choices == "3" and v._3 == v.empty:
            if v.turn == "x":
                v._3 = c.deepcopy(v.x)
                v.turn = "o"
                break
            elif v.turn == "o":
                v._3 = c.deepcopy(v.o)
                v.turn = "x"
                break

        elif choices == "4" and v._4 == v.empty:
            if v.turn == "x":
                v._4 = c.deepcopy(v.x)
                v.turn = "o"
                break
            elif v.turn == "o":
                v._4 = c.deepcopy(v.o)
                v.turn = "x"
                break

        elif choices == "5" and v._5 == v.empty:
            if v.turn == "x":
                v._5 = c.deepcopy(v.x)
                v.turn = "o"
                break
            elif v.turn == "o":
                v._5 = c.deepcopy(v.o)
                v.turn = "x"
                break

        elif choices == "6" and v._6 == v.empty:
            if v.turn == "x":
                v._6 = c.deepcopy(v.x)
                v.turn = "o"
                break
            elif v.turn == "o":
                v._6 = c.deepcopy(v.o)
                v.turn = "x"
                break

        elif choices == "7" and v._7 == v.empty:
            if v.turn == "x":
                v._7 = c.deepcopy(v.x)
                v.turn = "o"
                break
            elif v.turn == "o":
                v._7 = c.deepcopy(v.o)
                v.turn = "x"
                break

        elif choices == "8" and v._8 == v.empty:
            if v.turn == "x":
                v._8 = c.deepcopy(v.x)
                v.turn = "o"
                break
            elif v.turn == "o":
                v._8 = c.deepcopy(v.o)
                v.turn = "x"
                break

        elif choices == "9" and v._9 == v.empty:
            if v.turn == "x":
                v._9 = c.deepcopy(v.x)
                v.turn = "o"
                break
            elif v.turn == "o":
                v._9 = c.deepcopy(v.o)
                v.turn = "x"
                break

        else:
            print("Please sellect one of the options")
    f.field = f.update_field()
    print(f.field)
    win_check()

# This is the main code for the PvE mode on easy
def play_easy():
    if v.start_time == "":
        v.start_time = time()
        v.start_time = str(v.start_time[3])+":"+str(v.start_time[4]) # This saves the start time for the stats
    field_list = []
    # This checks if the squares are empty for the players turn
    if v._1 == v.empty:
        choice_1 = "1"
        field_list.append(v._1)
    else:
        choice_1 = "/"
    if v._2 == v.empty:
        choice_2 = "2"
        field_list.append(v._2)
    else:
        choice_2 = "/"
    if v._3 == v.empty:
        choice_3 = "3"
        field_list.append(v._3)
    else:
        choice_3 = "/"

    if v._4 == v.empty:
        choice_4 = "4"
        field_list.append(v._4)
    else:
        choice_4 = "/"
    if v._5 == v.empty:
        choice_5 = "5"
        field_list.append(v._5)
    else:
        choice_5 = "/"
    if v._6 == v.empty:
        choice_6 = "6"
        field_list.append(v._6)
    else:
        choice_6 = "/"

    if v._7 == v.empty:
        choice_7 = "7"
        field_list.append(v._7)
    else:
        choice_7 = "/"
    if v._8 == v.empty:
        choice_8 = "8"
        field_list.append(v._8)
    else:
        choice_8 = "/"
    if v._9 == v.empty:
        choice_9 = "9"
        field_list.append(v._9)
    else:
        choice_9 = "/"
    
    choices = ""
    #The players turn
    while v.turn == "x": 
        print("")
        choices = input(f"Player {v.turn}'s turn\n{choice_1}|{choice_2}|{choice_3}\n{choice_4}|{choice_5}|{choice_6}\n{choice_7}|{choice_8}|{choice_9}\nChoose a square: ")
        
        if choices == "1" and v._1 == v.empty:
                v._1 = c.deepcopy(v.x)
                v.turn = "o"
                break

        elif choices == "2" and v._2 == v.empty:
                v._2 = c.deepcopy(v.x)
                v.turn = "o"
                break

        elif choices == "3" and v._3 == v.empty:
                v._3 = c.deepcopy(v.x)
                v.turn = "o"
                break

        elif choices == "4" and v._4 == v.empty:
                v._4 = c.deepcopy(v.x)
                v.turn = "o"
                break

        elif choices == "5" and v._5 == v.empty:
                v._5 = c.deepcopy(v.x)
                v.turn = "o"
                break

        elif choices == "6" and v._6 == v.empty:
                v._6 = c.deepcopy(v.x)
                v.turn = "o"
                break

        elif choices == "7" and v._7 == v.empty:
                v._7 = c.deepcopy(v.x)
                v.turn = "o"
                break

        elif choices == "8" and v._8 == v.empty:
                v._8 = c.deepcopy(v.x)
                v.turn = "o"
                break

        elif choices == "9" and v._9 == v.empty:
                v._9 = c.deepcopy(v.x)
                v.turn = "o"
                break

        else:
            print("Please sellect one of the options")
    f.field = f.update_field()
    print(f.field)
    win_check()
    field_list = []
    # This checks if the squares are empty for the bots turn
    if v._1 == v.empty:
        choice_1 = "1"
        field_list.append(v._1)
    else:
        choice_1 = "/"
    if v._2 == v.empty:
        choice_2 = "2"
        field_list.append(v._2)
    else:
        choice_2 = "/"
    if v._3 == v.empty:
        choice_3 = "3"
        field_list.append(v._3)
    else:
        choice_3 = "/"

    if v._4 == v.empty:
        choice_4 = "4"
        field_list.append(v._4)
    else:
        choice_4 = "/"
    if v._5 == v.empty:
        choice_5 = "5"
        field_list.append(v._5)
    else:
        choice_5 = "/"
    if v._6 == v.empty:
        choice_6 = "6"
        field_list.append(v._6)
    else:
        choice_6 = "/"

    if v._7 == v.empty:
        choice_7 = "7"
        field_list.append(v._7)
    else:
        choice_7 = "/"
    if v._8 == v.empty:
        choice_8 = "8"
        field_list.append(v._8)
    else:
        choice_8 = "/"
    if v._9 == v.empty:
        choice_9 = "9"
        field_list.append(v._9)
    else:
        choice_9 = "/"
    # The bots turn
    sleep(1)
    while v.turn == "o" and v.x_winner == False and v.winner != "draw":
        field_o = r.randint(1,9)

        if field_o == 1 and v._1 == v.empty:
            v._1 = c.deepcopy(v.o)
            v.turn = "x"
            break

        elif field_o == 2 and v._2 == v.empty:
            v._2 = c.deepcopy(v.o)
            v.turn = "x"
            break

        elif field_o == 3 and v._3 == v.empty:
            v._3 = c.deepcopy(v.o)
            v.turn = "x"
            break

        elif field_o == 4 and v._4 == v.empty:
            v._4 = c.deepcopy(v.o)
            v.turn = "x"
            break

        elif field_o == 5 and v._5 == v.empty:
            v._5 = c.deepcopy(v.o)
            v.turn = "x"
            break

        elif field_o == 6 and v._6 == v.empty: 
            v._6 = c.deepcopy(v.o)
            v.turn = "x"
            break

        elif field_o == 7 and v._7 == v.empty:
            v._7 = c.deepcopy(v.o)
            v.turn = "x"
            break

        elif field_o == 8 and v._8 == v.empty:
            v._8 = c.deepcopy(v.o)
            v.turn = "x"
            break

        elif field_o == 9 and v._9 == v.empty:
            v._9 = c.deepcopy(v.o)
            v.turn = "x"
            break
            
    if v.x_winner == False:
        f.field = f.update_field()
        print("\nEasy Bots turn:")
        print(f.field)
        win_check()
        


def win_check():
    if v._1  == "  x  " and v._5  == "  x  " and v._9 == "  x  ":
        v.winner = "x"
    elif v._3  == "  x  " and v._5  == "  x  " and v._7 == "  x  ":
        v.winner = "x"
    elif v._1  == "  x  " and v._2  == "  x  " and v._3 == "  x  ":
        v.winner = "x"
    elif v._4  == "  x  " and v._5  == "  x  " and v._6 == "  x  ":
        v.winner = "x"
    elif v._7  == "  x  " and v._8 == "  x  " and v._9 == "  x  ":
        v.winner = "x"
    elif v._1 == "  x  " and v._4  == "  x  " and v._7 == "  x  ":
        v.winner = "x"
    elif v._2 == "  x  " and v._5 == "  x  " and v._8 == "  x  ":
        v.winner = "x"
    elif v._3 == "  x  " and v._6 == "  x  "and v._9 == "  x  ":
        v.winner = "x"

    if v._1 == "  o  " and v._5 == "  o  " and v._9 == "  o  ":
        v.winner = "o"
    elif v._3 == "  o  " and v._5 == "  o  " and v._7 == "  o  ":
        v.winner = "o"
    elif v._1 == "  o  " and v._2 == "  o  " and v._3 == "  o  ":
        v.winner = "o"
    elif v._4 == "  o  " and v._5 == "  o  " and v._6 == "  o  ":
        v.winner = "o"
    elif v._7 == "  o  " and v._8 == "  o  " and v._9 == "  o  ":
        v.winner = "o"
    elif v._1 == "  o  " and v._4 == "  o  " and v._7 == "  o  ":
        v.winner = "o"
    elif v._2 == "  o  " and v._5 == "  o  " and v._8 == "  o  ":
        v.winner = "o"
    elif v._3 == "  o  " and v._6 == "  o  " and v._9 == "  o  ":
        v.winner = "o"

    if v.winner == "x":
        print("Player x wins this match")
        v.x_winner = True
    elif v.winner == "o":
        print("Player o wins this match")
    # elif v._1 != v.empty and v._2 != v.empty and v._3 != v.empty and v._4 != v.empty and v._5 != v.empty and v._6 != v.empty and v._7 != v.empty and v._8 != v.empty and v._9 != v.empty:
    elif v.empty not in [v._1,v._2,v._3,v._4,v._5,v._6,v._7,v._8,v._9]:
        v.winner = "draw"
        print("It`s a draw")

def reset():
    if v.winner == "x":
        v.x_wins +=1
    elif v.winner == "o":
        v.o_wins +=1
    elif v.winner == "draw":
        v.draw += 1
    v.games = v.x_wins + v.o_wins + v.draw
    total_wins = (f"Games played: {v.games}\nPlayer x`s wins: {v.x_wins}\nPlayer o`s wins: {v.o_wins}\nDraws: {v.draw}\n")
    print(total_wins)
    v.restart_choice = input("Do you want to play again?[Y/n] ")
    if v.restart_choice == "y" and "Y":
        v._1 = v.empty
        v._2 = v.empty
        v._3 = v.empty
        v._4 = v.empty
        v._5 = v.empty
        v._6 = v.empty
        v._7 = v.empty
        v._8 = v.empty
        v._9 = v.empty
        if v.gamemode == "player":
            if v.x_wins < v.o_wins:
                v.turn = "x"
            elif v.o_wins < v.x_wins:
                v.turn = "o"
        else:
            v.turn = "x"
        v.x_winner = False
        v.winner = ""
        f.field = c.deepcopy(f.original_field)
    else:
        stats_write(total_wins)
        exit()
    return total_wins

def stats_write(total_wins):
    date = time()
    if v.start_time == str(date[3])+":"+str(date[4]):
        date = str(date[2]) +", "+ str(date[1]) +", "+ str(date[0]) +" "+str(date[3])+":"+str(date[4])+"\n"
    elif v.gamemode == "player":
        player_x = input("Player x`s name: ")
        player_o = input("Player o`s name: ")
        date = str(date[2]) +", "+ str(date[1]) +", "+ str(date[0]) +" "+v.start_time+"-"+str(date[3])+": "+str(date[4])+" "+player_x+" vs. "+player_o+"\n"
    
    elif v.gamemode == "easy":
        player_x = input("Player x`s name: ")
        date = str(date[2]) +", "+ str(date[1]) +", "+ str(date[0]) +" "+v.start_time+"-"+str(date[3])+": "+str(date[4])+" "+player_x+" vs. "+"Easy Bot"+"\n"
    
    elif v.gamemode == "medium":
        player_x = input("Player x`s name: ")
        date = str(date[2]) +", "+ str(date[1]) +", "+ str(date[0]) +" "+v.start_time+"-"+str(date[3])+": "+str(date[4])+" "+player_x+" vs. "+"Medium Bot"+"\n"
    

    elif v.gamemode == "undefeatable":
        player_x = input("Player x`s name: ")
        date = str(date[2]) +", "+ str(date[1]) +", "+ str(date[0]) +" "+v.start_time+"-"+str(date[3])+": "+str(date[4])+" "+player_x+" vs. "+"Undefeatable Bot"+"\n"

    if v.games > 0:
        with open("ttt_stats.txt","a") as s:
            s.write(str(date)+str(total_wins)+"\n")

def stats_read():

    file_exists = exists("ttt_stats.txt")
    if file_exists == False:
        print("Play some games to fill the stats tab")
    else:
        with open("ttt_stats.txt","r") as s:
            stats = s.read()
        print(stats)

"""
play()
print(f.field)
win_check()
"""