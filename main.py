# import the logo, vs, random interger and data from available file

from art import logo
from art import vs

from random import randint
from gamedata import data

# print logo
print(logo)


# function to generate first random for data

def random_number():
  rand_index = randint(0, len(data) - 1)
  return rand_index

# function for data output and index call
def random_data(number, str):
  rand_data = data[number]
  data_output = f"{str}: {rand_data['name']}, {rand_data['description']} from {rand_data['country']}"
  print(data_output)
  return rand_data

# count score
count = 0

# true when still in game
keep_playing = True

while keep_playing:
  # print data for compare
  compare_value = random_data(random_number(), "Compare A")
  
  # print logo "vs"
  print(vs)
  
  #print data for against
  vs_value = random_data(random_number(), "Against B")
  
  # ask user for input  "Who has more followers? Type "A" or "B"
  user_guess = input("\n\nWho has more followers? Type \"A\" or \"B\": ").upper()

  # Condition
  
  # if a: check if a is greater for the value in data then add score by 1 and print "You're correct, your score is"
  if user_guess == 'A' and compare_value["follower_count"] >  vs_value["follower_count"]:
    # score increases by 5
    count += 5
    print(f"\nCorrect!, Your score is {count} \n\n\n\n")
  else:
    # else: Output: Sorry, that's wrong. Final score is
    # game ends by False
    keep_playing = False
    print(f"Sorry, that's wrong. Final score is {count}")

# End code