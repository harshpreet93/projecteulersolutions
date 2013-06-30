import time
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#sieve method returns a list of all primes from 2 to the upperbound. The list
#also contains empty indexes, they can be ignored
def sieve(upperbound):
	plist=[]
	for i in range(0,upperbound+1):plist.append(i)
	for j in range(2,int(len(plist)**0.5)):
		if(plist[j]!=0):
			for k in range((2*j),len(plist),j):
				if(plist[k]!=0):plist[k]=0
	return plist[2:]
start=time.clock()
primelist= sieve(2000000)
sum=0
for i in primelist:sum+=i
elapsed=(time.clock()-start)
print str(sum)+" finished in "+str(elapsed)+" seconds"