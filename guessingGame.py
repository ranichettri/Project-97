import random
number= random.randint(1,9)
chance= 0
player= input("Enter your name:-")
name= "Guessing the number"
intro= "Guess a number (between 1 and 9) GOOD LUCK!!!:)"
print(name)
print(intro)
#print(number)
guess= int(input("Enter your guess:-"))

while chance < 5:
    if number==guess:
        chance= chance+1
        if chance == 5:
            break
        print("CONGRATULATIONS!! ",player," did it:)")
        break
    else:
        chance= chance+1
        if chance == 5:
            break
        if guess > number : 
            hint= "high"
            hmm= "lower than"
        else:
            hint= "low"
            hmm= "higher than"
        print("You were too",hint,player,":( Try guessing!!",hmm,guess)
        #print(number)
        guess= int(input("Enter your guess:-"))

if not chance < 5:
    if number==guess:
        print("CONGRATULATION!!",player," did it:) ")
    if number!=guess:
        print("OH NO",player,"!! You lost:(!! The number is ",number)
        
