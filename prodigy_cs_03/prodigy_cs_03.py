import re


def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character like !, @, #, $, etc.")

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, suggestions


def main():
    print("\n-------------------------------")
    print("|  Password Strength Checker  |")
    print("-------------------------------")
    while True:
        print("\n1. Check Password")
        print("2. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "2":
            print("Goodbye.")
            break

        elif choice == "1":
            password = input("\nEnter password: ").strip()

            if not password:
                print("Please enter a password.")
                continue

            strength, suggestions = check_password(password)
            
            print("\n--------------------------------------------------------------------")
            print("Analysis of password:")
            print("Password:", password)
            print("Strength:", strength)

            if suggestions:
                print("\nRecommendations to improve your password:")
                for tip in suggestions:
                    print("-", tip)
                print("\n--------------------------------------------------------------------")
            else:
                print("\nExcellent! Your password meets all checks.")
                print("\n--------------------------------------------------------------------")

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
