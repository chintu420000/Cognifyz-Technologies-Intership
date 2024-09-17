import string
def check_password_strength(password):
    min_length = 8
    has_uppercase = any(char in string.ascii_uppercase for char in password)
    has_lowercase = any(char in string.ascii_lowercase for char in password)
    has_digit = any(char in string.digits for char in password)
    has_special_char = any(char in string.punctuation for char in password)
    if len(password) >= min_length and has_uppercase and has_lowercase and has_digit and has_special_char:
        return "Strong"
    elif len(password) >= min_length and (has_uppercase or has_lowercase) and (has_digit or has_special_char):
        return "Moderate"
    else:
        return "Weak"
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")
