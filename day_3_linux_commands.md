# DevOps Journey - Day 3: 100 Linux Commands

## Introduction

Welcome to **Day 3** of my DevOps journey! Today, I’ve learned **100 Linux commands** and want to document them here. This will help both me and others who are learning. These commands cover various aspects of working with Linux systems, including file management, system monitoring, networking, and more.

## 1. File and Directory Management

1. **`ls`** - List directory contents

   - Usage: `ls -l`
   - Example: Shows a detailed list of files and directories.

2. **`cd`** - Change directory

   - Usage: `cd /path/to/directory`
   - Example: Moves into the specified directory.

3. **`pwd`** - Print working directory

   - Usage: `pwd`
   - Example: Displays the current directory path.

4. **`mkdir`** - Create a new directory

   - Usage: `mkdir new_directory`
   - Example: Creates a directory named `new_directory`.

5. **`rmdir`** - Remove an empty directory

   - Usage: `rmdir directory_name`
   - Example: Removes an empty directory.

6. **`rm`** - Remove files or directories

   - Usage: `rm file.txt`
   - Example: Deletes the specified file.

7. **`cp`** - Copy files or directories

   - Usage: `cp source.txt destination.txt`
   - Example: Copies `source.txt` to `destination.txt`.

8. **`mv`** - Move or rename files

   - Usage: `mv oldfile.txt newfile.txt`
   - Example: Renames or moves `oldfile.txt` to `newfile.txt`.

9. **`touch`** - Create an empty file or update timestamp

   - Usage: `touch newfile.txt`
   - Example: Creates an empty `newfile.txt` file.

10. **`cat`** - Concatenate and display file content
    - Usage: `cat file.txt`
    - Example: Displays the content of `file.txt`.

## 2. File Permissions and Ownership

11. **`chmod`** - Change file permissions

    - Usage: `chmod 755 file.txt`
    - Example: Gives read, write, and execute permissions to the owner, and read/execute to others.

12. **`chown`** - Change file owner and group

    - Usage: `chown user:group file.txt`
    - Example: Changes the owner and group of `file.txt`.

13. **`chgrp`** - Change group ownership
    - Usage: `chgrp group file.txt`
    - Example: Changes the group ownership of `file.txt`.

## 3. System Monitoring

14. **`top`** - Display system tasks

    - Usage: `top`
    - Example: Shows running processes and their system resource usage.

15. **`htop`** - Interactive process viewer

    - Usage: `htop`
    - Example: Displays a more user-friendly process list than `top`.

16. **`ps`** - Report a snapshot of current processes

    - Usage: `ps aux`
    - Example: Displays all running processes.

17. **`free`** - Display memory usage

    - Usage: `free -h`
    - Example: Shows memory usage in a human-readable format.

18. **`df`** - Display disk space usage

    - Usage: `df -h`
    - Example: Shows disk space usage in a human-readable format.

19. **`du`** - Estimate file space usage

    - Usage: `du -sh`
    - Example: Shows the total disk usage of the current directory.

20. **`uptime`** - Show how long the system has been running

    - Usage: `uptime`
    - Example: Displays the system uptime and load averages.

21. **`dmesg`** - Print or control the kernel ring buffer

    - Usage: `dmesg | grep error`
    - Example: Filters the kernel log for error messages.

22. **`lscpu`** - Display CPU architecture information
    - Usage: `lscpu`
    - Example: Shows details about your CPU architecture.

## 4. Networking

23. **`ping`** - Send ICMP echo request to a network host

    - Usage: `ping google.com`
    - Example: Pings Google's DNS server to check connectivity.

24. **`ifconfig`** - Configure a network interface

    - Usage: `ifconfig eth0`
    - Example: Displays the status of the `eth0` network interface.

25. **`ip`** - Show/manipulate routing, devices, and tunnels

    - Usage: `ip addr show`
    - Example: Displays network interface details.

26. **`netstat`** - Network statistics

    - Usage: `netstat -tuln`
    - Example: Displays active network connections.

