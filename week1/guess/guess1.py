import sys,random,math

print("Choose a number between 1-100 and i will guess it")

#guess a number
def guess(min,max):
    guess0 = random.randint(min,max)
    return guess0



#check if our number is the number the user got and if not weather it is higher or lower
def check():
    Min = 1
    Max = 100
    number_of_guesses = 0 
    
    while number_of_guesses < 10 :
        number_of_guesses = number_of_guesses +1
        number = guess(Min,Max)
    
        ans = input("Is "+ str(number)+" yor number? ")

    

        if ans[0] == 'n' or ans[0] =='N':
            hl = input("Is your number higher or lower ")
            if hl[0] == 'l':
                Max = number-1
            
            elif hl[0]=='h':
                Min = number+1
        else:
            print(str(number)+" is your number.")
            
            number_of_guesses =100



check()
#number_of_guesses = number_of_guesses + 1
