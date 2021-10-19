import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

def create_output():
    output = []
    for text in range(len(inp)):
        output.append( ord(inp[text]) ^ ord(key[text % len(key)]) )
    return output

def numbers_output(list_of_base_ten_vals):
    output = []
    for xored_base_ten_value in list_of_base_ten_vals:
        output.append(hex(xored_base_ten_value)[2:])
    return output

if(debug):
  print("mode:"+mode)
  print("key: "+key)
  print("inp: "+inp)
