from random import randint
from art import logo
EASY_LEVELS = 10
HARD_LEVELS = 5


def check_answer(player_guess, answer, turns):
  """Check answer against guess. Returns the number of turns remaining."""
  if player_guess > answer:
    print("Too HIGH!")
    return turns -1
  elif player_guess < answer:
    print("Too LOW!")
    return turns -1
  else:
    print(f"YOU GOT IT! The answer is {answer}")

def check_difficulty():
  global turns
  level = input("Choose a difficulty. Type 'easy' or 'hard' and let's START: ")
  if level == "easy":
    print("You have 10 attempts to guess the number.")
    return EASY_LEVELS
  else:
    print("You have 5 attempts to guess the number.")
    return HARD_LEVELS


def game():
  print(logo)
  print("Welcome to the Lottery Game!")
  print("Guess what is the number between 1 and 100?")
  
  answer = randint(1, 100)
  turns = check_difficulty()
  
  player_guess = 0
  while player_guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
  
    turns = check_answer(player_guess, answer, turns)
    if turns == 0:
      print("You don't have any attempts.YOU LOSE!")
      return
    elif player_guess != answer:
      print("Guess again: ")
game()
