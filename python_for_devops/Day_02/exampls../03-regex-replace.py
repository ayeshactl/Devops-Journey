
# Replace a word in a string using regex (re.sub())....

import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)   #$re.sub() → a Python regex function that replaces all occurrences of a pattern in a string with a specified replacement.
print("Modified text:", new_text)