#ask user to input float nnumbers
#check if given value is valid
#if equal print "equal try again"
#else print "not equal"
#same as the equal code in batch 1

def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Retry")

num1 = get_valid_input("1st number: ")
num2 = get_valid_input("2nd number: ")

if num1 == num2:
    print("equal, we're looking for not equal so try again.")
else:
    print("Not Equal")