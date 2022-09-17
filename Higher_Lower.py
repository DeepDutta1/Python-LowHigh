from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  '''Takes the account data and return the printable format.'''
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc},from {account_country} "

def check_answer(guess, a_followers, b_followers):
  """take the user guess and follower counts and returns if they got it right. """
  if a_followers > b_followers:
        # if guess == 'a':
        #     return True
        # else:
        #     return False
    return guess == "a"
  else:
    return guess == "b"

#Display art
print(logo)
#score keeping
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
#generate a random account from the game data

  #making account au position B become the next account at position A.
  account_a = account_b
  account_b = random.choice(data)
    
  if account_a == account_b:
    account_b = random.choice(data)

  print(f"compare A: {format_data(account_a)}. ")
  print(vs)
  print(f"Against B: {format_data(account_b)}. ")

    #ask user for a guess.
  guess = input("who has more followers? Type 'A' or 'B' : ").lower

    #check if user is correct.
    ##get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #clear the screen between rounds.
  clear()
  print(logo)

    ## use if statement to check if user is correct.
    #give user feedback on their guess.
  if is_correct:
    score += 1
    print(f"You're right! Current score {score}. ")
  else:
    game_should_continue = False
    print(f"sorry, that's worng. final score: {score} ")






#making account at position B become the next the next account at position A.

