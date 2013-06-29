#A palindromic number reads the same both ways. The largest palindrome made 
#from the product of two 2-digit numbers is 9009 = 91 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def findPalindrome():
	palindromes=[]
	for i in range(999,99,-1):
		for j in range(999,99,-1):
			if(str(i*j) == str(i*j)[::-1]):palindromes.append(i*j)
	palindromes.sort()
	return palindromes[len(palindromes)-1]

print findPalindrome()
