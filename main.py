import visuals as v
import menu as m
import sys as s

print("Welcome to Tic Tac Toe")
choice = "0"
while choice not in ["1","2","3"]:
    print("[1]Play\n[2]Stats\n[3]Exit")
    choice = input("(1/2/3): ")
    if choice == "1":
        while v.restart_choice == "y" or "Y":
            while v.winner == "":
               m.play()
            m.reset()
    elif choice == "2":
        print("")
        m.stats_read()
        choice = "0"
    elif choice == "3":
        s.exit()
    else:
        print("\nPlease sellect one of the options")