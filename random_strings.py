from interpreter import run
import random

"""
text file in the format:
    length of output
    output
    bitstring
"""
def rewrite(new_length, output, bitstring):
    tf = open("output.txt", "w")
    tf.write(str(new_length)+"\n"+str(output)+"\n"+str(bitstring))
    tf.close()

def is_valid_output(output):
    tckr = True
    if not len(output)%2:
        for i in output:
            if tckr:
                if i == '1':
                    tckr = False
                else:
                    return(False)
            elif not tckr:
                if i == '0':
                    tckr = True
                else:
                    return(False)
        return(True)
    else:
        return(False)

text_file = open("output.txt", "r")
curr_length = int(text_file.readline().strip())
text_file.close()

prog = "01"*5
while True:
    inp_arr = []
    for _ in range(70):
        inp_arr.append(str(random.randint(0,1)))
    inp_str = ''.join(inp_arr) + prog
    output = run(inp_str)
    if output:
        #print(len(output))
        #print(output)
        #print(inp_str)
        if len(output) > curr_length:
            if is_valid_output(output):
                rewrite(len(output), output, inp_str)
                curr_length = len(output)
                print("           WRITING")
                print(len(output))
                print(output)
                print(inp_str)
"""
To Do:
    Make it run lots.
    Make it check of the string is of the correct format(ie. 10101010101010.....). DONE
    Make it write to and read a text file for archived results. DONE
"""
