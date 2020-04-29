'''
@author Akansh Jha
@date Apr 23rd, 2020
'''
import sys
from os import system, name


class EncryptionDecryption:

    @staticmethod
    def encryption_choice():
        print("We are ready to encrypt your file/text...")
        string_or_filepath = EncryptionDecryption.choose_file_or_string()

    @staticmethod
    def decryption_choice():
        print("We are ready to decrypt your file/text...")
        EncryptionDecryption.choose_file_or_string()

    @staticmethod
    def clear():  # define our clear function
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux. here os.name = 'posix'
        else:
            _ = system('clear')

    @staticmethod
    def redisplay_menu_options():
        next_choice = input("""\n\nHit 'm' for the menu...
Hit any other key to exit...\n\n""")
        if next_choice != 'm' or next_choice != 'M':
            print("Exiting...")
            sys.exit()

    @staticmethod
    def choose_file_or_string():
        try:
            file_or_string_choice = int(input("""\nHow would you like us to perform the operation..
            1. Using File.
            2. Using String
            We recommend you to use files.\n\n"""))
        except ValueError:
            print("Invalid Choice.\nPlease try to select the valid choice..")
            EncryptionDecryption.choose_file_or_string()

        if file_or_string_choice == 1:
            return input("\nPlease give us full path to that file..\n")
        elif file_or_string_choice == 2:
            return input('Type in the string in a single line. you want to get it performed on..\n')
        else:
            print('You have not selected the valid choice.\nPlease try to select the valid choice..')
            EncryptionDecryption.choose_file_or_string()

# main code :
# while True:
#     try:
#         __clear()
#         choice = int(input("""Enter your choice :
#          1. Encryption
#          2. Decryption
#          3. Exit\n\n"""))
#     except ValueError:
#         print("Invalid choice...")
#         __redisplay_menu_options()
#         continue
#
#     if choice == 1:
#         __encryption_choice()
#
#     elif choice == 2:
#         __decryption_choice()
#
#     elif choice == 3:
#         print("Exiting...")
#         sys.exit()
#     else:
#         print("You have not selected the valid choice...\nPlease try to select the valid choice...")
#     __redisplay_menu_options()
