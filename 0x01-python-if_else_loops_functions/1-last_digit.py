#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
outStr = 'Last digit of '
if number < 0:
    ld = -(ld)
if ld == 0:
	print(outStr + f"{number:d} is {ld:d} and is 0")
elif ((ld > 6) and (ld !=0)):
    print(outStr + f"{number:d} is {ld:d} and is less than 6 and not 0")
elif ld > 5:
    print(outStr + f"{number:d} is {ld:d} and is greater than 5")