27. **`ss`** - Utility to investigate sockets

    - Usage: `ss -tuln`
    - Example: Shows similar information to `netstat`.

28. **`wget`** - Download files from the web

    - Usage: `wget http://example.com/file.tar.gz`
    - Example: Downloads a file from a URL.

29. **`curl`** - Transfer data from or to a server

    - Usage: `curl -O http://example.com/file.zip`
    - Example: Downloads a file from the internet.

30. **`nslookup`** - Query DNS to obtain domain name or IP address

    - Usage: `nslookup google.com`
    - Example: Resolves the IP address of `google.com`.

31. **`traceroute`** - Trace the route packets take to a network host

    - Usage: `traceroute google.com`
    - Example: Shows the path packets take to reach `google.com`.

32. **`route`** - Show/manipulate the IP routing table
    - Usage: `route -n`
    - Example: Displays the routing table.

## 5. Text Processing

33. **`grep`** - Search for patterns in files

    - Usage: `grep "pattern" file.txt`
    - Example: Searches for "pattern" in `file.txt`.

34. **`awk`** - Pattern scanning and processing language

    - Usage: `awk '{print $1}' file.txt`
    - Example: Prints the first column of `file.txt`.

35. **`sed`** - Stream editor for filtering and transforming text

    - Usage: `sed 's/old/new/g' file.txt`
    - Example: Replaces "old" with "new" in `file.txt`.

36. **`cut`** - Remove sections from each line of files

    - Usage: `cut -d, -f1 file.csv`
    - Example: Cuts the first field (column) from a CSV file.

37. **`sort`** - Sort lines of text files

    - Usage: `sort file.txt`
    - Example: Sorts the contents of `file.txt` alphabetically.

38. **`uniq`** - Report or omit repeated lines

    - Usage: `uniq file.txt`
    - Example: Removes duplicate lines in `file.txt`.

39. **`head`** - Output the first part of files

    - Usage: `head -n 10 file.txt`
    - Example: Shows the first 10 lines of `file.txt`.

40. **`tail`** - Output the last part of files
    - Usage: `tail -n 10 file.txt`
    - Example: Displays the last 10 lines of `file.txt`.

## 6. System Information and Performance

41. **`uname`** - Print system information

    - Usage: `uname -r`
    - Example: Displays the current Linux kernel version.

42. **`lscpu`** - Show CPU architecture information

    - Usage: `lscpu`
    - Example: Displays information about CPU architecture.

43. **`lsblk`** - List information about block devices

    - Usage: `lsblk`
    - Example: Lists all the block devices connected to your system.

44. **`iostat`** - Report CPU and I/O statistics

    - Usage: `iostat`
    - Example: Shows CPU and input/output statistics.

45. **`vmstat`** - Report virtual memory statistics

    - Usage: `vmstat`
    - Example: Displays memory, swap, and system statistics.

46. **`lshw`** - List hardware configuration

    - Usage: `lshw -short`
    - Example: Displays a summarized hardware list.

47. **`uptime`** - Show how long the system has been running
    - Usage: `uptime`
    - Example: Displays system uptime and load averages.

## 7. Process Management

48. **`ps`** - Report current processes

    - Usage: `ps aux`
    - Example: Lists all running processes with detailed information.

49. **`kill`** - Terminate processes

    - Usage: `kill -9 pid`
    - Example: Kills a process with a specified process ID (PID).

50. **`killall`** - Kill processes by name

    - Usage: `killall process_name`
    - Example: Terminates all processes with the name `process_name`.

51. **`bg`** - Resume a suspended job in the background

    - Usage: `bg`
    - Example: Resumes the most recent job in the background.

52. **`fg`** - Bring a background job to the foreground

    - Usage: `fg`
    - Example: Brings the most recent job to the foreground.

53. **`jobs`** - List active jobs
    - Usage: `jobs`
    - Example: Displays all background jobs.

