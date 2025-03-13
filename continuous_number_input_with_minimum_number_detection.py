#Start
#Declare set numbers
#loop stop when invalid input
#get number and store in list
#print minimun number in list
#Stop

print("Enter numbers continuously. Input stops when an invalid entry is detected.")

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    print("Stopping input with invalid value. Lowest number is:", min(numbers))
else:
    print("No valid numbers entered.")
