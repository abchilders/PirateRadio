#!/bin/bash
# Reads each line of a text file and converts that line of text into a .wav
#	file using espeak TTS.

filename=$1
while read line; do
	python /root/tags/espeak_wav_maker.py $line
done < $filename
