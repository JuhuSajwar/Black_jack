import random

word_list = ['juhu','bharat','harshita']

chosen_word = random.choice(word_list)

lives = 6

display = []
for _ in range(len(chosen_word)):
    display+='_'
print(display)    

end_of_game = False

while not end_of_game :
    guess = input("guess a letter :").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose. The word was", chosen_word)
        end_of_game =True
        print("you lose")         
    
    print(display)
    
    if '_' not in display :
        end_of_game =True
        print("you win")    
            