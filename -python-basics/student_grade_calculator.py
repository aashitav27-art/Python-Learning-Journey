student_name = input("Enter student name: ")

math = float(input("Enter Math marks: "))
science= float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = math + science + english
percentage = total / 3


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("\n----- Student Result -----")
print("Name:", student_name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)