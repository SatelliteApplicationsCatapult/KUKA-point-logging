# THis code is run on a src file and is used to automate a call to a sub-program for each point to be logged in.
# Log1 sub-program should be on the KUKA smart pad. It creates a txt file with log of each axis position and a timestamp of when it was reached.
# The txt file is savec under C:\KRC\Roboter\Template\
# You need to update the file path L22-23

import re #import RegEx

# Patterns to look for
to_init = (";COMMANDS")
sub_init = (";COMMANDS\\n for i = 1 to 300\\n ;reset timer\\n $timer[1]=0\\n ;start timer\\n $timer_stop[1]=false\\n")
to_init_axis = (r";FOLD SPTP")
sub_axis = ("\\na=$axis_act\\n;FOLD SPTP")
to_log = (";ENDFOLD\\n")
sub_log = (";ENDFOLD\\nWAIT SEC 10.0;\\n;log i, axis position, timestamp\\nlog1(i, a.a1, a.a2, a.a3, a.a4, a.a5, a.a6, a.e1, $timer[1])\\n;increment waypoint nb\\ni=i+1\\n")
to_end = ("END\\n")
sub_end = ("\\nendfor\\n;stop timer\\n$timer_stop[1]=true\\nEND")

# List where the first is pattern to find and second is the replacement for pattern
replacements = [(to_init, sub_init), (to_init_axis, sub_axis), (to_log, sub_log), (to_end, sub_end)]

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
        

