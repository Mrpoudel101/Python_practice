
def welcome():
    print("----Welcome to Caesar Cipher----")  
    print("----This program encrypts and decrypts text using Caesar Cipher.----")
welcome()

def main():
   
    def Enter_Message():
        # asking user for encryption and decryption
        user_input = input("Would you like to encrypt or decrypt? enter 'EN' to ENCRYPT, 'DY' to DECRYPT: \n ").upper()           
            #for encryption
        if user_input == "EN":
            def encrypt():
             print("----ENCRYPTION start----")
             # ask message to encrypt
             Encrypt_Text = input('enter your text for encryption: \n' ).upper()
             Shift_Num = int(input("enter the shift number: ")) # shift number input
             encrypt_output = ""
             for i in range(len(Encrypt_Text)):
                    encrypt_value = Encrypt_Text[i]

                    if encrypt_value == " ":
                        encrypt_output += " "
                    else:
                        encrypt_output += chr((ord(encrypt_value) + Shift_Num - 65)%26+65)
            
             print("The encrypted code is :-\n", encrypt_output)  # display result
                
            encrypt()
            # for decryption
        elif user_input == "DY":
            print("----DECRYPTION Start----")
            def decrypt():
             Decrypt_text = input(
                 'enter your text for decryption: \n').upper()  # asking text
             # asking shift number
             Shift_Num = int(input("enter the shift number: "))
             decrypt_output = ""
             for i in range(len(Decrypt_text)):
                decrypt_value = Decrypt_text[i]

                if decrypt_value == " ":
                  decrypt_output += " "

                else:
                    decrypt_output += chr((ord(decrypt_value) -  Shift_Num - 65) % 26 + 65)

             print("The decrypted code is :- \n",
                   decrypt_output)  # display result

            decrypt()
            # for the wrong input
        else:
            print(
                "invalid entry, enter en to ENCRYPT, dy to DECRYPT, exit to EXIT the program ")
            decide = input('try again Y for YES, N for NO: \n').upper()
            if decide == 'Y':
                main()
            else:
                print("Thank You for Using")
            
            Enter_Message()
            
            
    Enter_Message()
     #for asking user to run programe.
    def restart():
        Restart = input(
            "Would you like to continue this program? (Y/N):- ").upper()
        if Restart == "Y":
                main()
        elif Restart == "N":
                print("Thank You For Using!")
            
        else:
                print("Invalid input! Please try again")
                restart()
    restart()
main()