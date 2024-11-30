import os
import sys

def say(text):
    os.popen('espeak -p 75 "' + text + '" --stdout | aplay 2>/dev/null')

# remove file name from arguments list
print sys.argv
text = sys.argv
text.pop(0)
# now reformat as whole string
text = str(' '.join(sys.argv))
print(text)
say(text)
