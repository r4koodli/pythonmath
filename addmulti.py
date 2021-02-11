""" Python to add and multiply given integers with condition """
import math
   
print('Enter value for a:')
a = int(raw_input().strip())
print('Enter value for b:')
b = int(raw_input().strip())
if (a*b < 1000):
  print('Product:', a*b)
else:
  print('Sum:', a+b)
