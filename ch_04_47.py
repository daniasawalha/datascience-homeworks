
import string

password_str = input("Enter your password: ")

uppercase = False
lowercase = False
digits = False

for ch in password_str:
    if ch in string.ascii_uppercase:
        uppercase = True
    if ch in string.ascii_lowercase:
        lowercase = True
    if ch in string.digits:
        digits = True
        
if uppercase and lowercase and digits and 6 <= len(password_str) <= 20:
    print('Valid password.')
else:
    print('Invalid password.')