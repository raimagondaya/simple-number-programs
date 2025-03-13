#Start
#Declare set numbers
#loop stop when invalid input
#get number
#print "duplicate" if in numbers
#else print "unique" and add to numbers
#Stop

print("Enter numbers continuously. Input stops when an invalid entry is detected.")

numbers = set()
while True:
    try:
        num = int(input("Enter a number: "))
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers.add(num)
    except ValueError:
        print("Invalid value. Stopping input.")
        break
