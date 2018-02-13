overtimerate = 1.5

import sys

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter number')
    sys.exit(1)
    
    
hours = float(input('Enter Hours'))
rate = float(input('Pay Rate'))
overtimerate = 1.5

def computepay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        hours = overtime
        overtimepay = overtime * rate * overtimerate
        return(hours * rate) + overtimepay
    else:
        return(hours * rate)


print(computepay(hours, rate))