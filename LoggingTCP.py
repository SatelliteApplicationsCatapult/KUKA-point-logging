# THis code is run on a src file and is used to automate a call to a sub-program for each point to be logged in.
# Log3 sub-program should be on the KUKA smart pad. It creates a txt file with log of each tcp position and a timestamp of when it was reached.
# The txt file is savec under C:\KRC\Roboter\Template\
# You need to update the file path L21-22

import re

# Patterns to look for
to_init = (";FOLD INI;%")
sub_init = ("\\ndecl e6axis a\\ndecl e6pos p\\n\\n;FOLD INIT;%")
to_init_axis = (r";FOLD SPTP")
sub_axis = ("\\na=$axis_act\\np=$pos_act\\n;FOLD SPTP")
to_log = (";ENDFOLD\\n")
sub_log = (";ENDFOLD\\n;log tcp position\\nlog3(p.x, p.y, p.z, p.a, p.b, p.c, a.e1)\\nWAIT SEC 10.0;\\n")

# List where the first is pattern to find and second is the replacement for pattern
replacements = [(to_init, sub_init), (to_init_axis, sub_axis), (to_log, sub_log)]

# Put text file path to edit here
input_file = open("C:\\Users\\Name.Name\\Documents\\Input_file_name.txt", "r")
output_file = open("C:\\Users\\Name.Name\\Documents\\Output_file_name.txt", "w+")

with output_file as new, input_file as original:
    for word in original:
        new_word = word
        for pattern, replacement in replacements:
            new_word = re.sub(pattern, replacement, word)
            if new_word != word:
                break
        new.write(new_word)