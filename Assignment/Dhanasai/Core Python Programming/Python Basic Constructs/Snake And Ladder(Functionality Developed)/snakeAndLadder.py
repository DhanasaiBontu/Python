import random

#UC 1 is start game with players at position 0

def start_game(num_players=1):
	positions = [0] * num_players
	dice_count = [0] * num_players
	return positions, dice_count

#UC 2 Roll the die
 
def roll_die():
	return random.randint(1,6)

# UC 3 check the option for No play, Ladder, Snake

def check_option():
	return random.choice(["NO_PLAY","LADDER","SNAKE"])

# UC 4 Repeat till player reaches winning position 100

def move_player(position, die_value, option):
	if option == "LADDER":
		position+=die_value
	elif option == "SNAKE":
		position-=die_value
	#NO_PLAY = no change
	
	if position<0:
		position=0
	return position

# UC 5 Ensure Exact winning position 100

def check_exact_win(position, previous_position):
	if position>100:
		return previous_position
	return position


# UC 6 Report number of dice rolls and position after each roll

def play_single_player():
	position,dice_count=start_game(1)
	position=position[0]	
	dice_count=dice_count[0]
	print("Single player game is started")
	while position!=100:
		die=roll_die()
		option=check_option()
		prev_position=position
		position = move_player(position,die,option)
		position=check_exact_win(position,prev_position)
		dice_count+=1
		print(f"Dice Roll: {die}, Option: {option}, Position: {position}")
	print(f"\nPlayer won the game in {dice_count} dice rolls\n")


# UC 7 Play game with 2 players and report the winner

def play_two_players():
	positions, dice_counts=start_game(2)
	current_player=0
	print("Two players game started")
	while True:
		die=roll_die()
		option=check_option()
		prev_position=positions[current_player]
		positions[current_player] = move_player(positions[current_player], die, option)
		positions[current_player] = check_exact_win(positions[current_player],prev_position)
		dice_counts[current_player]+=1
		print(f"Player {current_player + 1} | Dice:{die} | Option:{option} | Position: {positions[current_player]}")
		if positions[current_player]==100:
			print(f"\nPlayer {current_player + 1} WON the game in {dice_counts[current_player]} dice rolls")
			break
		current_player = 1-current_player

if __name__ == "__main__":
	play_single_player()
	play_two_players()