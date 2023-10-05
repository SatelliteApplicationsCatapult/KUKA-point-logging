import re #import RegEx

# Patterns to look for
to_init = (";FOLD INI;%")
sub_init = ("\\n  decl e6axis a\\n  decl e6pos p\\n\\n;FOLD INI;%")

to_time = (";COMMANDS")
sub_time = ("\\n;COMMANDS\\n;init and start timer\\n$TIMER[1]=0\\n$TIMER_STOP[1]=FALSE")

to_init_axis = (r";FOLD SPTP")
sub_axis = ("\\na=$axis_act\\np=$pos_act\\n;FOLD SPTP")

to_log = (";ENDFOLD\\n")
sub_log = (";ENDFOLD\\n;log tcp position, track, and timer\\nlog4Mani(p.x, p.y, p.z, p.a, p.b, p.c, a.e1, $TIMER[1])\\nWAIT SEC 5.0;\\n")

to_end = ("END\\n")
sub_end = ("\\n;stop timer\\n$TIMER_STOP[1]=TRUE\\nEND")

# List where the first is pattern to find and second is the replacement for pattern
replacements = [(to_init, sub_init), (to_time, sub_time), (to_init_axis, sub_axis), (to_log, sub_log), (to_end, sub_end)]

# Put text file path to edit here
input_file = open("C:\\Users\\Name.Name\\Documents\\Input_file_name", "r")
output_file = open("C:\\Users\\Name.Name\\Documents\\Output_file_name.txt", "w+")

with output_file as new, input_file as original:
    for word in original:
        new_word = word
        for pattern, replacement in replacements:
            new_word = re.sub(pattern, replacement, word)
            if new_word != word:
                break
        new.write(new_word)