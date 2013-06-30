#What is the sum of the digits of the number 2^1000?
result=0
for i in str(2**1000):result+=int(i)
print result