#ask the user to input 10 numbers
#make sure input is valid
#use try-except blocks
#enter num 1 - 10 using loop
#total = (num 1 - 10)
#print total

print("Enter 10 numbers and we will add all of them and print the sum:")

total = 0

for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            total += num
            break
        except ValueError:
            print("Enter a valid number.")

print(f"The sum is: ", total)
