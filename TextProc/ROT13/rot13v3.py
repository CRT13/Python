""""rot13v3 = Convert html file content (without affecting the tags) to ROT13 format"""
######################## IMPORT LIBRARIES #######################
import sys
import string
from optparse import OptionParser
########################## DICTIONARIES #########################
CHAR_MAP = dict(list(zip(string.ascii_lowercase, string.ascii_lowercase[13:36]+string.ascii_lowercase[0:13])))
###################### CLASS DECLARATIONS #######################
class RotateStream(object):
    MARKUP_START = '<'
    MARKUP_END = '>'
    def __init__(self,skip_tags):
        self.skip_tags = skip_tags
    # Return 13-shifted character notation of a letter
    def rot13_letter(self,letter):
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
    # Return from a file handle
    def rot13_file(self,handle):
        state_markup = False
        for line in handle:
            for char in line:
                if self.skip_tags:
                    if state_markup:
                        """Check for '>' in line"""
                        if char == self.MARKUP_END:
                            state_markup = False
                    else:
                        """Check for '<' in line"""
                        if char == self.MARKUP_START:
                            state_markup = True
                        else:
                            char = self.rot13_letter(char)
                else:
                    char = self.rot13_letter(char)
                yield char
########################## MAIN PROGRAM #########################
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-t','--tags',dest="tags",help="Ignore Markup Tags",default=False,action="store_true")
    options,args = parser.parse_args()
    """Initialize instance of class"""
    rot13class = RotateStream(options.tags)
    for letter in rot13class.rot13_file(sys.stdin):
        sys.stdout.write(letter)
#################################################################    
"""
NOTE: From Windows Command Line, change to directory where the script
is stored, then type:
    type testPage.html | python rot13v3.py -t > rot13.html
Replace 'testPage' with the name of any html file you have in your current directory.
"""
