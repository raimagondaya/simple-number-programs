#user input 10 numbers
#for loop from num1 - num10
#check if num n is divisible by 2
#if yes, add to the odd number count
#repeat until reaching num 10
#print "there are <odd number counted> odd numbers"

print("You will input 10 numbers and the program will count how many of those numbers are odd.")

odd_numbers = 0

for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))  
            if num % 2 != 0:
                odd_numbers += 1
            break
        except ValueError:
            print("Enter a valid number.")

print(f"There are {odd_numbers} odd numbers")
