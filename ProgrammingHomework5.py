

##from math import sqrt
##
##def f(x) :
##	return g(x) + sqrt(h(x))			  
##def g(x) :
##	return 4 * h(x)			  
##def h(x) :
##	return x * x + k(x) - 1	
##def k(x) :
##     return 2 * (x + 1) 
##
##
##x1 = f(2)
##print("x1 = " , x1)
##
##x2 = g(h(2))
##print("x2 = " , x2)
##
##x3 = k(g(2) + h(2))
##print("x3 = " , x3)
##
##x4 = f(0) + f(1) + f(2)
##print("x4 = ", x4)
##
##x5 = f(-1) + g(-1) + h(-1) + k(-1)
##print("x5 = " , x5)



#Programming Exercises

##length = len("black boxes")
##
##print(length)




# Joshua Edwards
# CSC 119 Sec. 2H2
# Professor Deherrera
# 8 April 2021


#Returns the first digit of the argument
n = input("Enter a number: ")

def firstDigit(n):
    string = str(n)
    first = int(string[0])
    return first

print("The first digit of that number is ", firstDigit(n))




#Returns the last digit of the argument
n = int(input("Enter a number: "))

def lastDigit(n):
    
    return n % 10 

print("The last digit of that number is " , lastDigit(n))




#Returns the number of digits in the argument
n = input("Enter a number: ")

def digits(n):
    length = len(n)
    return length

print("The amount of digits in the number you entered is " , digits(n))









