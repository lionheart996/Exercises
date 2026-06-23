text = input()
encrypted_text = ""

for ch in text:
    encrypted_character = chr(ord(ch) + 3)
    encrypted_text += encrypted_character

print(encrypted_text)