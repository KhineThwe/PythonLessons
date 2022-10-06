import random
def play():
	user_choice = input("What's your choice? 'r' for rock,'p' for paper,'s' for scissors\n")
	computer_choice = random.choice(['r','p','s'])
	
	print("Computer_choice",computer_choice)
	
	if user_choice == computer_choice:
		return "It is a tie"
	
	if is_win(user_choice,computer_choice):
		return "You won!"
	return "You Lost!"

def is_win(player,opponent):
	if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
		return True


print(play())

