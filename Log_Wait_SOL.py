###### Automate call to logging sub-program for program to run on KUKA #####
#  
# Author: Esther Rayssiguie
#
# Description:
# This script is to run on a laptop, external to KUKA's controller. It will automate a logging
# for the tcp position and a timer whenever a motion is reached. This was coded for SPTP type motions.
# You can easily change the type of motions you want to log by changing "SPTP" to "SLIN" for example in 
# the patterns to look for. Or add multiple.
# 
# 1- You will need to take the src file you want to change and rename it as a txt file.
#     E.g.: BatchMani.src   ->  BatchMani.txt
# 2- Then update the path of your txt file to the disred one in this script
# 3- Run this script. You will obtain the new txt file with the substitution
# 4- Take your new txt file and rename it to be src. Make sure the name match with the corresponding dat file!
#     E.g.: BatchManiNew.txt -BatchManiNew.src
#

# Import packages
import re #import RegEx

# Patterns to look for #
# Declare p for KUKA TCP's position
to_init = (";FOLD INI;%")
sub_init = ("\\n  decl e6pos p\\n\\n;FOLD INI;%")
# Start a timer at beginning of program
to_time = (";COMMANDS")
sub_time = (";COMMANDS\\n;init and start timer\\n$TIMER[1]=0\\n$TIMER_STOP[1]=FALSE")
#re-initialise the e6pos for each SPTP declared
to_init_axis = (r";FOLD SPTP")
sub_axis = ("\\np=$pos_act\\n;FOLD SPTP")
# send the tcp position and timer value to the sub-program called log4Sol which will log all the data in a file
# the created file by log4Sol is saved under: 
to_log = (";ENDFOLD\\n")
sub_log = (";ENDFOLD\\n;log tcp position, track, and timer\\nlog4Sol(p.x, p.y, p.z, p.a, p.b, p.c, $TIMER[1])\\nWAIT SEC 5.0;\\n")
# stop the timer
to_end = ("END\\n")
sub_end = ("\\n;stop timer\\n$TIMER_STOP[1]=TRUE\\nEND")

# List where the first is pattern to find and second argument is the replacement for the pattern
replacements = [(to_init, sub_init), (to_time, sub_time), (to_init_axis, sub_axis), (to_log, sub_log), (to_end, sub_end)]

# Put the file path of the text file to edit here
input_file = open("C:\\Users\\Name.Name\\Documents\\Input_file_name.txt", "r")
# Put the file path of the NEW txt file which will be created here with it's name
output_file = open("C:\\Users\\Name.Name\\Documents\\Output_file_name.txt", "w+")

# Open the text file to update and the new file that will contain the pattern's replacement
with output_file as new, input_file as original:
    for word in original:
        new_word = word
        # For each pattern detected, write it's substitution in the new created file
        for pattern, replacement in replacements:
            new_word = re.sub(pattern, replacement, word)
            if new_word != word:
                break
        new.write(new_word)