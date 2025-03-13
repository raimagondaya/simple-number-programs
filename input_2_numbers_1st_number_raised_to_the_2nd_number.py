#ask user to input float numbers
#check if given value is valid
#result = num1 ** num2
#print "the result is <result>"
def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

print("We'll raise the 1st number you're going to input to the power of the second number you will input. ")
num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

result = (num1 ** num2)
print("The result is", result)
