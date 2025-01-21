import sys

player1 = "x"
player2 = "O"

isFirstPlayer = True

mylist = [[" ", " "," "],
          [" "," "," "],
          [" " ," "," "]]
          

# this function askplayer asks the player where they would like to go, checks its all ok and returns it.
def askplayer(player):
    printgrid()
    row = int(input("what row would you want to replace an item in 1,2 or 3 player " + player + "?"))
    collum = int(input("now what collum would you want to replace an item in 1,2 or 3 player " + player + "?"))
    if row > 3 or row < 1 or collum > 3 or collum < 1 :
        print("cannot be bigger than 3 or smaller than 1")
        sys.exit()
        
    return row, collum
    
def haswon(player):
    if mylist[0][0] == player and mylist[0][1] == player and mylist [0][2] == player:
        return True
    elif mylist[1][0] == player and mylist[1][1] == player and mylist [1][2] == player:
        return True
    elif mylist[2][0] == player and mylist[2][1] == player and mylist [2][2] == player:
        return True
    elif mylist[0][0] == player and mylist[1][0] == player and mylist [2][0] == player:
        return True
    elif mylist[0][1] == player and mylist[1][1] == player and mylist [2][1] == player:
        return True
    elif mylist[0][2] == player and mylist[1][2] == player and mylist [2][2] == player:
        return True
    elif mylist[0][0] == player and mylist[1][1] == player and mylist [2][2] == player:
        return  True
    elif mylist[2][0] == player and mylist[1][1] == player and mylist [0][2] == player:
        return True
def printgrid():
    #prints the final array
    for i in range(3):
        print(mylist[i])

# this for loop, loops askplayer 9 times, it takes the return for the askplayer function and places the naught/crosses in its spot
for i in range(9):
    if isFirstPlayer:
        row, collum = askplayer("1")
        mylist[row-1][collum-1] = player1
        if haswon(player1) == True:
            print("congrats player 1 has won")
            printgrid()
            sys.exit()
    else:
        row, collum = askplayer("2")
        mylist[row-1][collum-1] = player2
        if haswon(player2) == True:
            print("congrats player 2 has won")
            printgrid()
            sys.exit
#switches between firstplayer being true and false so allows the code to swap between players.
    isFirstPlayer = not(isFirstPlayer)
