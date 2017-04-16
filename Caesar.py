def encrypt(shift, msg):
    enc_msg = ''
    for letter in msg:
        if ord(letter) in range(ord('a'), ord('z')+1):
            enc_msg += chr((ord(letter)-ord('a')+shift)%(ord('z')-ord('a')+1)+ord('a'))
        elif ord(letter) in range(ord('A'), ord('Z')+1):
            enc_msg += chr((ord(letter)-ord('A')+shift)%(ord('Z')-ord('A')+1)+ord('A'))
        else:
            enc_msg += letter
    return enc_msg


def decrypt(shift, msg):
    dec_msg = ''
    for letter in msg:
        if ord(letter) in range(ord('a'), ord('z')+1):
            dec_msg += chr((ord(letter)-ord('a')-shift)%(ord('z')-ord('a')+1)+ord('a'))
        elif ord(letter) in range(ord('A'), ord('Z')+1):
            dec_msg += chr((ord(letter)-ord('A')-shift)%(ord('Z')-ord('A')+1)+ord('A'))
        else:
            dec_msg += letter
    return dec_msg


def crack(msg):
    cracked = []
    for letter in range(ord('z')-ord('a')+1):
        cracked.append(encrypt(letter,msg))
    return cracked


def full_encrypt(shift, msg):
    enc_msg = ''
    for character in msg:
        enc_msg += chr((ord(character)+shift)%128)
    return enc_msg


def full_decrypt(shift, msg):
    dec_msg = ''
    for character in msg:
        dec_msg += chr((ord(character)-shift)%128)
    return dec_msg


def full_crack(msg):
    output = []
    for character in range(128):
        output.append(full_encrypt(character,msg))
    return output


def live_encrypt(shift):
    enc_msg = ''
    print 'Enter message to encrypt:'
    while True:
        msg = str(raw_input())
        if msg == 'exit()': break
        out = encrypt(shift, msg)
        enc_msg += out
        print out
    return enc_msg


def live_decrypt(shift):
    dec_msg = ''
    print 'Enter message to decrypt:'
    while True:
        msg = str(raw_input())
        if msg == 'exit()': break
        out = decrypt(shift, msg)
        dec_msg += out
        print out
    return dec_msg


def main():
    shift = int(raw_input('Enter shift factor:\n'))
    msg = str(raw_input('Enter your Message:\n'))
    enc_msg = encrypt(shift, msg)
    dec_msg = decrypt(shift, enc_msg)
    cracked = crack(msg)

    print 'Your encrypted message is:\n' + enc_msg + '\n\n'
    print 'Your decrypted message is:\n' + dec_msg + '\n\n'
    print 'All possibilities:'
    for msg in cracked:
        print msg


if __name__ == '__main__':
    main()
    #print live_encrypt(3)
    #print live_decrypt(3)