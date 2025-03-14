#start
#enter numbers continuously until invalid input
#store numbers in list
#loop until invalid input
#compute average of numbers in list
#print computed average
#end

print("Enter numbers continuously. Input stops when an invalid entry is detected.")

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    average = sum(numbers) / len(numbers) 
    print("Average of all the entered numbers:", average)
else:
    print("No valid numbers entered.")
