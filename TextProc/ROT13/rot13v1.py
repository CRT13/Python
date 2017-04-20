"""rot13v1 = Convert command-line input to ROT13 format"""
######################## IMPORT LIBRARIES #######################
import sys
import string
########################## DICTIONARIES #########################
CHAR_MAP = dict(list(zip(string.ascii_lowercase, string.ascii_lowercase[13:36]+string.ascii_lowercase[0:13])))
##################### FUNCTION DECLARATIONS #####################
# Return 13-shifted character notation of a letter
def rot13_letter(letter):
    do_upper = False
    if letter.isupper():
        do_upper = True
    letter = letter.lower()
    if letter not in CHAR_MAP:
        return letter
    else:
        letter = CHAR_MAP[letter]
        if do_upper:
            letter = letter.upper()
    return letter
########################## MAIN PROGRAM #########################
if __name__ == '__main__':
        for char in sys.argv[1]:
            sys.stdout.write(char)
        sys.stdout.write('\n')
        for char in sys.argv[1]:
            sys.stdout.write(rot13_letter(char))
        sys.stdout.write('\n')
#################################################################    
"""
NOTE: From Windows Command Line, change to directory where the script
is stored, then type:
    python rot13v1.py "Hi, My Name is ... Slim Shady"
Replace the text in quotes with something you like.
"""
