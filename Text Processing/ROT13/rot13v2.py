"""rot13v2 = Convert html file content (alongwith tags) to ROT13 format"""
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
        for line in sys.stdin:
            for char in line:
                sys.stdout.write(rot13_letter(char))
#################################################################
"""
NOTE: From Windows Command Line, change to directory where the script
is stored, then type:
    type testPage.html | python rot13v2.py > rot13.html
Replace 'testPage' with the name of any html file you have in your current directory.    
"""
