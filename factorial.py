import sys
#function definition
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

#prompt user to input integer
print('Enter integer')
n = int(input())
if n <0:                            #declines negative integers
    print('Positive integers only') 
    sys.exit
else:                               #accepts positive integers 
    display = factorial(n)
    print('Factorial of ' + str(n) + ' is ' + str(display))