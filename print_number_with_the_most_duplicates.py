#start
#enter numbers continuously until invalid input
#store numbers in list
#loop until invalid input
#find numbers with the most duplicates
#print num with theh most duplicate number
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
    most_frequent = max(set(numbers), key=numbers.count)
    print("Number with the most duplicates:", most_frequent)
else:
    print("No valid numbers entered.")
