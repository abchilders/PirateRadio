import os
import sys
import argparse
from datetime import datetime

def say(text):
    os.popen('espeak "' + text + '" --stdout | aplay 2>/dev/null')

def create_wav(text, file_name):
    os.popen('espeak "' + text + '" --stdout > ' + file_name)
    
def main():
    # set up argument parser
    parser = argparse.ArgumentParser(description='Uses TTS to convert STDIN to a .wav file.')
    parser.add_argument('-f', '--file', nargs='?', type=str, help='The file name to output audio to (default: current datetime)')
    parser.add_argument('text', nargs='+', type=str, help='The text to be converted to speech')
    args = parser.parse_args()
    
    # if output file not specified, get current date and time for naming .wav output file
    if(args.file):
        filename = args.file
    else:
        now = datetime.now()
        filename = now.strftime("%d-%m-%Y_%H:%M:%S:%f") + '.wav'
    print('creating ' + filename)

    # make espeak wav of given text
    text = args.text
    text = str(' '.join(text))
    create_wav(text, filename)
    #read back file out loud 
    #say(text)
    #os.popen('aplay ' + filename)

main()
