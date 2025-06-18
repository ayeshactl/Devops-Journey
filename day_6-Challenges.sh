#!/bin/bash
<<comment
🔹✅ Challenge 1: Write a simple Bash script that prints “Hello DevOps” along with the 
current date and time.
comment

#ANSWER:
echo "hi Ayesha, hello in devops,the current date and time is: $(date)"
#OUTPUT:
#hi Ayesha, hello in devops, the current date and time is: $(date)"



: <<'comment'
🔹 Challenge 2: Check if a website is reachable using curl or ping
comment

# ✅ Challenge 2 Script

# Define the website and domain
WEBSITE="https://www.learnxops.com"
DOMAIN="learnxops.com"

# Check website availability using curl
if command -v curl >/dev/null 2>&1; then
    if curl -Is "$WEBSITE" --max-time 5 | head -n 1 | grep -q "200\|301\|302"; then 
        echo " Success: $WEBSITE is reachable via curl!"
    else 
        echo "⚠️ Curl check failed, trying ping..."

        if ping -c 2 -W 2 "$DOMAIN" > /dev/null 2>&1; then
            echo "Success: $DOMAIN is reachable via ping!"
        else 
            echo " Failure: $WEBSITE is not reachable via curl or ping."
        fi
    fi
else
    echo "⚠️ curl is not installed. Skipping curl check, trying ping..."

    if ping -c 2 -W 2 "$DOMAIN" > /dev/null 2>&1; then
        echo "Success: $DOMAIN is reachable via ping!"
    else 
        echo " Failure: $WEBSITE is not reachable."
    fi
fi




: <<comment
✅ Challenge 3: Write a script that takes a filename as an argument, checks if it exists, and prints the content of the file accordingly.
comment


#ANSWER:
# check if filename argument is provided
if [ $# -eq 0 ]; then
      echo "Error: No file provided."
      echo "Usage: ./check_file.sh <filename>"
      exit 1
fi

FILENAME="$1"

#check if the file exists
if [ -f "$FILENAME" ]; then
      echo "File '$FILENAME' found. Displaying content:"
     cat "$FILENAME"
else 
     echo "Error: File '$FILENAME' does not exist."
fi





<<comment
✅ Challenge 4: Create a script that lists all running processes and writes the output to a file named process_list.txt.
comment

#ANSWER:

#DEFINE OUTPUT FILE 
OUTPUT_FILE="process_list.txt"

#List all running processes and write to file 
ps aux > "$OUTPUT_FILE"

#print success message
echo "Process list saved to $OUTPUT_FILE"

<<comment
##OUTPUT
 Example:

Case 1: ❌ No Argument
./check_file.sh
Output:
❌ Error: No filename provided.
Usage: ./check_file.sh <filename>

Case 2: ✅ File Exists
./check_file.sh hello.txt
Output:
✅ File 'hello.txt' found. Displaying content:
<content of hello.txt>

Case 3: ❌ File Doesn’t Exist
./check_file.sh xyz.txt
Output:
❌ Error: File 'xyz.txt' does not exist.

comment


<<comment
✅Challenge 5: Write a script that installs multiple packages at once (e.g., git, vim, curl). The script should check if each package is already installed before attempting installation.
comment

#ANSWER:
#define the list of packages to install
PACKAGES=("git" "vim" "curl")

#Loop through each package and check if its installed
for PACKAGE in "${PACKAGES[@]}"; do
if dpkg -l | grep -qw "$PACKAGE"; then
     echo "$PACKAGE is already installed."
else
    echo "Installing $PACKAGE..."
    sudo apt-get install -y "$PACKAGE" && \
    echo "$PACKAGE installed successfully." || \
    echo "Failed to install $PACKAGE."
   fi
done




<<comment
✅ Challenge 6: Create a script that monitors CPU and memory usage every 5 seconds and logs the results to a file.
comment

#ANSWER:
#!/bin/bash

# Define the log file
LOG_FILE="resource_usage.log"

echo "Monitoring CPU AND Memory usage... LOGS WILL BE SAVED IN $LOG_FILE"
echo "Timestamp | CPU (%) | Memory (%)" > "$LOG_FILE"

# Infinite loop to log system usage every 5 seconds
while true; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

    # Get CPU usage
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

    # Get Memory usage
    MEM_USAGE=$(free | awk '/Mem/ {printf "%.2f", $3/$2 * 100}')

    # Write data to the log file
    echo "$TIMESTAMP | $CPU_USAGE | $MEM_USAGE" >> "$LOG_FILE"

    # Wait for 5 seconds
    sleep 5
done

>>>>>>> 3779bfd (Add more challenges)
