import os
import sys
from datetime import datetime

def say(text):
    os.popen('espeak "' + text + '" --stdout | aplay 2>/dev/null')

def create_wav(text, file_name):
    os.popen('espeak "' + text + '" --stdout > ' + file_name + '.wav')

def main():
    # remove file name from arguments list
    print sys.argv
    text = sys.argv
    text.pop(0)

    # now reformat as whole string
    text = str(' '.join(sys.argv))

    # get current date and time for naming .wav output file
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
    print(dt_string)

    # make espeak wav of given text and read back out loud
    print(text)
    create_wav(text, dt_string)
    #say(text)
    #os.popen('aplay ' + dt_string + '.wav')

main()
