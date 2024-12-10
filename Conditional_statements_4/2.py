# Practical Example 6: Write a Python program to check if a number is prime using if_else.

num = int(input("Enter the number : "))

if num>1:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} The is not prime number")
            break
    else:
            print(f"{num} this is prime number : ")
else:
    print(f"{num} this is ot prime number ")