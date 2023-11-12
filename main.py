import visuals as v
import menu as m
import sys as s

print("Welcome to Tic Tac Toe\n")
choice = "0"
while choice not in ["1","2","3"]:
    print("[1]Play\n[2]Stats\n[3]Exit")
    choice = input("(1/2/3): ")
    if choice == "1":
        print("\n[1]PvP\n[2]PvE Easy\n[3]PvE Medium\n[4]PvE Undefeatable\n")
        choice = input("(1/2/3): ")
        if choice == "1":
            while v.restart_choice == "y" or "Y":
                while v.winner == "":
                   m.play()
                m.reset()
                v.gametype = "player"
        if choice == "2":
            while v.restart_choice == "y" or "Y":
                while v.winner == "":
                   m.play_easy()
                m.reset()
                v.gametype = "easy"
        else:
            print("\nPlease sellect one of the options")
    elif choice == "2":
        print("")
        m.stats_read()
        choice = "0"
    elif choice == "3":
        s.exit()
    else:
        print("\nPlease sellect one of the options")