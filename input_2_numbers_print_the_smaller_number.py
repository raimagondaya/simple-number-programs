#ask user to input float nnumbers
#check if given value is valid
#if num1 < num 2: print "<num1> is smaller than <num 2>'
#ifelse num 2 < num 1: "<num2> is smaller than <num1>"
#else: print "they're the same, no amount is smaller"

def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

print("input two numbers and we'll print what's smaller")
num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

if num1 < num2:
    print(num1, "is smaller")
elif num2 < num1:
    print(num2, "is smaller")
else:
    print("The two numbers are the same, no smaller value")
