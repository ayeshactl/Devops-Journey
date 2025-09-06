"""

strip() ka use string ke aage-peeche ke unwanted spaces, newlines (\n), ya special characters ko hataane ke liye hota hai.
Yeh beech ke characters ko nahi hatata — sirf start aur end se.

"""

text = "   some spaces around    "
stripped_text = text.strip()
print("Stripped text:",stripped_text)