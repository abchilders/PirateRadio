Hey!!! Don't edit the files in this directory!!!
This is backups from the root directory and from the pirateradio directory, which I did by doing the following:

sudo su
cp -r /root /home/pi/root-backup
cp -r /pirateradio /home/pi/root-backup

And then, from /home/pi/:
sudo chown pi -R root-backup
