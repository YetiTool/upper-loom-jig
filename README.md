# Clone the repo and make the launcher executable
- Clone this repo into _/home/pi_ by using `git clone https://github.com/YetiTool/upper-loom-jig`
- Access the repository directory with the command `cd upper-loom-jig`
- Make the launcher script executable by running `sudo chmod +x launcher.sh`
# Make launcher.sh run on boot by making it a cronjob
- Return to /home/pi by running `cd ..`
- Run `sudo crontab -e`
- When prompted, choose which editor you want to use. I used `/bin/nano`
- Add the following line to the bottom of the file: `@reboot bash /home/pi/upper-loom-jig/launcher.sh &`
- Press 'Ctrl' + 'X', then 'Y', then 'Enter' to save and close the file
- reboot the Pi with `sudo reboot` to test that the script auto starts.
- If the script is running correctly you will see the line "START DD-MM-YYYY HH-MM-SS" in RESULTS.txt
