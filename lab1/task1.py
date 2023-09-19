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

    message = input("Enter the message\nMessage := ")

    return option, key, message

if __name__=='__main__':
    option, key, message = user_input()
    match option:
        case "1":
            encrypted_message = ""
            for char in message:
                if char in string.whitespace:
                    encrypted_message += " " 
                elif char.isupper():
                    encrypted_message += string.ascii_uppercase[(ord(char)-65 + int(key)) % 26]  
                elif char.islower():
                    encrypted_message += string.ascii_lowercase[(ord(char)-97 + int(key)) % 26] 
            print(f"The encrypted message is {encrypted_message}") 
        case "2":
            decrypted_message = ""
            for char in message:
                if char in string.whitespace:
                    decrypted_message += " "
                elif char.isupper():
                    decrypted_message += string.ascii_uppercase[(ord(char)-65 - int(key)) % 26]
                elif char.islower():
                    decrypted_message += string.ascii_lowercase[(ord(char)-97 - int(key)) % 26]
            print(f"The decrypted message is {decrypted_message}")
        case _:
            raise Exception("The user picked an invalid argument")


