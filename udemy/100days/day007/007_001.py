word_list = ["pes","macka","kacka","krava","koza"]
import random
random_choice = random.choice(word_list)
print (random_choice)
guess = input("Guess a letter: ").lower()
#print (guess)

# guess = input("Guess a letter: ").lower
for letter in random_choice:
    if letter == guess:
        print ("Right")
    else:
        print ("Wrong")