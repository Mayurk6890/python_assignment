#  Practical Example 7: Write a Python program to calculate grades based on percentage using
#                       if-else ladder.

marks = int(input("Enter your marks : "))

if marks<=100:
    if marks >= 60:
        print("A grade")
    elif marks >= 45 and marks < 60:
        print("B grade")
    elif marks >= 33 and marks < 45:
        print("C grade")
    else:
        print("fail")
else:
    print(" Invalid marks ")
