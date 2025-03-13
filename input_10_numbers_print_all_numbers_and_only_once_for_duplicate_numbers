#start
#prompt user to input 10 numbers
#check if the value is valid
#declare it to a list
#track for unique numbers
#track for numbers with duplicate and make them only appear once
#print unique numbers and only one of the duplicate numbers

print("Input any 10 numbers and we will print all of them. For numbers with duplicates, only the first entry will be printed.")

numbers = []
seen = set()
ordered_unique = []

for i in range(10):
    while True:
        try:
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
            if num not in seen:
                ordered_unique.append(num)
                seen.add(num)
            break
        except ValueError:
            print("Please enter a valid number.")

print("Numbers entered:", ordered_unique)
