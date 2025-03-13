#Input 2 numbers
#ensure input value is valid
#num1 % num2
#print remainder

def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

print("Input two numbers and we'll print the remainder when the first number is divided by the second number.")

num1 = get_valid_input("1st  number (dividend): ")
num2 = get_valid_input("2nd number (divisor): ")

while num2 == 0:
    print("Division by zero is not allowed. Please enter a nonzero number.")
    num2 = get_valid_input("Enter the second number: ")

remainder = num1 % num2
print("The remainder is:", remainder)
