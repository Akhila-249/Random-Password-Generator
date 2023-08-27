import random
import string

def generate_random_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    all_characters = lowercase_letters + uppercase_letters + digits + punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("Random Password Generator")
    
    try:
        password_length = int(input("Enter desired password length: "))
        
        if password_length <= 0:
            print("Password length must be positive.")
            return
        
        password = generate_random_password(password_length)
        print("Generated Password:", password)
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
