import sys
from menu.EcriptionDecryption import EncryptionDecryption


#main menu
encode_decode = EncryptionDecryption()

while True:
    try:
        encode_decode.clear()
        choice = int(input("""Enter your choice : 
         1. Encryption
         2. Decryption
         3. Exit\n\n"""))
    except ValueError:
        print("Invalid choice...")
        encode_decode.redisplay_menu_options()
        continue

    if choice == 1:
        encode_decode.encryption_choice()

    elif choice == 2:
        encode_decode.decryption_choice()

    elif choice == 3:
        print("Exiting...")
        sys.exit()
    else:
        print("You have not selected the valid choice...\nPlease try to select the valid choice...")
    encode_decode.redisplay_menu_options()
