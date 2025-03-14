#start
#enter numbers continuously until invalid input
#store numbers in list
#loop until invalid input
#find the highest number
#print highest number
#end

print("Enter numbers continuously. It will stop if there's invalid input.")

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    print("Highest number entered:", max(numbers))
else:
    print("No valid numbers entered.")