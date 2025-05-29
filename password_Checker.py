import re

# Load common passwords
with open("C:/cybersecurity/google/project/password_checker/common_passwords.txt") as f:
    common_passwords = set(p.strip() for p in f.readlines())

# Ask user to enter a password
password = input("Enter a Password to check its strength:\n")


# Error checks
length_error = len(password) < 8
uppercase_error = re.search(r"[A-Z]", password) is None
lowercase_error = re.search(r"[a-z]", password) is None
digit_error = re.search(r"\d", password) is None
specialcase_error = re.search(r"[!@#$%^&*()><:;{}]", password) is None  # fixed special characters

# Output suggestions
if length_error:
    print("X Password is too short. Minimum 8 characters required.")
if uppercase_error:
    print("Add at least one uppercase letter.")
if lowercase_error:
    print("Add at least one lowercase letter.")
if specialcase_error:
    print("Add at least one special character.")
if digit_error:
    print("Add at least one number.")

# Check against common passwords
if password in common_passwords:
    print("X This password is too common, try another password.")

# Final strength message
if not (length_error or uppercase_error or lowercase_error or digit_error or specialcase_error or password in common_passwords):
    print("Password is strong.")

#Calculate strength score and label
score = 0
if not length_error:
    score += 1
if not uppercase_error:
    score += 1
if not lowercase_error:
    score += 1
if not digit_error:
    score += 1
if not specialcase_error:
    score += 1

if password in common_passwords:
    strength = "Very Weak"
elif score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

print(f"\n🔒 Password Strength: {strength}")    
