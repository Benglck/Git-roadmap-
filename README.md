# Git-roadmap-
This is a simple python script which commits and pushes a single file every day so it looks like you work every day.

## How it works
The script simply updates a file called `daily_work.txt`, commits the change, and runs `git push`. Because it uses standard git commands, it pushes the daily commits to whichever remote repository the folder is currently connected to (its `origin`).

## How to use it for your own GitHub profile
If you want to use this script to maintain your own contribution graph, **you must Fork this repository** (or create a brand new repo of your own). If you just clone this repository directly, the script will try to push to the original creator's repository and fail because you don't have access!

1. **Fork** this repository to your own GitHub account (click the "Fork" button at the top right of the page).
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Git-roadmap-.git
   ```
3. Open the terminal and navigate into the folder:
   ```bash
   cd Git-roadmap-
   ```
4. Run the script manually to test it:
   ```bash
   python3 Main.py
   ```

## Automating it
To make it look like you are working every day without you having to remember, you can schedule the script to run automatically in the background.

### On macOS (Recommended for Mac users)
We provide a setup script that uses macOS `launchd`. This is highly recommended over cron because if your computer is asleep at the scheduled time, it will automatically catch up and run the script as soon as you wake it up:
```bash
./setup_launchd.sh
```

### On Linux / macOS (cron)
You can use a cron job. We provide a setup script that will add it for you:
```bash
./setup_cron.sh
```
Or you can add this line manually using `crontab -e` (make sure to adjust the path to match where you cloned your fork):
```bash
0 10 * * * cd /absolute/path/to/Git-roadmap- && /usr/bin/python3 Main.py
```
