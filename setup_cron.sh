#!/bin/bash

# Get the absolute path to the repository directory
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_EXEC="$(which python3)"

# Define the cron job line (runs every day at 10:00 AM)
CRON_JOB="0 10 * * * cd \"$REPO_DIR\" && \"$PYTHON_EXEC\" Main.py"

# Check if the cron job already exists
(crontab -l 2>/dev/null | grep -F "$REPO_DIR/Main.py") > /dev/null
if [ $? -eq 0 ]; then
    echo "Cron job already exists for this script."
else
    # Add the new cron job
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "Successfully added the cron job!"
    echo "The script will now run automatically every day at 10:00 AM."
fi
