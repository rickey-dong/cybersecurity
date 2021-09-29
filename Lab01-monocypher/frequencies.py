import sys

filename = ""

if len(sys.argv) > 1:
    filename = sys.argv[1]
    text = open(filename).read()
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
    print(freq_dict)
    while ascii_val < 123:
        freq_list.append(freq_dict[chr(ascii_val)])
        ascii_val += 1
    return freq_list

list_of_standard_letter_freqs = calculate_frequencies(text)

string_percentages_results = ""

index = 0

while index < 26:
    string_percentages_results += chr(index + 97) + ":" + list_of_standard_letter_freqs[index]
    string_percentages_results += '\n'
    index += 1

print(string_percentages_results)
