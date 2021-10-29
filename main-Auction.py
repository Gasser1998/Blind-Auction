from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)


biddings = {

}

def biddings_add(name, bid):
  biddings[name] = bid

def get_key(val):
    for key, value in biddings.items():
         if val == value:
             return key

def find_bidder(biddings):
  x = 0
  y = ''
  for bidder in biddings:
    bid_amount = biddings[bidder]
    if x < bid_amount:
      x = bid_amount
      y = bidder
  print(F"${x} is the highest bid by {y}.")


should_end = False
while not should_end:
  name = input("What's your name? ")
  bid = int(input("What would you like to bid? "))
  biddings_add(name, bid)
  restart = input('Would anyone else like to bid? ')
  clear()
  if restart == 'no':
    should_end = True
    find_bidder(biddings)






print("Thank you, Goodbye.")


    
print(biddings.items())


#different way of solving:
# max_bid = max(biddings.values())
# max_name = get_key(max_bid)
#print(F"${max_bid} is the highest bid by {max_name}.")


