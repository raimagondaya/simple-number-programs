#ask user to input float numbers
#check if given value is valid
#difference = num1 - num2
#print "the difference is <difference>"

def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

print("We'll subtract the two numbers you're going to input")
num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

difference = (num1 - num2)
print("The difference of the two numbers is", difference)
