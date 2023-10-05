# KUKA-point-logging
These programs are to automate calls to a subprogram to log points and timestamp.

# Logging.py
# This code is to run on a src file and is used to automate a call to a log1 sub-program for each point to be logged in.
# Log1 sub-program should be on the KUKA smart pad. It creates a txt file with log of each axis position and a timestamp of when it was reached.
# The txt file is savec under C:\KRC\Roboter\Template\
# You need to update the file path L22-23 on the Logging.py

# LoggingTCP.py
# This code is to run on a src file and is used to automate a call to a log3 sub-program for each point to be logged in.
# Log3 sub-program should be on the KUKA smart pad. It creates a txt file with log of each tcp position and a timestamp of when it was reached.
# The txt file is savec under C:\KRC\Roboter\Template\
# You need to update the file path L20-21 on the Logging.py
