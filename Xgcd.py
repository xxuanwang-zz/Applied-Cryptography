'''
Created on 2019年10月28日

@author: DELL
'''
def gcd(a, b):  # Find the greatest common divisor 
    if a < b:
        gcd(b, a)
    # q = a // b
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

    
def Extended(a, b):  # Calculate the Extended Euclidean algorithm
                     # Using recursion method
    if b == 0:  # When the recursion reaches the boundary
                # the solution can be easily obtained
        return 1, 0
    else:
        x2, y2 = Extended(b, a % b)  # Other situations
        x1 = y2
        y1 = x2 - (a // b) * y2
        
        return x1, y1


def Inverse():
    message = open('input.txt', "r")
    line = ''
    for newline in message.readlines():
        line = line + str(newline)  # Read the text and turn the text into individual characters
    message.close()
    line = line.split()
    # ## Read lines from the file
    g = int(line[0])  
    m = int(line[1])
   
    if g < 0:
        g = abs(g)
    Gcd = gcd(g, m)
    if Gcd == 1:  # Determine if there is a multiplicative inverse
                  # If two numbers are mutually prime, the value of their greatest common divisor is 1
                  # Thus, multiplicative inverses exist between two numbers
        x, y = Extended(g, m)
        x = x % m  # The multiplicative inverse should be an integer
        y = y % g  # Use '%' to convert the result into an integer
        print("The result is :", x)  # Output the multiplicative inverse of g
    else :
        print("Do Not Have!")

    
Inverse()

