from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(f"{logo}\n")
print("Welcome to the secret auction program.")

bids = {}
bidding_is_finished = False

def find_highest_bid(bidding_record):
  highest_bid = 0
  winner = ""
  for each_bid in bidding_record:
    bid_amount = bidding_record[each_bid]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = each_bid
  print(f"The winner is {winner} with a bid of ${highest_bid}!")

while not bidding_is_finished:
  name = input("What is your name?\n")
  your_bid = int(input("What is your bid?\n$"))
  bids[name] = your_bid
  ask_to_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if ask_to_continue == "no":
    bidding_is_finished = True
    find_highest_bid(bids)
  elif ask_to_continue == "yes":
    clear()
  



