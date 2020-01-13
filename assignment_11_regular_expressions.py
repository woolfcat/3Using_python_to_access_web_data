'''
In this assignment you will read through and parse a file with text and numbers.
You will extractall the numbers in the file and compute the sum of the numbers.
'''

import re
fname=input('enter file name:')
fh=open(fname)
numlist=list()
sum=0
for l in fh:
    l=l.rstrip()
    num=re.findall('[0-9.]+',l)
    numlist=numlist+num
for n in numlist:
    m=float(n)
    sum=sum+m
print(sum)
