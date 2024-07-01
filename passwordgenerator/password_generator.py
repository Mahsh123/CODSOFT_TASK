import random
import string

def generate_password(length):
    
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation  

    
    all_characters = lower_case + upper_case + digits + symbols


    password = ''.join(random.sample(all_characters, length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be greater than zero.")
            password = generate_password(length)
            print("Generated Password:", password)
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid positive integer for length.")

if __name__ == "__main__":
    main()
