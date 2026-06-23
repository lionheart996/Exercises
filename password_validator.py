
def password_validator(password):
    valid = 'Password is valid'
    if len(password) < 6 or len(password) > 10:
        valid = "Password must be between 6 and 10 characters"
    if not password.isalnum():
        valid += "\nPassword must have at least 2 digits"
    digit_count = 0

    for ch in password:
        if ch.isdigit():
            digit_count += 1

    if digit_count < 2:
        valid += "\nPassword must have at least 2 digits"
    return valid

print(password_validator("MyPass123"))