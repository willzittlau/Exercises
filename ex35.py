from sys import exit

def gold_room():
    print ("The room is full of gold. How much do you take?")
    
    next = input('> ')
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")
    