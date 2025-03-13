#Ask user to input 10 numbers
#store the numbers in a list
#set the first number as the starting value
#num1 - num2 to num10
#print result

def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

print("Input 10 numbers. The program will subtract all the numbers from the first number.")

numbers = []
for i in range(10):
    numbers.append(get_valid_input(f"Enter number {i+1}: "))

result = numbers[0]
for num in numbers[1:]:
    result -= num

print("The result is: ", result)
