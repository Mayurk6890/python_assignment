# Practical Example 3: Write a Python program to find a specific string in the list using a simple
#                      for loop and if condition

list = ['apple','banana','mango','cherry','strawberry']

found = False

for i in list:
    string = input("Enter the string to search: ")
    if i == string:
        print(f"{string} this string found in list")
        found = True 
    else:
        print("not found")