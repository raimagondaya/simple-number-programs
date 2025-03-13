#ask user to input float numbers
#check if given value is valid
#sum = num1 + num2
#print "the sum is <sum>"
def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

print("We'll add the two numbers you're going to input")
num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

sum = (num1 + num2)
print("The sum of the two numbers is", sum)
