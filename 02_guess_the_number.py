import random

def randomnumber():
    number = random.randint(1,99)
    return number

def main():
    point = 1
    number = randomnumber()
    print("""Hi, I have a number in my mind from 1 to 99.
        Can you guess the number?
        """)
    while point != 0:

        guess = input("--> ")
        if guess == number:
            print("Correct :)")
            point = 0
            pass
        elif guess > number:
            print("Your guess is more than number. Try Again!")
            pass
        elif guess < number:
            print("Your guess is less than number. Try Again!")
            pass
        pass
    pass

if __name__ == '__main__':
    main()
