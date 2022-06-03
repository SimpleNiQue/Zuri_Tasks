#! usr/bin/python3
from random import choice


win_class = {
	'R':'S',
	'P':'R',
	'S':'P',
}

entry = {
	'R':'Rock',
	'P':'Paper',
	'S':'Scissors'
}

def RPS():
	print("R = Rock, P = Paper, S = Scissors")
	player = input("Enter Your Choice\n")
	computer = choice(['R', 'P', 'S'])

	if player not in win_class:
		print("Invalid Entry")
		RPS()
	else:
		if computer == win_class[player]:
			print(f"Player({entry[player]}) : CPU({entry[computer]})")
			print(f"Player wins")
			return True

		elif player == win_class[computer]:
			print(f"Player({entry[player]}) : CPU({entry[computer]})")
			print(f"Computer Wins")
			return True

		else:
			print(f"Player({entry[player]}) : CPU({entry[computer]})")
			print(f'Draw')
			RPS()

play = RPS()
play
