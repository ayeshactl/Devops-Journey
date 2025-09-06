
#1️⃣ Extract all IP addresses from server logs

import re

log = "Error from 192.168.1.10, connected from 10.0.0.5, retry 172.16.0.1"
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", log)
print(ips)

# \d       → any digit (0-9)
# +        → one or more of previous (\d+ = one or more digits)
#  \.       → literal dot
# \d+\.\d+\.\d+\.\d+  → matches IP like 192.168.1.10 (four groups of digits separated by dots)


## 2️⃣ Extract all email addresses from config or alert files

config = "admin@example.com, devops@company.com, user123@domain.org"
emails = re.findall(r"[a-zA-Z0-9._%+-]@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")  # Regex pattern for email

emails = re.findall(pattern, text)
print(emails)  # Output: ['admin@example.com', 'devops@company.org']


# Explanation of each part of the regex:
# [a-zA-Z0-9._%+-]+  → username part (letters, digits, . _ % + -)
# @                  → literal @ symbol
# [a-zA-Z0-9.-]+     → domain name (letters, digits, . -)
# \.                 → literal dot before TLD
# [a-zA-Z]{2,}       → TLD (at least 2 letters, e.g., com, org)