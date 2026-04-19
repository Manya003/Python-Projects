# Password Validator

password = input("Enter password: ")

if len(password) < 8:
    print("Invalid password: Must be at least 8 characters long")

elif " " in password:
    print("Invalid password: Should not contain spaces")

elif not any(char.islower() for char in password):
    print("Invalid password: Must contain a lowercase letter")

elif not any(char.isupper() for char in password):
    print("Invalid password: Must contain an uppercase letter")

elif not any(char.isdigit() for char in password):
    print("Invalid password: Must contain a number")

elif not any(char in "@#$%^&*!" for char in password):
    print("Invalid password: Must contain a special character")

else:
    print("Valid password")