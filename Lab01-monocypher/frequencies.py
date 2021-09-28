import sys

filename = ""

if len(sys.argv) > 1:
    filename = sys.argv[1]
    text = open(filename).read()
    print(text)
else:
    print("error! provide a file")

def calculate_frequencies(source_text):
    freq_dict = {}
    total_num_of_letters = 0
    for character in source_text:
        if character.isalpha():
            total_num_of_letters += 1
            
