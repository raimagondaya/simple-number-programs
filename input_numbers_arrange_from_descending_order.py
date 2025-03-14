#start
#enter numbers continuously until invalid input
#store numbers in list
#loop until invalid input
#sort numbers
#print arranged numbers
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
    numbers.sort(reverse=True)  # Sort numbers in descending order
    print("Numbers from highest to lowest:", numbers)
else:
    print("No valid numbers entered.")
