import string

def user_input():
    option = input("Choose the option:\n\t1. Encrypt\n\t2. Decrypt\nOption := ")
    while option not in ["1", "2"]:
        print("Please choose a valid option") 
        option = input("Choose the option:\n\t1. Encrypt\n\t2. Decrypt\nOption := ")

    key = input("Enter a key from the range [1...25]\nKey := ")
    while int(key) not in range(1, 26):
        print("Please choose a key from the given range")
        key = input("Enter a key from the range [1...25]\nKey := ")

    permutation_key = input("Enter the permutation key\nPermutation := ")
    while len(permutation_key) > 26:
        print("Please enter a key with the length less than 26 characters") 
        permutation_key = input("Enter the permutation key\nPermutation := ")

    message = input("Enter the message\nMessage := ")

    return option, key, permutation_key, message

if __name__=='__main__':
    option, key, permutation_key, message = user_input()
    #alphabet_uppercase = string.ascii_uppercase.replace(string.ascii_uppercase[:len(permutation_key)], permutation_key.upper())
    #alphabet_lowercase = string.ascii_lowercase.replace(string.ascii_lowercase[:len(permutation_key)], permutation_key.lower())
    alphabet_uppercase = string.ascii_uppercase 
    alphabet_lowercase = string.ascii_lowercase 
    for i, char in enumerate(permutation_key):
        alphabet_uppercase = alphabet_uppercase.replace(permutation_key[i], string.ascii_uppercase[i], 1).replace(alphabet_uppercase[i], permutation_key[i], 1)
        alphabet_lowercase = alphabet_lowercase.replace(permutation_key[i], string.ascii_lowercase[i], 1).replace(alphabet_lowercase[i], permutation_key[i], 1)
    print(alphabet_uppercase, alphabet_lowercase)
    match option:
        case "1":
            encrypted_message = ""
            for char in message:
                if char in string.whitespace:
                    encrypted_message += " " 
                elif char.isupper():
                    encrypted_message += alphabet_uppercase[(ord(char)-65 + int(key)) % 26]  
                elif char.islower():
                    encrypted_message += alphabet_lowercase[(ord(char)-97 + int(key)) % 26] 
            print(f"The encrypted message is {encrypted_message}") 
        case "2":
            decrypted_message = ""
            for char in message:
                if char in string.whitespace:
                    decrypted_message += " "
                elif char.isupper():
                    decrypted_message += alphabet_uppercase[(ord(char)-65 - int(key)) % 26]
                elif char.islower():
                    decrypted_message += alphabet_lowercase[(ord(char)-97 - int(key)) % 26]
            print(f"The decrypted message is {decrypted_message}")
        case _:
            raise Exception("The user picked an invalid argument")


