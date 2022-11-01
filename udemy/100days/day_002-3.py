# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
age_int = int(age)
#Write your code below this line 👇
year_left = 90 - age_int
days_left = year_left * 365
week_left = year_left * 52
month_left = year_left * 12
print (f"You have {days_left} days, {week_left} weeks, and {month_left} months left")
