# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
names = name1 + name2
count_t = names.count('t')
count_r = names.count('r')
count_u = names.count('u')
count_e = names.count('e')
count_l = names.count('l')
count_o = names.count('o')
count_v = names.count('v')
count_true = count_t + count_r + count_u + count_e
count_love = count_l + count_o + count_v + count_e

true_love_count = int(f"{count_true}{count_love}")

if true_love_count < 10 or true_love_count > 90:
    print(f"Your score is {true_love_count}, you go together like coke and mentos.")
elif 40 < true_love_count < 50:
    print(f"Your score is {true_love_count}, you are alright together.")
else:
    print(f"Your score is {true_love_count}.")
