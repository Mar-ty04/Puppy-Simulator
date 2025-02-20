#Marisol Morales & Andreas Moreno 5/6/2024 The puppy simulator game

import check_input
import puppy


def main():
#Puppy object is created and game loop starts 
  pup = puppy.Puppy()
  interacting = True
  print("You have a new puppy!")
  while interacting:
#Menu will be displayed that gives different actions for the user to give to the puppy 
    choice = check_input.get_int_range("What do you want to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit\nEnter choice: ", 1, 3)
#Given the choice, the puppy will or wont perform certain 
#actions depending on the state of the puppy
    if choice == 1:
      print()
      print(pup.give_food())
      print()
    elif choice == 2:
      print()
      print(pup.throw_ball())
      print()
    else:
      #If User wishes the quit the game loop will end 
      interacting = False

main()