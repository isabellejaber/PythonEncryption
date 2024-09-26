Create a Python Encryption & Decryption Tool

In this deliverable I utilizes Python to create a Simple Text Encryption and Decryption Tool.


Part 1

Wrote functions to encrypt and decrypt text using a Vignere Cipher, given a single word as a secret key. My function will handle uppercase letters and remove spaces, special characters, and numbers from both the message and the key.

For example, if the message was welcome to brainstation and the secret key was cybersecurity, the encrypted text would be ycmgfeivisztgpquekasp. As well, if the encrypted text was ycmgfeivisztgpquekasp and the secret key was cybersecurity, the decrypted text would be welcometobrainstation

Encrypt the following text with the key: secretkey
"Hello"
"World!"
"encryption4ever"
"someone cracked my password"
"poor security hurts everyone"
Decrypt the following encrypted text with the key brainstation
"srnabepakm"
"ciubrxhrvm"
"cvsbcjtcmqqrt"
"qfozfwvukqhlilrbfwoekgcaf"
"uyeyhavkuzcjowofwmfplwjrskhmyssywwu"


Part 2
I modified my program to receive input from the user using the command line. User should receive the following:

The direction as to whether they are encrypting or decrypting
The text to encrypt/decrypt
Secret key to shift the message


Part 3

Scenario: A company is in the midst of a security overhaul. Before all their new security policies have been instigated, they've implemented a "passphrase for authentication" system where when a user is in need of assistance, they must give you their passphrase. I must check that the passphrase given is the same as the passphrase that is stored. I have a list of these passphrases on hand, but all the passphrases are hashed to ensure security and privacy.

Using the hashlib library, I created a function that will hash a passphrase using the SHA-256 hashing algorithm.

Using the following information, I determined whether the following users are who they say they are:

| NAME OF USER	        |PASSPHRASE GIVEN	        |HASH STORED
|-----------------------|-------------------------|-----------------------------------------------------------------
|DARYL HOWLAND	        |husky	                  |09e28e9c5875ef3b2b7463e1c9adc3cefbd35af73283f9f9281dc9b8c48f9524
|MARISSA FERREIRA	    	|labrador	                |0782cb514029008de13d7e71aa1662c310b08d0d0abb29b3220466c0f3b08c1f
|TIM SUNG	            	|beagle	                  |6573818d2ffc8a09380b22a5aa517a33cca87f54e51897ee8e64b45166a76e51
|SIMONE OSTERMANN	     	|dachshund	              |e05151fd4885688b44dece508de93cfcbe7cacb262d1d3999f9287014ab5bfb7

I wrote a function that will check the hashed passphrase to the hash stored, generate the appropriate boolean, and prints a statement indicating whether the user has given the proper passphrase or not.
