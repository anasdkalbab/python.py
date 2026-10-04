import sys

number_of_colomns = int(input())
user_input = input("Enter numbers separated by spaces: ")
number = [int(x) for x in user_input.split()]
number = sorted(number)
number = int(number)
print(number)
