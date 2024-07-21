# Playfair Cipher Implementation Documentation

## Overview
This script implements the Playfair cipher, a manual symmetric encryption technique. It provides functionality to encrypt and decrypt text using a keyword-based 5x5 table.

## Features
1. Generate a key table from a given keyword
2. Encrypt plaintext using the Playfair cipher algorithm
3. Decrypt ciphertext using the Playfair cipher algorithm

## Implementation Details

### Main Components
1. `generate_key_table(key: str) -> List[List[str]]`: Generates the 5x5 key table used for encryption and decryption.
2. `find_position(key_table: List[List[str]], char: str) -> Tuple[int, int]`: Finds the position of a character in the key table.
3. `encrypt_pair(key_table: List[List[str]], a: str, b: str) -> str`: Encrypts a pair of characters according to Playfair rules.
4. `decrypt_pair(key_table: List[List[str]], a: str, b: str) -> str`: Decrypts a pair of characters according to Playfair rules.
5. `encrypt_playfair(text: str, key: str) -> str`: Encrypts the entire plaintext using the Playfair cipher.
6. `decrypt_playfair(ciphertext: str, key: str) -> str`: Decrypts the entire ciphertext using the Playfair cipher.

### Playfair Cipher Algorithm Implementation

#### Key Table Generation
The `generate_key_table()` function creates the 5x5 table as follows:
1. Start with an empty table.
2. Add unique letters from the keyword (converted to uppercase).
3. Fill the remaining spaces with unused letters of the alphabet (excluding 'J').
4. Arrange the table into a 5x5 grid.

#### Encryption Process
The `encrypt_playfair()` function implements the encryption as follows:
1. Generate the key table from the given keyword.
2. Prepare the plaintext:
   - Convert to uppercase.
   - Replace 'J' with 'I'.
   - Group the text into pairs of letters.
   - If a pair has two identical letters, insert 'X' between them.
   - If the text has an odd number of letters, append 'X'.
3. For each pair of letters:
   - If the letters are in the same row of the key table, replace with letters to their right (wrapping around).
   - If the letters are in the same column, replace with letters below them (wrapping around).
   - If the letters form corners of a rectangle, replace with letters on the same row but at the other corners of the rectangle.

#### Decryption Process
The `decrypt_playfair()` function reverses the encryption process:
1. Generate the key table from the given keyword.
2. Group the ciphertext into pairs of letters.
3. For each pair, apply the reverse of the encryption rules.

## Usage
The script can be run from the command line. It includes a simple demonstration in the `__main__` block:

```python
if __name__ == "__main__":
    text = "HELLO"
    key = "KEYWORD"
    
    encrypted_text = encrypt_playfair(text, key)
    print(f"Encrypted text: {encrypted_text}")
    
    decrypted_text = decrypt_playfair(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")
```

## Limitations and Considerations
- The implementation replaces 'J' with 'I' in the plaintext and key table.
- The script does not handle lowercase letters; all input is converted to uppercase.
- Spaces and non-alphabetic characters are not preserved in the encryption/decryption process.
- The Playfair cipher, while more secure than simple substitution ciphers, is still vulnerable to frequency analysis attacks and is not suitable for securing sensitive information in modern contexts.

## Dependencies
The script uses only Python standard library modules. No additional installations are required beyond a standard Python environment.
