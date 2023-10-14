import string

class VigenereAlgorithm:
    _key = None
    _text = None

    _alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"

    @staticmethod
    def get_alphabet() -> str:
        return VigenereAlgorithm._alphabet

    @staticmethod
    def set_alphabet(alphabet: str) -> None:
        VigenereAlgorithm._alphabet = alphabet

    @staticmethod
    def get_key() -> str:
        return VigenereAlgorithm._key

    @staticmethod
    def set_key(key: str) -> None:
        VigenereAlgorithm._key = key

    @staticmethod
    def get_text() -> str:
        return VigenereAlgorithm._text

    @staticmethod
    def set_text(text: str) -> None:
        VigenereAlgorithm._text = text

    @staticmethod
    def encrypt() -> str:
        return "".join(VigenereAlgorithm.get_alphabet()[(VigenereAlgorithm.get_alphabet().index(VigenereAlgorithm.get_text()[i]) + VigenereAlgorithm.get_alphabet().index(VigenereAlgorithm.get_key()[i % len(VigenereAlgorithm.get_key())])) % len(VigenereAlgorithm.get_alphabet())] for i in range(len(VigenereAlgorithm.get_text())))

    @staticmethod
    def decrypt() -> str:
        return "".join(VigenereAlgorithm.get_alphabet()[(VigenereAlgorithm.get_alphabet().index(VigenereAlgorithm.get_text()[i]) - VigenereAlgorithm.get_alphabet().index(VigenereAlgorithm.get_key()[i % len(VigenereAlgorithm.get_key())])) % len(VigenereAlgorithm.get_alphabet())] for i in range(len(VigenereAlgorithm.get_text())))


if __name__ == "__main__":
    print("Vigenère Cipher Algorithm 1.0")

    key = input("Enter key: ").strip()
    while len(key) < 7:
        print("Invalid key was provided. Please enter a key with the minimal length of 7 characters.")
        key = input("Enter key: ").strip()

    char = None
    text = input("Enter text: ").strip().translate({ord(c): None for c in string.whitespace})
    while len(text) < 1 or len([char := c for c in text if c.upper() not in VigenereAlgorithm.get_alphabet()]):
        if char:
            print(f"Invalid character at position: {text.index(char)+1}.") 
            print(f"Please enter the text using the following alphabet:\n\t{VigenereAlgorithm.get_alphabet()}")
        text = input("Enter text: ").strip().translate({ord(c): None for c in string.whitespace})

    print("Options:\n\t1. Encrypt\n\t2. Decrypt")
    option = input("Enter action: ").strip()
    while option not in ["1", "2"]:
        print("Invalid option was provided. Please enter an option from the list above.")
        option = input("Enter action: ").strip()

    VigenereAlgorithm.set_key(key.upper())
    VigenereAlgorithm.set_text(text.upper())
    match option:
        case "1":
            encrypted_text = VigenereAlgorithm.encrypt()
            print(f"Encrypted text: {encrypted_text}")
        case "2":
            decrypted_text = VigenereAlgorithm.decrypt()
            print(f"Decrypted text: {decrypted_text}")
        case _:
            raise Exception("Invalid option was chosen.")
