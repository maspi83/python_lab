#If the bill was $150.00, split between 5 people, with 12% tip. 
print ("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
calculate = (bill + (bill * (tip / 100))) / people
roud_calculate = round(calculate, 2)
print ("Solution 1 - using str")
print ("Each person should pay: $" + str(roud_calculate))
print ("Solution 2 - using function")
print (f"Each person should pay: ${roud_calculate}")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

