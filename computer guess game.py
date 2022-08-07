import random

def computer_guess(x):
    bounds=[0, x]
    user_input=""
    randnum=0
    guess_count=1
    while True:
        randnum=random.randint(bounds[0]+1, bounds[1]-1)
        print(randnum)
        user_input=input("Is this higher(h), lower(l), or just right(r)? ")
        if user_input.lower()=="h":
            bounds[1]=randnum
        elif user_input.lower()=="l":
            bounds[0]=randnum
        elif user_input.lower()=="r":
            break
        else:
            print("Only input h, l, or r.")
        guess_count+=1
    print(f"Game over! The computer had guessed your number in {guess_count} tries.")

maxnum=int(input("Input maximum number to be guessed: "))
computer_guess(maxnum)