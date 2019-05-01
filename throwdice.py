import random


def diceroll():
		dice = random.randint(1,6)
		dice2 = random.randint(1,6)
		print("1. Dice = "+str(dice))
		print("2. Dice = "+str(dice2))
		pass


def main():
	point=1
	while point!=0:
		choose = input("""
				Want to throw dice?
				1-Okay
				2-Exit game
				""")
		if choose==1:
			diceroll()
			pass
		elif choose==2:
			point=0
			pass

		pass
	pass

if __name__ == '__main__':
	main()