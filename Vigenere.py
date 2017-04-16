import Caesar


def encrypt(pwd, msg):
    enc_msg = ''
    for letter in range(len(msg)):
        enc_msg += Caesar.encrypt(ord(pwd[letter % len(pwd)].lower()) - ord('a')+1, msg[letter])
    return enc_msg


def decrypt(pwd, msg):
    dec_msg = ''
    for letter in range(len(msg)):
        dec_msg += Caesar.decrypt(ord(pwd[letter % len(pwd)].lower()) - ord('a')+1, msg[letter])
    return dec_msg


def brute(password_list, msg):
    output = []
    for password in password_list:
        output.append(decrypt(password,msg))
    return output


def live_encrypt(pw):
    enc_msg = ''
    print 'Enter message to encrypt:'
    i = 0
    while True:
        msg = str(raw_input())
        if msg == 'exit()': break
        msg_out = ''
        for j in range(len(msg)):
            msg_out += Caesar.encrypt(ord(pw[i%len(pw)].lower())-ord('a')+1, msg[j])
            i += 1
        enc_msg += msg_out
        print msg_out
    return enc_msg


def live_decrypt(pw):
    dec_msg = ''
    print 'Enter message to decrypt:'
    i = 0
    while True:
        msg = str(raw_input())
        if msg == 'exit()': break
        msg_out = ''
        for j in range(len(msg)):
            msg_out += Caesar.decrypt(ord(pw[i%len(pw)].lower())-ord('a')+1, msg[j])
            i += 1
        dec_msg += msg_out
        print msg_out
    return dec_msg


def main():
    pwd = str(raw_input('Enter your password:\n'))
    msg = str(raw_input('Enter your message:\n'))
    pw_list = map(str, raw_input('Enter passwords:\n').split())
    enc_msg = encrypt(pwd, msg)
    dec_msg = decrypt(pwd, enc_msg)
    bruted_msg = brute(pw_list, enc_msg)

    print 'Your encrypted message is:\n' + enc_msg + '\n\n'
    print 'Your decrypted message is:\n' + dec_msg + '\n\n'
    print 'Your bruteforced messages are:'
    for msg in bruted_msg:
        print msg


if __name__ == '__main__':
    main()
    #live_encrypt('password')
    #live_decrypt('password')