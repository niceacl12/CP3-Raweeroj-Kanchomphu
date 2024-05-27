UsernameInput = input("Username: ")
PasswordInput = input("Password: ")
UsernameSignIn = input("Username: ")
PasswordSignIn = input("Password: ")

if UsernameInput == UsernameSignIn and PasswordInput == PasswordSignIn:
    print("Sign in")
    print("-----LignitrShop-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    UserSelected = int(input("Your Choice (Number only) is: "))
    if UserSelected == 1:
        price = int(input("Price (THB): "))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif UserSelected == 2:
        price1 = int(input("First Product Price: "))
        price2 = int(input("Second Product Price: "))
        print(price1+price2)
else:
    print("Your username or password incorrect")