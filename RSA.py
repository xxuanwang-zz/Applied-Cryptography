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

    
def FastPower(g, x, p):
    
    result = 1
    while x > 0:
        if x % 2 == 1:
            result = result * g % p 
        g = g ** 2 % p
        x //= 2
    return result

def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ext_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q

def RSA_Bob(N, e):
    message = open('message.txt', "r") # Read the message from files
    line = ''
    for newline in message.readlines():
        line = line + str(newline)  # Read the text and turn the text into individual characters
    message.close()
    c_list = [] # Use to place the later result
    if len(line) > len(str(N)): # Condition 1
        text_list = split_text(line, N) # Split the message into smaller strings
        for i in range(len(text_list)): # Traverse the elements in the list
            m = msg2int(text_list[i]) # Convert the element into int
            c = FastPower(m, e, N)
            c_list.append(c) # Put the encryption result into the list
        return c_list
    else: # Condition 2
        m = msg2int(line)
        c = FastPower(m, e, N)
        c_list.append(c)
        return c_list
    
def split_text(line, N): # Split the string into smaller strings
    split_list = []
    num = len(line) // len(str(N)) # The number of N's in line
    num = num * 10 # The number of chunks
    total = len(line) // num # Use index to get each chunks

    for i in range(0, num):
        tmp = line[(i * (total + 1)) : ((total + 1) * (i + 1))]
        split_list.append(tmp)
            
    return split_list

def RSA_Alice():
    text = open('input.txt', "r")
    line = ''
    for newline in text.readlines():
        line = line + str(newline)  # Read the text and turn the text into individual characters
    text.close()
    line = line.split()
    # ## Read lines from the file
    p = int(line[0])  
    q = int(line[1])
    e = int(line[2])
    N = p * q # Key creation
    phi = (p-1)*(q-1)
    _, d, _ = ext_gcd(phi, e) # Generate d use the Extended Euclid algorithm
    if d < 0:
        d = d + phi
    Cyphertext = RSA_Bob(N, e) #Encrypt the message
    
    Plaintext = []
    for i in range(len(Cyphertext)):
        plaintext = int2msg(FastPower(Cyphertext[i], d, N)) # Decrypt the cyphertext
        plaintext = ''.join(plaintext)
        Plaintext.append(plaintext)
    Plaintext = ''.join(Plaintext)    
    print("RSA_Alice", Plaintext)

   
RSA_Alice()
