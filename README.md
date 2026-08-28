# Git-roadmap-
This is an simple python script wich commits an pushes a single file every day so it looks like you work every day.

## How to use

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the script:
   ```bash
   python3 Main.py
   ```
4. To make it run automatically every day, you can set up a cron job (Linux/macOS) or a Task in Task Scheduler (Windows).

**Example cron job (runs every day at 10:00 AM):**
```bash
0 10 * * * cd /path/to/Git-roadmap- && /usr/bin/python3 Main.py
```
