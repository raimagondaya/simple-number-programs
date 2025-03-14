#start
#user input 10 times
#validate if input is valid
#store num on list
#store duplicates on list
#loop until 10 input
#print duplicate numbers
#end

print("Input 10 numbers and we will print those numbers that has duplicates.")

print("Enter 10 numbers:")

numbers = []
for i in range(10):
    while True:
        try:
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

duplicates = sorted(set(num for num in numbers if numbers.count(num) > 1))

print("Numbers with duplicates:", duplicates)
