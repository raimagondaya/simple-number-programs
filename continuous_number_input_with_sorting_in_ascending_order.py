#start
#declare empty number list
#loop until invalid input
#ask user for numbers
#store numbers in list
#sort numbers in ascending order
#print arranged numbers

print("Enter numbers continuously. Input stops when an invalid entry is detected.")

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    numbers.sort()
    print("Numbers in ascending order:", numbers)
else:
    print("No valid numbers entered.")