## 8. Disk and File Systems

54. **`fdisk`** - Partition a disk

    - Usage: `fdisk /dev/sda`
    - Example: Opens the partition editor for the disk `/dev/sda`.

55. **`parted`** - Partitioning tool for managing disk partitions

    - Usage: `parted /dev/sda`
    - Example: Starts the parted tool to manage partitions on `/dev/sda`.

56. **`mkfs`** - Create a filesystem

    - Usage: `mkfs.ext4 /dev/sda1`
    - Example: Creates an ext4 filesystem on the partition `/dev/sda1`.

57. **`fsck`** - Check and repair a filesystem

    - Usage: `fsck /dev/sda1`
    - Example: Checks and repairs the filesystem on `/dev/sda1`.

58. **`mount`** - Mount a filesystem

    - Usage: `mount /dev/sda1 /mnt`
    - Example: Mounts the partition `/dev/sda1` to `/mnt`.

59. **`umount`** - Unmount a filesystem
    - Usage: `umount /mnt`
    - Example: Unmounts the filesystem mounted at `/mnt`.

## 9. User and Group Management

60. **`useradd`** - Add a user to the system

    - Usage: `useradd username`

    - Example: Creates a new user named `username`.

61. **`usermod`** - Modify a user account

    - Usage: `usermod -aG groupname username`
    - Example: Adds a user to a specific group.

62. **`userdel`** - Delete a user

    - Usage: `userdel username`
    - Example: Removes the user `username` from the system.

63. **`groupadd`** - Create a new group

    - Usage: `groupadd groupname`
    - Example: Creates a new group named `groupname`.

64. **`groupdel`** - Delete a group

    - Usage: `groupdel groupname`
    - Example: Removes the group `groupname`.

65. **`passwd`** - Change user password

    - Usage: `passwd username`
    - Example: Changes the password for the specified user.

66. **`id`** - Print user and group ID

    - Usage: `id username`
    - Example: Displays the user and group IDs of `username`.

67. **`groups`** - Show user’s groups
    - Usage: `groups username`
    - Example: Displays the groups that `username` belongs to.

## 10. Archive and Compression

68. **`tar`** - Archive files

    - Usage: `tar -cvf archive.tar directory/`
    - Example: Creates a tarball (`archive.tar`) from a directory.

69. **`gzip`** - Compress files

    - Usage: `gzip file.txt`
    - Example: Compresses `file.txt` into `file.txt.gz`.

70. **`gunzip`** - Decompress files

    - Usage: `gunzip file.txt.gz`
    - Example: Decompresses `file.txt.gz` back to `file.txt`.

71. **`zip`** - Compress files into a ZIP archive

    - Usage: `zip archive.zip file1.txt file2.txt`
    - Example: Creates a ZIP archive from `file1.txt` and `file2.txt`.

72. **`unzip`** - Extract files from a ZIP archive

    - Usage: `unzip archive.zip`
    - Example: Extracts all files from `archive.zip`.

73. **`bzip2`** - Compress files with Bzip2

    - Usage: `bzip2 file.txt`
    - Example: Compresses `file.txt` to `file.txt.bz2`.

74. **`bunzip2`** - Decompress files compressed with Bzip2
    - Usage: `bunzip2 file.txt.bz2`
    - Example: Decompresses `file.txt.bz2`.

## 11. Package Management

75. **`apt-get`** - Package handling utility for Ubuntu/Debian-based systems

    - Usage: `apt-get install package_name`
    - Example: Installs a package on Ubuntu/Debian.

76. **`apt-cache`** - Query the APT cache

    - Usage: `apt-cache search package_name`
    - Example: Searches for a package in the APT cache.

77. **`yum`** - Package management for CentOS/RHEL-based systems

    - Usage: `yum install package_name`
    - Example: Installs a package on CentOS/RHEL.

78. **`dnf`** - Next-generation package manager for Fedora

    - Usage: `dnf install package_name`
    - Example: Installs a package on Fedora.

