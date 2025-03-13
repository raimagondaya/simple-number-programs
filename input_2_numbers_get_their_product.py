#ask user to input float numbers
#check if given value is valid
#product = num1 * num2
#print "the product is <product>"

def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

print("We'll multiply the two numbers you're going to input")
num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

product = (num1 * num2)
print("The product of the two numbers is", product)
