#user input 10 numbers
#for loop from num1 - num10
#check if num n is divisible by 2
#if yes, add to the even number count
#repeat until reaching num 10
#print "there are <even number counted> even numbers"

print("You will input 10 numbers, and the program will count how many of those numbers are even.")

even_numbers = 0

for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))  
            if num % 2 == 0:
                even_numbers += 1
            break
        except ValueError:
            print("Enter a valid number.")

print(f"There are {even_numbers} even numbers")
