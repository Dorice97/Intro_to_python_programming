#hangman game program

import random

word_list=["pajama", "peekaboo","exodus","fjord","flapjack", "flopping","funny", "galaxy", "gazebo", "gizmo",
    "glyph", "gnarly", "gossip","haphazard","hyphen", "icebox", "injury", "ivory", "jackpot","blizzard", 
    "boggle","wave","equip","abruptly","absurd"]

def get_word(word_list):
    return random.choice(word_list).upper()

def play(word):
    word_completion = "_" * len(word)
    guessed_letters = []
    trials = 0

 # Use a list for stages (simplified art here)
    hangman_stages = [
        "Stage 0",
        "Stage 1 (head)",
        "Stage 2 (body)",
        "Stage 3 (one arm)",
        "Stage 4 (two arms)",
        "Stage 5 (one leg)",
        "Stage 6 (two legs)"
    ]
    max_trials = len(hangman_stages) - 1

    print("Welcome, let's play hangman!")
    
#guess validation  
    while trials < max_trials and "_" in word_completion:
        try:
            guess = input("Guess a letter: ").upper()

            if guess!= guess.isalpha() or len(guess)!=1:
                print("invalid choice!")
                
            if len(guess) == 1 and guess in guessed_letters:
                print("You already guessed that letter.")

            elif guess not in word:
                print("Wrong guess!")
                trials = trials + 1
                guessed_letters.append(guess)
            else:
                print("Good job! Letter is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

                   
        except :
            print("validation error")

        print(hangman_stages[trials])
        print(word_completion)

    if "_" not in word_completion:
        print("You guessed the word:", word)
    else:
        print("You lost! The word was:", word)

play(get_word(word_list))











