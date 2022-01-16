import math
num = input('Calculate number of decimal places upto which you want to calculate the value of PI: ')
print('The value of PI upto {n} decimal places is {0:.{n}f}'.format(math.pi, n=num))