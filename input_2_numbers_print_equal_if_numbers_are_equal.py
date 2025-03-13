#ask user to input float nnumbers
#check if given value is valid
#if equal print "Equal"
#else print "not equal"

def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

if num1 == num2:
    print("Equal")
else:
    print("Not equal")