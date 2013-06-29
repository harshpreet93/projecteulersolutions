#2520 is the smallest number that can be divided by each of the numbers from 
#1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the 
#numbers from 1 to 20?
import time
def divisibility():
	start=time.clock()
	cases=[11,12,13,14,15,16,17,18,19]
	div=False
	check=2520*2
	while(div==False):
		counter=0
		for i in reversed(cases):
			#if(check%2520!=0):break
			if(check%i==0):counter+=1
			else:break
		if counter==len(cases):
			div=True
			elapsed=(time.clock()-start)
			return "the answer is "+str(check), "finished in "+str(elapsed)+" seconds"
		else:check+=2520

print divisibility()


