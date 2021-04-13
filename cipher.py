# A simple En-/De-crypting program using a Caesar Cipher 

# Function for encryption and decryption
def cipher(data, key, mode):
    alphabet = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ1234567890-=!@#$%^&*()_+`~,./;'[]\\<>?:\"{}|"
    new_data = ""
    for c in data:
        # Shift character by c
        index = alphabet.find(c)
        if index == -1:
            # Character not found
            new_data += c
        else:
            # Shift string based on key and mode
            new_index = index + key if mode == 1 else index - key
            new_index %= len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    # Return the ciphered text
    return new_data

# Select input mode (encryption or decryption)
mode = input("Are you (E)ncrypting or (D)ecrypting? ")

# Encrypt text
if mode == "E":
    key = int(input("What would you like the cipher key to be? "))
    string = input("Insert message to be encrypted: ")
    encrypted = cipher(string, key, 1)
    print("Cipher: ", encrypted)

# Decrypt cipher
elif mode == "D":
    key = int(input("What would you like the cipher key to be? "))
    string = input("Insert cipher to be decrypted: ")
    decrypted = cipher(string, key, 0)
    print("Decrypted message: ", decrypted)