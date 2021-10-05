import sys

if len(sys.argv) > 3: # python mode file file
    mode = sys.argv[1]
    if mode == "encode":
        plaintext_file = sys.argv[2]
        key_file = sys.argv[3]
        message = open(plaintext_file).read()
        key = open(key_file).read()
        message = message.strip()
        key = key.strip()
        shifting_strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ciphertext = ""
        for i in range(len(message)):
            ciphertext += shifting_strings[ (shifting_strings.find(message[i]) + shifting_strings.find(key[i % len(key)]) ) % 26]
        print(ciphertext)
    elif mode == "decode":
        cipher_file = sys.argv[2]
        key_file = sys.argv[3]
        cipher = open(cipher_file).read()
        key = open(key_file).read()
        cipher = cipher.strip()
        key = key.strip()
        shifting_strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = ""
        for i in range(len(cipher)):
            message += shifting_strings[ (shifting_strings.find(cipher[i]) - shifting_strings.find(key[i % len(key)]) ) ]
        print(message)
