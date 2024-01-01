import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    password = generate_password(length)

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
