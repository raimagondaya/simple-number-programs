#begin
#Declare list
#Make user input 10 numbers and put in list
#Check if values entered are valid 
#Identify numbers that only appear once in the list
#print unique numbers
#end.

print("Input any 10 numbers and we will print those numbers that don't have any duplicates.")

numbers = []
for i in range(10):
    while True:
        try:
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Please enter a valid number.")

unique_numbers = [num for num in numbers if numbers.count(num) == 1]

print("Numbers that don't have duplicates:", unique_numbers)
