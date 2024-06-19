import subprocess
import datetime
import os

# Configuration
SOURCE_DIR = "D:\Projects\AccuKnox Project\System Health Monitoring"
REMOTE_USER = "manish4singh"
REMOTE_HOST = "https://github.com"
REMOTE_DIR = "https://github.com/manish4singh/System-Health-Monitoring"
LOG_FILE = "backup.log"

def backup_directory():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"Backup started at {timestamp}\n"
    
    try:
        result = subprocess.run(
            ["rsync", "-avz", SOURCE_DIR, f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            log_message += "Backup completed successfully.\n"
        else:
            log_message += f"Backup failed with errors:\n{result.stderr}\n"
    except Exception as e:
        log_message += f"Backup failed with exception:\n{str(e)}\n"
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message += f"Backup ended at {timestamp}\n"
    log_message += "-" * 60 + "\n"
    
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_message)

if __name__ == "__main__":
    backup_directory()
