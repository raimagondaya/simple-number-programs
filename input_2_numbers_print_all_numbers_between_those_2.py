#ask the user to input 2 numbers
#check if value input is valid
#determine smaller and largest number
#print all numbers in between

def get_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid number.")

num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

print("Numbers in between", num1, "and", num2, "are:")
for num in range(min(num1, num2) + 1, max(num1, num2)):
    print(num)
