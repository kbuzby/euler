import math
def binstr(n):
	str = []
	while n >= 2:
		str.insert(0, math.floor(n%2))
		n /= 2
	str.insert(0,math.floor(n))
	return str

def ispalindrome(n):
        if n==n[::-1]:
                return True
        else:
                return False

ans = 0
for x in range(1,1000000):
        if ispalindrome(str(x)):
                print(x)
                bins = binstr(x)
                if ispalindrome(bins):
                        print(bins)
                        ans += x
	
print(ans)
