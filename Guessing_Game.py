import random as rd
def  Guessing_Game():
    attempts = 0
    while True:
        random=rd.randrange(1,100)
        guess=int(input("enter your guessed number:"))
        attempts+=1
        print(f"total attempts={attempts}")
        if guess==random:
            print(f"here the random_number={random}")
            print(f"here the guess_number={guess}")
            print("your guessed number is correct")
            break
        elif guess<random:
            print(f"here the random_number={random}")
            print(f"here the guess_number={guess}")
            print("your guess is to low")
        elif guess>random:
            print(f"here the random_number={random}")
            print(f"here the guess_number={guess}")
            print("your guess is to high")
        else:
            print("you enter incoorect value")
Guessing_Game()