79. **`rpm`** - Package manager for RPM-based systems

    - Usage: `rpm -ivh package.rpm`
    - Example: Installs an RPM package.

80. **`dpkg`** - Debian package manager

    - Usage: `dpkg -i package.deb`
    - Example: Installs a `.deb` package.

81. **`pacman`** - Package manager for Arch Linux
    - Usage: `pacman -S package_name`
    - Example: Installs a package on Arch Linux.

## 12. System Shutdown and Reboot

82. **`shutdown`** - Shut down the system

    - Usage: `shutdown -h now`
    - Example: Immediately shuts down the system.

83. **`reboot`** - Reboot the system

    - Usage: `reboot`
    - Example: Restarts the system.

84. **`poweroff`** - Power off the system

    - Usage: `poweroff`
    - Example: Powers off the system immediately.

85. **`halt`** - Halt the system
    - Usage: `halt`
    - Example: Stops all processes and halts the system.

## 13. Disk Usage and Management

86. **`fdisk`** - Partition a disk

    - Usage: `fdisk /dev/sda`
    - Example: Opens the partition editor for the disk `/dev/sda`.

87. **`parted`** - Partitioning tool for managing disk partitions

    - Usage: `parted /dev/sda`
    - Example: Starts the parted tool to manage partitions on `/dev/sda`.

88. **`mkfs`** - Create a filesystem

    - Usage: `mkfs.ext4 /dev/sda1`
    - Example: Creates an ext4 filesystem on the partition `/dev/sda1`.

89. **`fsck`** - Check and repair a filesystem

    - Usage: `fsck /dev/sda1`
    - Example: Checks and repairs the filesystem on `/dev/sda1`.

90. **`mount`** - Mount a filesystem

    - Usage: `mount /dev/sda1 /mnt`
    - Example: Mounts the partition `/dev/sda1` to `/mnt`.

91. **`umount`** - Unmount a filesystem
    - Usage: `umount /mnt`
    - Example: Unmounts the filesystem mounted at `/mnt`.

## 14. Logs and System Messages

92. **`journalctl`** - Query systemd logs

    - Usage: `journalctl -u service_name`
    - Example: Shows logs for a specific systemd service.

93. **`dmesg`** - Display kernel ring buffer messages

    - Usage: `dmesg | grep error`
    - Example: Filters kernel messages for errors.

94. **`tail -f`** - Follow a log file

    - Usage: `tail -f /var/log/syslog`
    - Example: Displays the real-time contents of `/var/log/syslog`.

95. **`less`** - View file content with paging
    - Usage: `less /var/log/messages`
    - Example: Views the content of the system log file.

## 15. System Backup and Restore

96. **`rsync`** - Remote file and directory synchronization

    - Usage: `rsync -av source/ destination/`
    - Example: Synchronizes files between two directories.

97. **`cpio`** - Copy files to and from archives

    - Usage: `find . | cpio -o > archive.cpio`
    - Example: Creates an archive of the current directory.

98. **`dd`** - Convert and copy a file

    - Usage: `dd if=/dev/sda of=/dev/sdb bs=64K conv=noerror,sync`
    - Example: Copies a disk to another disk.

99. **`tar`** - Backup and extract files from archives
    - Usage: `tar -cvf backup.tar /path/to/backup`
    - Example: Creates a backup of a directory in `backup.tar`.

## 16. Environment and Shell

100. **`echo`** - Display a line of text


### Conclusion
The path to becoming a **DevOps Engineer** requires a mix of foundational knowledge, mastering tools, and consistent hands-on practice. Keep learning, building projects, and collaborating with teams to gain real-world experience.

---

### Reference:
For more insights, check out this article on **[Linux Commands in DevOps](https://www.linkedin.com/pulse/linux-commands-devops-used-day-to-day-activit-chetan-/)**.
    - Usage: `echo "Hello, World!"`
    - Example: Prints "Hello, World!" to the terminal.
