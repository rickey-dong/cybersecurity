import sys

if len(sys.argv) > 3: # python mode file file
    mode = sys.argv[1]
    if mode == "encode":
        plaintext_file = sys.argv[2]
        key_file = sys.argv[3]
        message = open(plaintext_file).read()
        key = open(key_file).read()
        shifting_strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ciphertext = ""
        for i in range(len(message)):
            ciphertext += message[i] + key[i % len(key)]
