import base64

choice = str(input("Do you want to encrpyt or decrypt your password?(e/d): "))
if choice=='e':
    password = input("Enter your password: ")
    print("Your encrypted password is: {}".format(base64.b64encode(bytes(password,'utf-8'))))
elif choice=='d':
    decrypt = input("Enter your encrypted password: ")
    print("Your decrypted password is: {}".format(base64.b64decode(bytes(decrypt,'utf-8'))))