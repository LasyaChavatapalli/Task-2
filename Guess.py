import random #package for random number
def startgame(name,num):
    no_of_guessesTaken = 0
    while no_of_guessesTaken < 6: #if the number of guesses is less than 6
        inp=input("Guess: ") 
        try:  
            guess_number = int(inp) #stores the guess as an integer instead of a string    

            if guess_number<=200 and guess_number>=1: #if they are in range
                no_of_guessesTaken=no_of_guessesTaken+1 #adds one guess each time the player is wrong
                if no_of_guessesTaken<6:
                    if guess_number<num:
                        print("The guess of the number that you have entered is too low")
                    elif guess_number>num:
                        print("The guess of the number that you have entered is too high")
                    if guess_number != num:
                        print("Try Again!")
                if guess_number==num:
                    break #if the guess is right, then we are going to jump out of the while block
            if guess_number>200 or guess_number<1: #if they aren't in the range
                print("Silly Goose! That number isn't in the range!")
                print("Please enter a number between 1 and 200")

        except: #if a number wasn't entered
            print("I don't think that "+inp+" is a number. Sorry")
            
    if guess_number == num:
        no_of_guessesTaken = str(no_of_guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + no_of_guessesTaken + ' guesses!')

    if guess_number != num:
        print('Nope. The number I was thinking of was ' + str(num))

play_again="yes"
while play_again.lower()=="yes" or play_again.lower()=="y" :
    print("May I ask you for your name?")
    name=input()  
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    print("Go ahead. Guess!")
    num=random.randint(1, 200)
    startgame(name,num)
    print("Do you want to play again?")
    play_again=input()