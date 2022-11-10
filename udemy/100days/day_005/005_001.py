# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# print("The non-correct way but lets play:")
# number_of_students = len(student_heights)
# total_height = sum(student_heights)
# average_height = round((total_height  / number_of_students),1)
# print(f"Average height is --> {average_height}")

total_height = 0
for height in student_heights:
    total_height += height
# print(total_height)

student_count = 0
for student in student_heights:
    student_count += 1
# print(student_count)

average_height = round(total_height / student_count)
print(f"{average_height}")
