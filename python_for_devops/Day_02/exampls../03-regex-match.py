
# Using re.match() to check if a string starts with a pattern...

import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
    print(search.group()) # brown
    print(search.start()) # 10  (index where match starts)
    print(search.end())    #15 (index where match ends)

else:
    print("no match!")