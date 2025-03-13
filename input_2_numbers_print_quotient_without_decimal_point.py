#import math
# ask user to input float numbers
#check if given value is valid
#quotient = round up to whole number(num1 // num2)
#print "the quotient is <quotient>"
import math

def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

print("We'll divide the two numbers you're going to input. The quotient will be rounded up so it won't have any decimal places.")
num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

if num2 != 0:
    quotient = math.ceil(num1 / num2) #math.ceil instead of int so the result would still be accurate
    print("The quotient is", quotient)
else:
    print("undefined.")