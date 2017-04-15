import Caesar

def encrypt(pwd, msg):
    enc_msg = ''
    for letter in range(len(msg)):
        enc_msg += Caesar.encrypt(ord(pwd[letter % len(pwd)].lower()) - ord('a'), msg[letter])
    return enc_msg


def decrypt(pwd, msg):
    dec_msg = ''
    for letter in range(len(msg)):
        dec_msg += Caesar.decrypt(ord(pwd[letter % len(pwd)].lower()) - ord('a'), msg[letter])
    return dec_msg


def main():
    pwd = str(raw_input('Enter your password:\n'))
    msg = str(raw_input('Enter your message:\n'))
    enc_msg = encrypt(pwd, msg)
    dec_msg = decrypt(pwd, enc_msg)

    print 'Your encrypted message is:\n' + enc_msg + '\n\n'
    print 'Your decrypted message is:\n' + dec_msg + '\n\n'


if __name__ == '__main__':
    main()