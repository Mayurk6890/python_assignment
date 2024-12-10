# Practical Example 8: Write a Python program to check if a person is eligible to donate blood
#                      using a nested if.

age = int(input("Enter your age: "))


if age>=18 and age<50:
    weight = int(input("Enter your weight: "))
    if weight>=50 and weight<100:
        print("You are eligible for blood donation ")
    else:
        print("You are not eligible blood donation ")
else:
    print("Your age is not appropriate for donating blood ")