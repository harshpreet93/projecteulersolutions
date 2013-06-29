#By considering the terms in the Fibonacci sequence whose values do not exceed 
#four million, find the sum of the even-valued terms.

#calculate the first n terms in the fibonacci sequence
def fib(n):
	result=[]
	result.append(1)
	result.append(2)
	i=2
	while(i<n):
		result.append(result[i-1]+result[i-2])
		i+=1
	return result
#get rid of odd numbers
def eliminateOdds(fibs):
	for i in range(len(fibs)):
		if(fibs[i]%2==1):fibs[i]=0
	return fibs
#get rid of big numbers
def eliminateBig(fibs):
	for i in range(len(fibs)):
		if (fibs[i]>4000000):fibs[i]=0
	return fibs
#sum up all the numbers in the list
def sum(fibs):
	sum=0
	for i in fibs:
		sum=sum+i
	return sum
smallfibs=fib(35)
#print smallfibs
smallfibs=eliminateOdds(smallfibs)
#print smallfibs
smallfibs=eliminateBig(smallfibs)
#print smallfibs
print sum(smallfibs)