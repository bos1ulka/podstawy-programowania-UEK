plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    code = ord(char)
    code = code + 1
    new_char = chr(code)
    encrypted_text = encrypted_text + new_char

print(f'Plain text:     {plain_text}')
print(f'Encrypted text: {encrypted_text}')
