#for num from 0 to 100
#if num divisible by 10 and 5, with a remainder not zero: print num

for num in range(101):
    if num % 10 != 0 and num % 10 != 5:
        print(num)
