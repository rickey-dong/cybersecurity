import sys
import math

filename = ""

if len(sys.argv) > 1:
    filename = sys.argv[1]
    cipherfile = sys.argv[2]
    text = open(filename, encoding="utf-8").read()
else:
    print("error! provide a file")

def calculate_frequencies(source_text):
    freq_dict = {}
    total_num_of_letters = 0
    for character in source_text:
        if character.isalpha():
            total_num_of_letters += 1
            letter = character.lower()
            if letter in freq_dict:
                freq_dict[letter] += 1
            else:
                freq_dict[letter] = 1
    for letter in freq_dict:
        freq_dict[letter] = freq_dict[letter] / total_num_of_letters
    freq_list = []
    ascii_val = 97
    while ascii_val < 123:
        if chr(ascii_val) in freq_dict:
            freq_list.append(freq_dict[chr(ascii_val)])
        else:
            freq_list.append(0)
        ascii_val += 1
    return freq_list

list_of_standard_letter_freqs = calculate_frequencies(text)

string_percentages_results = ""

index = 0

while index < 26:
    string_percentages_results += chr(index + 97) + ":" + str(list_of_standard_letter_freqs[index])
    string_percentages_results += '\n'
    index += 1

print(string_percentages_results)

def caesar_cracker(ciphertext):
    cipher = open(ciphertext, encoding="utf-8").read()
    print(cipher)
    cipher_letter_freqs = calculate_frequencies(cipher)
    potential_correct_shift = 0
    correct_shift = 0
    eucl_dist = float('inf')
    potential_eucl_dist = 0
    rotation = 0
    while rotation < 26:
        index = 0
        while index < 26:
            potential_eucl_dist += (list_of_standard_letter_freqs[index] - cipher_letter_freqs[(index + potential_correct_shift) % 26])**2
            index += 1
        potential_eucl_dist = math.sqrt(potential_eucl_dist)
        if potential_eucl_dist < eucl_dist:
            eucl_dist = potential_eucl_dist
            correct_shift = potential_correct_shift
        rotation += 1
        potential_eucl_dist = 0
        potential_correct_shift += 1
    cracked_text = ""
    for character in cipher:
        if character.isalpha():
            print(correct_shift)
            print(ord(character))
            if ord(character)-correct_shift < 97:
                cracked_text += chr( (ord(character) - correct_shift) + 26)
            else:
                cracked_text += chr(ord(character)-correct_shift)
        else:
            cracked_text += character
    return cracked_text

print(caesar_cracker(cipherfile))