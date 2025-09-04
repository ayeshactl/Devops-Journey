# -------------------------
# Python Backup Script
# -------------------------
# Modules import
import shutil       # file/folder operations & compression
import datetime     # date & time
import os           # path handling

# Function to create backup
def backup_files(source, destination):
    """
    Backup a folder into a compressed .tar.gz archive
    Backup filename will include current date and time to make it unique
    """
    # get current date and time
    now = datetime.datetime.now()   # example: 2025-09-04 14:30:25
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")  # format: YYYY-MM-DD_HH-MM-SS
    
    # create backup filename with destination path
    backup_file_name = os.path.join(destination, f"backup_{timestamp}")
    
    # create compressed archive (.tar.gz)
    # shutil.make_archive(output_filename, format, source_dir)
    shutil.make_archive(backup_file_name, 'gztar', source)
    
    # print confirmation message
    print(f"Backup created successfully: {backup_file_name}.tar.gz")

# -------------------------
# User can change these paths
# -------------------------
source = "/home/a/Desktop/Devops-Journey/python workshop practice"
destination = "/home/a/Desktop/Devops-Journey/python workshop practice/backups"

# Ensure destination folder exists, create if not
if not os.path.exists(destination):
    os.makedirs(destination)

# Call the backup function
backup_files(source, destination)
