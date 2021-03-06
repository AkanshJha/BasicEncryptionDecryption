'''
@author Akansh Jha
@date Apr 23rd, 2020
'''
import _io
import string
import sys
from os import system, name
import time
from pathlib import Path
import random


class EncryptionDecryption:
    len_of_ran_string = 5

    @staticmethod
    def encryption_choice():
        print("We are ready to encrypt your file/text...")
        string_or_filepath, file_dir = EncryptionDecryption.__choose_file_or_string()
        print(file_dir)
        N = EncryptionDecryption.len_of_ran_string
        rand_alphanum = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        if isinstance(string_or_filepath, _io.TextIOWrapper):
            print("File Type.")
            data = string_or_filepath.read()
            # print(data)
            # Generating Random AlphaNumeric String of length 5
            print(rand_alphanum)
            write_file = open("{}//encoded.txt".format(file_dir), "w")
            # writing this random alphanumeric string to the file
            write_file.write(rand_alphanum)
            write_file.write("".join(tuple(EncryptionDecryption.__encode_data(data))))
            # EncryptionDecryption.__encode_data(data)
            write_file.close()
        elif isinstance(string_or_filepath, str):
            print("string type.")
            stored_in_list = tuple(EncryptionDecryption.__encode_data(string_or_filepath))
            print("Encrypted String for given string is '{}".format(rand_alphanum), end='')
            print("".join(stored_in_list), end="'.")
            print("\nPlease copy this encoded string.")

    @staticmethod
    def __encode_data(content):
        for i in content:
            encoded = chr(ord(i)+1)
            yield encoded

    @staticmethod
    def __decode_data(content):
        for i in content:
            decoded = chr(ord(i)-1)
            yield decoded

    @staticmethod
    def decryption_choice():
        print("We are ready to decrypt your file/text...")
        string_or_filepath, file_dir = EncryptionDecryption.__choose_file_or_string()
        N = EncryptionDecryption.len_of_ran_string
        if isinstance(string_or_filepath, _io.TextIOWrapper):
            print("File Type.")
            string_or_filepath.read(N)
            data = string_or_filepath.read()
            write_file = open("{}//decoded.txt".format(file_dir), "w")
            write_file.write("".join(tuple(EncryptionDecryption.__decode_data(data))))
            EncryptionDecryption.__decode_data(data)
        elif isinstance(string_or_filepath, str):
            print("string type.")
            # slicing the string string_or_filepath[EncryptionDecryption.len_of_ran_string::]
            stored_in_tuple = tuple(EncryptionDecryption.__decode_data(string_or_filepath[EncryptionDecryption.len_of_ran_string::]))
            print("Decoded string is '", end='')
            print("".join(stored_in_tuple),end="'.")
            print("\n")

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
        if next_choice != 'm':
            EncryptionDecryption.terminate_execution()
        # elif next_choice != 'M':
        #     EncryptionDecryption.terminate_execution()

    @staticmethod
    def terminate_execution():
        print("Exiting...")
        time.sleep(3)
        sys.exit()

    @staticmethod
    def __choose_file_or_string():
        try:
            file_or_string_choice = int(input("""\nHow would you like us to perform the operation..
            1. Using File.
            2. Using String
            We recommend you to use files.\n\n"""))
        except ValueError:
            print("Invalid Choice.\nPlease try to select the valid choice..")
            EncryptionDecryption.__choose_file_or_string()

        if file_or_string_choice == 2:
            string = input('Type in the string in a single line. you want to get it performed on..\n')
            return string, None
        elif file_or_string_choice == 1:
            file_path = input("\nPlease give us full path to that file..\n")
            file_dir = Path(file_path).parent
            #print(EncryptionDecryption.fil)
            try:
                file = open(file_path, 'r')
                return file, file_dir
            except FileNotFoundError:
                print("You might have not given the correct file path.\nPlease check and choose option again.\n")
                EncryptionDecryption.__choose_file_or_string()
            except:
                print("Some error occurred. Please try to choose the option again.\n")
                EncryptionDecryption.__choose_file_or_string()
        else:
            print('You have not selected the valid choice.\nPlease try to select the valid choice..')
            EncryptionDecryption.__choose_file_or_string()


# main code :
while True:
    try:
        EncryptionDecryption.clear()
        choice = int(input("""Enter your choice :
         1. Encryption
         2. Decryption
         3. Exit\n\n"""))
    except ValueError:
        print("Invalid choice...")
        EncryptionDecryption.redisplay_menu_options()
        continue

    if choice == 1:
        EncryptionDecryption.encryption_choice()

    elif choice == 2:
        EncryptionDecryption.decryption_choice()

    elif choice == 3:
        EncryptionDecryption.terminate_execution()
    else:
        print("You have not selected the valid choice...\nPlease try to select the valid choice...")
    EncryptionDecryption.redisplay_menu_options()