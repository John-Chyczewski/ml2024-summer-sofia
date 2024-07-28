# Ask the user for input N positive integers
N = int(input("Please input a positive integer N: "))

# Initialize an empty list
numbers = []

# Ask the user to provide N numbers (one by one) and read them
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

X = int(input("Enter an integer X: "))

# Check if X is in the list of numbers
if X in numbers:
    # Output the index (from 1 to N) of X
    index = numbers.index(X) + 1
    print(f"The index of {X} is: {index}")
else:
    # Output -1 if X is not in the list
    print("-1")
