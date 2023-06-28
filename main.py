# import the logo

from art import logo
from art import vs

from random import randint
from gamedata import data

# print logo
print(logo)


# generate first random for data

def random_number():
  rand_index = randint(0, len(data) - 1)
  return rand_index

# print data for compare
def random_data(number, str):
  rand_data = data[number]
  data_output = f"{str}: {rand_data['name']}, {rand_data['description']} from {rand_data['country']}"
  print(data_output)
  return rand_data

  


# ask user for input  "Who has more followers? Type "A" or "B"


# condition
count = 0
keep_playing = True
# if a: check if a is greater for the value in data then add score by 1 and print "You're correct, your score is"

while keep_playing:
  compare_value = random_data(random_number(), "Compare A")
  # print logo "vs"
  print(vs)
  #print data for against
  vs_value = random_data(random_number(), "Against B")
  user_guess = input("\n\nWho has more followers? Type \"A\" or \"B\": ").upper()
  if user_guess == 'A' and compare_value["follower_count"] >  vs_value["follower_count"]:
    count += 5
    print(f"\nCorrect!, Your score is {count} \n\n\n\n")
  else:
    keep_playing = False
    print(f"Sorry, that's wrong. Final score is {count}")
  


# else: Output: Sorry, that's wrong. Final score is

# Start code