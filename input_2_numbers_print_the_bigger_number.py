#pseudocode ig
#ask user to input float nnumbers
#check if given value is valid
#if num1 > num 2: print "<num1> is bigger than <num 2>'
#ifelse num 2 > num 1: "<num2> is bigger than <num1>"
#else: print "they're the same, no amount is bigger"

print("input two numbers and we'll print what's bigger")
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else :
     print("The two numbers are the same, no bigger number")
