#ask user to input float numbers
#check if given value is valid
#quotient = num1 * num2
#print "the quotient is <quotient>"
def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

print("We'll divide the two numbers you're going to input")
num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

if num2 != 0:
    quotient = num1 / num2
    print("The quotient is", quotient)
else:
    print("undefined.")