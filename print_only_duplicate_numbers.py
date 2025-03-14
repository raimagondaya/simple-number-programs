


print("Enter 10 numbers:")

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

duplicates = sorted(set(num for num in numbers if numbers.count(num) > 1))

print("Numbers with duplicates:", duplicates)
