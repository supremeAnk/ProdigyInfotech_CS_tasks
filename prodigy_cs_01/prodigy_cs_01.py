def caesar(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def getShift():
    while True:
        try:
            shift = int(input("  Enter shift key (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("  Invalid! Shift must be between 1 and 25.")
        except ValueError:
            print("  Invalid! Please enter a number.")


def showResult(label, text):
    print(f"\n  {label + ':'}")
    print(f"  {text}")


def main():
    print("\n------------------------")
    print("|  Caesar Cipher Tool  |")
    print("------------------------")

    while True:
        print("\n  1. Encrypt")
        print("  2. Decrypt")
        print("  3. Exit")
        choice = input("\n  Enter choice (1/2/3): ").strip()

        if choice == "1":
            message = input("\n  Enter message to encrypt: ")
            shift = getShift()
            encrypted = caesar(message, shift, "encrypt")
            showResult("Encrypted", encrypted)

        elif choice == "2":
            cipher = input("\n  Enter cipher to decrypt: ")
            shift = getShift()
            decrypted = caesar(cipher, shift, "decrypt")
            showResult("Decrypted", decrypted)

        elif choice == "3":
            print("\n  Goodbye!\n")
            break

        else:
            print("\n  Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
