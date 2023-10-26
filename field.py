import visuals as v
from copy import deepcopy as c
# These are the real visuals
original_field = f"""     |     |
{v._1}|{v._2}|{v._3}
_____|_____|_____
     |     |    
{v._4}|{v._5}|{v._6}
_____|_____|_____
     |     |
{v._7}|{v._8}|{v._9}
     |     |"""
field = c(original_field)
# This is the function that updates the field after a player made his turn
def update_field():
    field = c(f"""     |     |
{v._1}|{v._2}|{v._3}
_____|_____|_____
     |     |    
{v._4}|{v._5}|{v._6}
_____|_____|_____
     |     |
{v._7}|{v._8}|{v._9}
     |     |""")
    return field