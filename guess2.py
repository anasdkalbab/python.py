import math, random,sys
z=0

less = 1
most = 100
print("Guess a number between 1 and 1000")
while z<10:
    z = z+1
    guess = random.randint(less,most)
    ask = input("is "+str(guess) + " your guess?")
    if ask == "yes":
        print(str(guess), "is your guess")
        break
    else :
        answer = input("Is your number higher or lower ")
        if answer == "lower":
            x = random.randint(less,guess)
            most = guess-1
        
                
            
        elif answer =="higher":
            x = random.randint(guess,most)  
            less = guess+1

            
