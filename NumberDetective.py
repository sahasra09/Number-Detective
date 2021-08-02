import random
print("NUMBER DETECTIVE")
print("Hola! Ready for the challenge?")
ND = random.randint(1, 15)
print("Guess a number from 1 to 15. Lets see if luck favours you!:")
chance = 0
while chance < 5:

    guess = int(input("Enter your guess:- "))

    if guess == ND:

        print("Congratulation YOU WON!!!")
        break

    if guess < ND:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chance+=1

if not chance < 5:
    print("YOU LOSE!!! The number is", ND)