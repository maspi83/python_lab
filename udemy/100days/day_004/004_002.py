import random
coin = int(random.randint(0, 1))
if coin == 0:
    coin_translate = "Heads"
elif coin == 1:
    coin_translate = "Tails"

print (f"{coin_translate}")