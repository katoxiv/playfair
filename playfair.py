def generate_key_table(key):
    key_table = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    for char in key:
        if char not in key_table:
            key_table.append(char.upper())
    
    for char in alphabet:
        if char not in key_table:
            key_table.append(char)
            
    return [key_table[i:i+5] for i in range(0, len(key_table), 5)]

def find_position(key_table, char):
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == char:
                return i, j
    return -1, -1

def encrypt_pair(key_table, a, b):
    row1, col1 = find_position(key_table, a)
    row2, col2 = find_position(key_table, b)
    
    if row1 == row2:
        return key_table[row1][(col1 + 1) % 5] + key_table[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return key_table[(row1 + 1) % 5][col1] + key_table[(row2 + 1) % 5][col2]
    else:
        return key_table[row1][col2] + key_table[row2][col1]

def decrypt_pair(key_table, a, b):
    row1, col1 = find_position(key_table, a)
    row2, col2 = find_position(key_table, b)
    
    if row1 == row2:
        return key_table[row1][(col1 - 1) % 5] + key_table[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return key_table[(row1 - 1) % 5][col1] + key_table[(row2 - 1) % 5][col2]
    else:
        return key_table[row1][col2] + key_table[row2][col1]

def encrypt_playfair(text, key):
    key_table = generate_key_table(key)
    text = text.upper().replace('J', 'I')
    
    i = 0
    pairs = []
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            b = 'X'
            i -= 1
        pairs.append(a+b)
        i += 2
    
    ciphertext = ''
    for a, b in pairs:
        ciphertext += encrypt_pair(key_table, a, b)
        
    return ciphertext

def decrypt_playfair(ciphertext, key):
    key_table = generate_key_table(key)
    ciphertext = ciphertext.upper().replace('J', 'I')
    
    i = 0
    pairs = []
    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i+1] if i+1 < len(ciphertext) else 'X'
        pairs.append(a+b)
        i += 2
    
    plaintext = ''
    for a, b in pairs:
        plaintext += decrypt_pair(key_table, a, b)
        
    return plaintext

if __name__ == "__main__":
    text = "HELLO"
    key = "KEYWORD"
    
    encrypted_text = encrypt_playfair(text, key)
    print(f"Encrypted text: {encrypted_text}")
    
    decrypted_text = decrypt_playfair(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")
