import random

rock = '''
    ____ROCK___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ____PAPER___
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    ____SCISSORS___
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_ascii_images = [rock, paper, scissors]
choice = int(input("Choose wisely(0,1,2): "))
print(f"\nYou choice is:{game_ascii_images[choice]}")

computer_choice = int(random.randint(0,2))
print(f"\nComputer has chosen: {game_ascii_images[computer_choice]}")
