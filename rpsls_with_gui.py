import random
import simplegui
"""
The given program plays rock, paper, scissorcs, lizard, 
spock with you.
"""

#function to convert name into number
def name_to_number(player_choice):
    if (player_choice == "rock"):
        return 0
    elif(player_choice == "spock"):
        return 1
    elif(player_choice == "paper"):
        return 2
    elif(player_choice == "lizard"):
        return 3
    elif(player_choice == "scissors"):
        return 4
#function to convert number into name        
def number_to_name(num):
    if(num == 0): return "rock"
    elif(num == 1): return "spock"
    elif(num == 2): return "paper"
    elif(num == 3): return "lizard"
    elif(num == 4): return "scissors"

#main function
def rpsls(player_choice):
    com_num = random.randrange(0,5) #generates random int from 0 to 4
    com_choice = number_to_name(com_num)
    player_num = name_to_number(player_choice)
    print "Player chooses", player_choice+"."
    print "Computer chooses", com_choice+"."
    
    if(com_num == player_num):
        print "Player and Computer tie!" 
        print " "
        return
        
    elif((com_num-player_num < 0) and (com_num-player_num > -3)):
            print "Player wins!"
            print " "
        
    
    else:
        print "Computer wins!"
        print " " 

#definition of the event handler        
def get_input(txt):
    return rpsls(txt)

#create a frame and assign callback to event handles
frame = simplegui.create_frame("RPSLS", 200,200)
frame.add_input("Choose one", get_input,200)

get_input("scissors")
get_input("paper")
get_input("rock")
get_input("lizard")
    
        
  