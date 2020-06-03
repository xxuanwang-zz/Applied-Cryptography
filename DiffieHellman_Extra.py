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


def DiffieHellman():
    message = open('input.txt', "r")
    line = ''
    for newline in message.readlines():
        line = line + str(newline)  # Read the text and turn the text into individual characters
    message.close()
    line = line.split()
    p = int(line[0])  

    b = int(line[2])
    A = int(line[3])
    
    cipher = bin2int(str(line[4]))  # # Convert 'cipher' into decimal
    key = fastPower(A, b, p)  # # Calculate the value of key
    k = fastPower(key, p - 2, p)  # # Calculate the inverse of the shared key mod p
    ciphertext = int2msg(k * cipher % p)  # # Decipher the ciphertext by multiplying k and cipher
                                         # # And then converting the result into readable English 
    
    print("The result is :", ciphertext)  # Convert the resulting binary string into plain English
    
    
DiffieHellman()

