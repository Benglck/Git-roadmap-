#!/bin/bash

# Define paths
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLIST_NAME="com.gitroadmap.dailycommit.plist"
PLIST_PATH="$HOME/Library/LaunchAgents/$PLIST_NAME"
PYTHON_EXEC="$(which python3)"

# Create the plist file
cat <<EOF > "$PLIST_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.gitroadmap.dailycommit</string>
    <key>ProgramArguments</key>
    <array>
        <string>$PYTHON_EXEC</string>
        <string>$REPO_DIR/Main.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>$REPO_DIR</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>10</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
EOF

# Unload if it already exists, then load the new one
launchctl unload "$PLIST_PATH" 2>/dev/null
launchctl load "$PLIST_PATH"

echo "Successfully set up the launchd agent!"
echo "Your script is now scheduled to run daily at 10:00 AM."
echo "If your Mac is asleep at 10:00 AM, it will automatically run as soon as you wake it up."
