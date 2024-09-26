
def encryption(text, key):
    data = ""
    for i in text:
        ascii = ord(i) + key
        if i.isupper():
            if ascii <= ord('Z'):
                data += chr(ascii)
            else:
                data += chr(ascii + ord('A') - ord('Z') - 1)
        elif i.islower():
            if ascii <= ord('z'):
                data += chr(ascii)
            else:
                data += chr(ascii + ord('a') - ord('z') - 1)
        else:
            data += i
    return data

def decryption(text, key):
    data = ""
    for i in text:
        ascii = ord(i) - key
        if i.isupper():
            if ascii >= ord('A'):
                data += chr(ascii)
            else:
                data += chr(ascii - ord('A') + ord('Z') + 1 )
        elif i.islower():
            if ascii >= ord('a'):
                data += chr(ascii)
            else:
                data += chr(ascii - ord('a') + ord('z') + 1 )
        else:
            data += i

    return data

def main_menu():
    while True:
        print("This is Ceasar Cipher!")
        s = input("Enter your text: ")
        
        print("What do you plan to do with the text?", "\n", "Encrypt (Press 1) or Decrypt (Press 2)?")
        ch = int(input("Choice: "))
        try:
            k = int(input("Enter your Caesar key: "))
            if ch == 1:
                encrypt = encryption(s, k)
                print("Plaintext:  ", s)
                print("Ciphertext: ", encrypt)
                
            elif ch == 2:
                decrypt = decryption(s, k)
                print("Ciphertext: ", s)
                print("Plaintext:  ", decrypt)

            else:
                print("Invalid Choice! ")
        except ValueError as e:
            print("Enter an integral Caesar Key!")
        print("Continue? (Y/N)")
        
        cho = input("Choice: ")
        if cho in ('N', 'n'):
            print("Exited successfully!")
            break

main_menu()
