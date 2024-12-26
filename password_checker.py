import re

def check_password_strength(password):
    # Check for minimum length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Check for character variety
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_+=<>?/{}[]~" for char in password)

    if not (has_upper and has_lower and has_digit and has_special):
        return "Moderate: Add uppercase, lowercase, digits, and special characters."

    # Check for common patterns
    common_patterns = ["12345", "password", "qwerty", "abc123"]
    if any(pattern in password.lower() for pattern in common_patterns):
        return "Weak: Avoid common patterns like 'password' or '12345'."

    return "Strong: Your password is secure!"

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    result = check_password_strength(password)
    print(result)
