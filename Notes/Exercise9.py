UsernameInput = input("Username: ")
PasswordInput = input("Password: ")

while UsernameInput != "admin" or PasswordInput != "1234":
    UsernameInput = input("Username: ")
    PasswordInput = input("Password: ")
    
print("Sign in")