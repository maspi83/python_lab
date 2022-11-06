# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count_string = len(names)
random_value = random.randint(0, count_string - 1)
plati = names[random_value]
print (f"{plati} is going to buy the meal today!")
