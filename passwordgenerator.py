import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("\n PASSWORD GENERATOR ")

    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Password length should be at least 4.")
            return

        upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        digits = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, upper, lower, digits, symbols)
       
        if password:
            print("\n Generated Password:", password)
            print("DONE BY CHETAN REDDY")
        else:
            print(" You must select at least one character type.")

    except ValueError:
        print(" Please enter a valid number.")


if __name__ == "__main__":
    main()
