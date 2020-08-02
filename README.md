PirateRadio
===========

MAKE Raspberry Pi Automated FM Radio Script.

Alex's spicy edits to the original [MAKE tutorial](https://makezine.com/projects/raspberry-pirate-radio/):
========================================
To future Alex: Follow the original MAKE tutorial, but use the suggestions here to make things go smoother. I had a lot of issues with trying to get this tutorial to work on my Raspberry Pi B. Documenting how I got it to work here, as well as adding my edits to the Python script. 

Step #1: Make the antenna.
--------------------------
* I used electrical tape instead of heat-shrink tubing. Ultimately, it didn't matter-- I ended up using a jumper wire because... 
* FCC Part 15 regulations stipulate that unlicensed frequency-emitting devices should have a range of about 200 feet maximum. *My 20 cm jumper wire is more than enough to exceed this range.* The original homemade 75 cm, 12 AWG antenna I used straight-up jammed my FM radio. So if you're going to go true pirate radio with a serious broadcast range, either stay far away from populated areas or don't get caught. ;)

Step #2: Flash the SD card and add music. 
-----------------------------------------
* When downloading MAKE Labs's disk image, first extract the .zip file you download. Then change the file extension from .iso to .img *before* flashing it to your SD card. 
* When adding music: 
    1. On the Raspberry Pi end: Make sure it's plugged into your LAN. You'll need some way to interface with the Raspberry Pi once the new SD card is inserted; you can't go headless right away. Create a "music" directory in root's home directory (so /root/music) and place all your music files there. The original script, contrary to tutorial directions, searches for music in the pirateradio directory. My edits relocated this search to within the home directory.
    2. SSHing into your Pi: 
        * If `alarmpi.local` can't be reached as an IP address, get your Pi's IP address like so: 
            - Enter `hostname -I` in the command line on your Raspberry Pi. 
            - Use that as your hostname when using WinSCP instead. 
        * While you're SFTPing into your Pi, make sure to download PirateRadio.py from this repository and replace the copy on your SD card with this one.     
   

Step #3: Edit the config file. 
-------------------------------
* Use [radio-locator](radio-locator.com) to find unused FM frequencies in your area before choosing a frequency to broadcast on. 
* The original script had weird issues-- either it crashed or it infinitely looped too fast for it to ever play anything. Shay @sk261 fixed this. 

No tips for Steps 4, 5, or 6. 


