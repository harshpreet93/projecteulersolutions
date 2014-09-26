from numpy import matrix
from numpy import linalg
openfile=open("p11input.txt")
arr=[]
for i in openfile:arr.append(i.split())
matrix=matrix(arr)
matrix=matrix.reshape(20,20)
print matrix