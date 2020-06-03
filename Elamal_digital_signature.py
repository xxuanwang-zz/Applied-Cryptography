import random
def fastPower(g, A, N):
    a = g
    b = 1
    while A > 0:
        if A % 2 == 1:
            b = (b * a) % N
        a = (a * a) % N 
        # print (a)
        A = A // 2
    # print (b)
    return b

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
   
def int2bin(integer):
        binString = ''
        while integer > 0:
                mod = integer % 2
                binString = str(mod) + binString
                integer //= 2
        while len(binString) % 8 != 0:
                binString = '0' + binString
        return binString


def bin2intlong(binary):
        total = 1
        for place in range(len(binary) - 1, 0, -1):
                tempvalue = int(binary[place])
                total += tempvalue * (2 ** (place))
        return total


def bin2int(binary):
        return int(binary, 2)


def msg2bin(message):
        return ''.join(['{0:08b}'.format(ord(x)) for x in message])


def bin2msg(binary):
        return ''.join(chr(int(binary[(i * 8):(i * 8 + 8)], 2)) for i in range(len(binary) // 8))


def msg2int(message):
        return bin2int(msg2bin(message))


def int2msg(integer):
        return bin2msg(int2bin(integer))


def MsgSenderBob():
    message = open('input.txt', "r")
    line = ''
    for newline in message.readlines():
        line = line + str(newline)  # Read the text and turn the text into individual characters
    message.close()
    line = line.split()
    # # The following part is key creation part
    p = int(line[0])  # p is a large prime number
    g = int(line[1])  # g is the generator
                      # p, g are public parameters
    b = random.randint(2, p-2) # b is Bob's private key
    
    Kpub = fastPower(g, b, p) # Kpub is Bob's public verification key
    message = 'Elgamal digital signature algorithm' # Message that Bob' would like to send to Alice.
                                                    # m is in the range(1, p-2)
                                                    # Also can use Hash function to get the digital digest
                                                    # if the message is too long
    msg = msg2int(message)  # # Convert the string into integer variable
    Ke = 1  # The following part is the signing section 
    r = fastPower(g, Ke, p)
    while Ke == random.randint(0, p-2): # # Select a random integer ephemeral key
        if gcd(Ke, p - 1) != 1:
            Ke = random.randint(0, p-2)
        
    Gcd = gcd(Ke, p - 1 )
    if Gcd == 1:  # Determine if there is a multiplicative inverse
                  # If two numbers are mutually prime, the value of their greatest common divisor is 1
                  # Thus, multiplicative inverses exist between two numbers
        x, y = Extended(Ke, p - 1)
        x = x % (p - 1)  # The multiplicative inverse should be an integer
        y = y % Ke  # Use '%' to convert the result into an integer
    s = (msg - b * r) * x % (p - 1) # r and s are two signature parameters 
                                    # Notice s modulo (p - 1), that's because for Alice during the verification process
                                    # s will be an exponent of g
                                    #so we can replace s by any quality that is congruent to s modulo (p - 1)
            
    # ## Write all the variables to the 'signatureinfo.txt' file in line
    output = open("signatureinfo.txt", "w")
    output.write (str(p))
    output.write ('\n')
    output.write (str(g))
    output.write ('\n')
    output.write (str(Kpub))
    output.write ('\n')
    output.write (str(r))
    output.write ('\n')
    output.write (str(s))
    output.write ('\n')
    output.write (str(msg))
    output.write ('\n')
    output.close ()
    
MsgSenderBob()

def MsgReceiverAlice(): 
    message = open('signatureinfo.txt', "r")
    line = ''
    for newline in message.readlines():
        line = line + str(newline)  # Read the text and turn the text into individual characters
    message.close()
    line = line.split()
    # ## Read lines from the file which provided by Bob
    p = int(line[0])  
    g = int(line[1])
    Kpub = int(line[2])
    r = int(line[3])
    s = int(line[4])
    msg = int(line[5])
    # # Alice verifies the signature by computing the following values
    t = fastPower(Kpub, r, p) * fastPower(r, s, p) % p # Compute the value of t
    T = fastPower(g, msg, p) # Compute the value of T
    #print(t, T)
    if t == T:
        print("Your message is safe!")
    elif t != T:
        print("Your message has been tempered with")
    
MsgReceiverAlice()


