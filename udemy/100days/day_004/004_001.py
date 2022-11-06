import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = int(random.randint(0, 2))
print(game_images[computer_choice])

if user_choice == computer_choice:
    print("Its a draw")
elif user_choice > computer_choice != "0":
    print("You WIN")
elif user_choice == "2" and computer_choice == "0":
    print("Computer WINs")
elif user_choice < computer_choice and user_choice != "0":
    print("Computer WINs")
elif user_choice < computer_choice and user_choice == "0":
    print("You WINs")

elif computer_choice > user_choice != "0":
    print("Computer WINs")
elif computer_choice == "2" and user_choice == "0":
    print("You WINs")
elif computer_choice < user_choice and computer_choice != "0":
    print("Computer WINs")
elif computer_choice < user_choice and computer_choice == "0":
    print("You WINs")