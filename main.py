# Print numbers from 1 to 10 using a loop.
for i in range(1,11):
    print(i)
print("--------------------------------------------")

# Print all even numbers between 1 and 20.
for i in range(0,21,2):
    print(i)
print("--------------------------------------------")

# Print the characters of the string "Python" one by one using a loop.
for i in "Python":
    print(i)
print("--------------------------------------------")

# Print the sum of numbers from 1 to 100.
a = 0
for  i in range (1,101):
    a+=i
print(a)
print("--------------------------------------------")

# Print multiplication table of 5 (like 5 x 1 = 5, ... 5 x 10 = 50).
for i in range (1,11):
    print (f"5 X {i} = {i*5}")
print("--------------------------------------------")

# Print all elements of a list using a loop.
# List: ["apple", "banana", "cherry"]
lst = ["apple", "banana", "cherry"]
for item in lst:
    print(item)
print("--------------------------------------------")

# Print only the vowels from the string "education" using a loop.
a = 'education'
for char in a:
    if char == 'a' or char == 'e' or char == 'i' or  char == 'o' or char == 'u':
        print(char)  
print("--------------------------------------------")

# Count how many times the letter 'a' appears in the string "banana" using a loop.
for char in "banana":
    p="banana".count("a")
print(p)
print("--------------------------------------------")

# Print numbers from 10 to 1 using a loop (reverse order).
for i in range (10,0,-1):
    print(i)
print("--------------------------------------------")

# Ask the user to enter 5 numbers using a loop and print their sum.
a = input("Enter 5 numbers separated by spaces: ")
b = list(map(int, a.split()))
sum_numbers = 0
for num in b:
    sum_numbers += num
print("Sum:", sum_numbers)
