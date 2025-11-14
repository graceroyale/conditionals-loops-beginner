# This line of codes prompts the user for a number n and prints all numbers from n to 1.
n = int(input("Enter a number: "))
while n < 1:
    n = int(input("Please enter a positive integer greater than 0: "))
for i in range(n, 0, -1):
    print(i)
