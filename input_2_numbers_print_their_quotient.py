#ask user to input float numbers
#check if given value is valid
#quotient = num1 * num2
#print "the quotient is <quotient>"

print("We'll divide the two numbers you're going to input")
num1 = float(input("1st number: "))
num2 = float(input("2nd number: "))

if num2 != 0:
    quotient = num1 / num2
    print("The quotient is", quotient)
else:
    print("no zeros, undefined.")