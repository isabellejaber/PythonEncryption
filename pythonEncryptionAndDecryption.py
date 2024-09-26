#!/usr/bin/env python3
import hashlib
from string import digits

# Part 1
#dictionary for letter/value pairs
letter_val = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
              'l': 12,'m': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
              'v': 22, 'w': 23,'x': 24, 'y': 25, 'z': 26}

# define encrypt function to accept the message and the key as arguments
def encrypt(message, key):
    #make the message lower case
    message=message.lower()
    #make the key lower case
    key=key.lower()
    #remove any spaces from message
    message = message.replace(" ", "")
    #remove any spaces from key
    key = key.replace(" ", "")
    # remove special characters from message
    message=''.join(letter for letter in message if letter.isalnum())
    # remove special characters from key
    key=''.join(letter for letter in key if letter.isalnum())
    #remove digits from message
    message = message.translate(str.maketrans('', '', digits))
    #remove digits from key
    key = key.translate(str.maketrans('', '', digits))
    #check if the key is shorter than the message.
    #while this is true append sections of the key to itself, so it's length eventually matches the length of the key.
    #this allows each letter in the message to have a corresponding letter in the key to encode it.
    while len(key) < len(message):
        diff = len(message) - len(key)
        key = key + key[:diff]
    #turn the message into a list of characters
    char_message = list(message)
    #turn the key into a list of characters
    char_key = list(key)
    #create the result variable to hold the encoded message
    result = ""
    #create temporary value to hold the index for the char_key list
    k = 0
    #for every character in the message
    for m in char_message:
        #add the value of the character in the message to its corresponding character in the key and subtract 1 (because it is exclusive) and store it in new_char_val
        m_char_val = letter_val[m]
        k_char_val = letter_val[char_key[k]]
        new_char_val = m_char_val + k_char_val - 1
        #if the value of the new character is greater than 26, then subtract 26 from it to loop back to the beginning of the alphabet
        if new_char_val > 26:
            new_char_val = new_char_val - 26
        #loop through the dictionary of letters and values to find the letter than corresponds to the new_char_val, and add it to the result.
        for letter, number in letter_val.items():
            if number == new_char_val:
                result += letter
        #increment the index for the char_key list
        k += 1
    #return the result
    return result


print(encrypt("Hello", "secretkey"))
print(encrypt("World!", "secretkey"))
print(encrypt("encryption4ever", "secretkey"))
print(encrypt("someone cracked my password", "secretkey"))
print(encrypt("poor security hurts everyone", "secretkey"))

# define decrypt function to accept the message and the key as arguments
def decrypt(message, key):
    #make the message lower case
    message = message.lower()
    #make the key lower case
    key = key.lower()
    #remove any spaces in the message
    message=message.replace(" ", "")
    #remove any spaces in the key
    key=key.replace(" ", "")
    #remove special characters from message
    message = ''.join(letter for letter in message if letter.isalnum())
    # remove special characters from key
    key =''.join(letter for letter in key if letter.isalnum())
    # remove digits from message
    message=message.translate(str.maketrans('', '', digits))
    # remove digits from key
    key=key.translate(str.maketrans('', '', digits))
    # check if the key is shorter than the message.
    # while this is true append sections of the key to itself, so it's length eventually matches the length of the key.
    # this allows each letter in the message to have a corresponding letter in the key to decode it.
    while len(key) < len(message):
        diff = len(message) - len(key)
        key = key + key[:diff]
    #turn the message into a list of characters
    char_message = list(message)
    #turn the key into a list of characters
    char_key = list(key)
    #create the result variable to hold the encoded message
    result = ""
    #create temporary value to hold the index for the char_key list
    k = 0
    #for every character in the message
    for m in char_message:
        # subtract the value of the character in the message to its corresponding character in the key and add 1 (
        # because it is inclusive) and store it in new_char_val
        m_char_val = letter_val[m]
        k_char_val = letter_val[char_key[k]]
        new_char_val = m_char_val - k_char_val + 1
        # if the value of the new character is less than 0, then subtract the absolute value of it from 26 to loop back to the end of the alphabet
        if new_char_val < 1:
            new_char_val = 26 - abs(new_char_val)
        # loop through the dictionary of letters and values to find the letter than corresponds to the new_char_val,
        # and add it to the result.
        for letter, number in letter_val.items():
            if number == new_char_val:
                result += letter
        #increment the index for the char_key list
        k += 1
    #return the result
    return result


print(decrypt("srnabepakm", "brainstation"))
print(decrypt("ciubrxhrvm", "brainstation"))
print(decrypt("cvsbcjtcmqqrt", "brainstation"))
print(decrypt("qfozfwvukqhlilrbfwoekgcaf", "brainstation"))
print(decrypt("uyeyhavkuzcjowofwmfplwjrskhmyssywwu", "brainstation"))

# Part 2
#get user input on which operation to perform
operation = input("Do you want to encrypt or decrypt? ")
#get message from the user
message = input("Enter your message: ")
#get key from the user
key = input("Enter your key: ")
#if operation is to encrypt, call the encrypt function passing in the user's message and key as the parameters, and print the encrypted message
if operation.lower() == "encrypt":
    encrypted = encrypt(message, key)
    print("Your encrypted message: " + encrypted)
#if operation is to decrypt, call the decrypt function passing in the user's message and key as the parameters, and print the decrypted message
elif operation.lower() == "decrypt":
    print("Your decrypted message: " + decrypt(message, key))
else:
    print("Sorry you did not enter a valid operation. Please try again later.")

# Part 3
#list of dictionaries with user info
user_info=[{"name": "DARYL HOWLAND", "passphrase": "husky",
            "hash": "09e28e9c5875ef3b2b7463e1c9adc3cefbd35af73283f9f9281dc9b8c48f9524"},
           {"name": "MARISSA FERREIRA", "passphrase": "labrador",
            "hash": "0782cb514029008de13d7e71aa1662c310b08d0d0abb29b3220466c0f3b08c1f"},
           {"name": "TIM SUNG", "passphrase": "beagle",
            "hash": "6573818d2ffc8a09380b22a5aa517a33cca87f54e51897ee8e64b45166a76e51"},
           {"name": "SIMONE OSTERMANN", "passphrase": "dachshund",
            "hash": "e05151fd4885688b44dece508de93cfcbe7cacb262d1d3999f9287014ab5bfb7"}]

#define function to translate a password into a hash value
def get_hash(password):
    #encode the password as bytes
    password_bytes=password.encode('utf-8')
    #use SHA-256 hash function to create a hash object
    hash_object=hashlib.sha256(password_bytes)
    #get the hexadecimal representation of the hash
    password_hash=hash_object.hexdigest()
    #return the password_hash value
    return password_hash

#for every user in the list, store their entered passphrase into pw, and print whether it matched the hash value associated with their passphrase
for i in user_info:
    pw = i["passphrase"]
    isThem = (get_hash(pw) == i["hash"])
    name = i["name"]
    if isThem:
        print(f"{name} has given the corrent passphrase.")
    else:
        print(f"{name} has NOT given the correct passphrase.")
