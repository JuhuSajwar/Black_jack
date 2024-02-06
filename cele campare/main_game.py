from art import *
from data import data
import random 
import os

print(logo)

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_acc_data():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check(guess , acc1 , acc2):
    if acc1 > acc2:
        return guess == "a"
    else:
        return guess == "b"
    
        
acc1 = random_acc_data()
acc2 = random_acc_data()
  
score = 0
game_of_followers = True

while game_of_followers :
    acc1 = acc2
    acc2 = random_acc_data()
    
    if acc1 == acc2:
        acc2 = random_acc_data()   
    
    print(format_data(acc1))
    print(vs)
    print(format_data(acc2))
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = acc1["follower_count"]
    b_follower_count = acc2["follower_count"]
    is_correct = check(guess, a_follower_count, b_follower_count)
    
    clear_output()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_of_followers = False
      print(f"Sorry, that's wrong. Final score: {score}")
       
    
