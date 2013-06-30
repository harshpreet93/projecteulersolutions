#Which starting number, under one million, produces the longest chain?
import time
def chainLen(num):
	chain=[]
	while(num!=1):
		if(num%2==1):
			num=(3*num)+1
			chain.append(num)
		else:
			num=num/2
			chain.append(num)
	return len(chain)+1
greatest=10
result=0
start=time.clock()
for i in range(14,1000001):
	chainlength=chainLen(i)
	if(chainlength>greatest):
		greatest=chainlength
		result=i
elapsed=time.clock()-start
print str(result)+" finished in "+str(elapsed)+" seconds"