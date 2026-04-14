from PIL import Image
import os

def xor_image(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Done! Output saved at: {output_path}")

def main():
    while True:
        print("\n-------------------------------")
        print("|  Image XOR Encryption Tool  |")
        print("-----------------------------------")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "3":
            print("Exiting program...")
            break

        if choice not in ["1", "2"]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        input_path = input("Enter input image path: ").strip()

        if not os.path.exists(input_path):
            print("File not found.")
            continue

        try:
            key = int(input("Enter XOR key (0-255): ").strip())
        except ValueError:
            print("Invalid key. Please enter a number between 0 and 255.")
            continue

        if not (0 <= key <= 255):
            print("Key must be between 0 and 255.")
            continue

        output_path = input("Enter output image path: ").strip()

        if choice == "1":
            xor_image(input_path, output_path, key)
            print("Image encrypted successfully.")

        elif choice == "2":
            xor_image(input_path, output_path, key)
            print("Image decrypted successfully.")

if __name__ == "__main__":
    main()
