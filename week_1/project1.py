#rock paper scissors game 

#allow program to pick randomly 

import random 

print("Hello friend! ","welcome to the game" ) 

user_score = 0
computer_score = 0
game_rounds = 0

while game_rounds < 3 : 
    program_pick=random.choice(['rock','paper','scissors']) 
    user_guess=input("pick a guess; rock, paper or scissors?  ") 
    user_guess=str(user_guess) 

    game_rounds=game_rounds + 1
    print('rounds payed: ', game_rounds,)

    if ( 
        (user_guess =='rock' and program_pick =='scissors') or 
        (user_guess =='scissors' and program_pick =='paper') or 
        (user_guess =='paper' and program_pick =='rock')  
    ): 
        print('You won!')
        user_score = user_score + 1 
    elif (
        (user_guess =='rock' and program_pick =='rock') or 
        (user_guess =='scissors' and program_pick =='scissors') or 
        (user_guess =='paper' and program_pick =='paper')
    ) :
        print ('its a tie!') 
    else:
        print('you lost this round')
        computer_score = computer_score + 1

#final results
print("Game over!")
if user_score > computer_score:
    print("You win the game!")
elif user_score < computer_score:
    print("Computer wins the game!")
else:
    print("It's a tie !")
