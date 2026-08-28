import subprocess
import datetime

FILE_TO_COMMIT = "daily_work.txt"

def daily_commit():
    # Get current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append the timestamp to the file to create a change
    with open(FILE_TO_COMMIT, "a") as file:
        file.write(f"Work done on {current_time}\n")
    
    try:
        # Git add
        subprocess.run(["git", "add", FILE_TO_COMMIT], check=True)
        
        # Git commit
        commit_message = f"Daily commit: {current_time}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Git push
        subprocess.run(["git", "push"], check=True)
        
        print(f"Successfully committed and pushed at {current_time}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during git operations: {e}")

if __name__ == "__main__":
    daily_commit()
