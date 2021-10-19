import sys

debug = False

def create_output():
    output = []
    for text in range(len(inp)):
        output.append( inp[text] ^ key[text % len(key)] )
    return output

def numbers_output(list_of_base_ten_vals):
    output = []
    for xored_base_ten_value in list_of_base_ten_vals:
        output.append(hex(xored_base_ten_value)[2:])
    return output

def display_numbers_output(list_of_base_sixteen_vals):
    display = ""
    for base_sixteen in list_of_base_sixteen_vals:
        display += base_sixteen
        display += " "
    display = display[:-1]
    return display

if(debug):
  print("mode:"+mode)
  print(key)
  print(inp)

if len(sys.argv) > 3: # .py mode keyfile messagefile
    mode = sys.argv[1]
    keyfile = sys.argv[2]
    inpfile = sys.argv[3]
    key = open(keyfile,"rb").read()
    inp = open(inpfile,"rb").read()
    key = key.strip() #removes the mandatory \n at the end of the file to support one line messages.
    inp = inp.strip() #removes the mandatory \n at the end of the file to support one line messages.
    if mode == "numOut":
        print(display_numbers_output(numbers_output(create_output())))
    elif mode == "human":
        xor_values_list = create_output()
        output_file = open("output", "ab")
        for xor_value in xor_values_list:
            output_file.write(xor_value.to_bytes(1, byteorder="little"))
        output_file.close()
    else:
        print("NOT A VALID MODE")
else:
    print("NOT ENOUGH ARGS")
