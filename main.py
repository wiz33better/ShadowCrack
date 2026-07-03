def encrypt(text, shift):
    """Encrypts text by adding the shift value forward."""
    for j in text:
        if j.isupper():
            a = ord(j) - 65
            b = a + shift          
            c = b % 26
            d = c + 65
            print(chr(d), end="")
        elif j.islower():
            a = ord(j) - 97
            b = a + shift          
            c = b % 26
            d = c + 97
            print(chr(d), end="")
        else: 
            print(j, end="")
    print()


def decrypt_brute_force(text):
    """Decrypts text by checking all 25 possible shifts."""
    print(f"\n{'='*15} BRUTE-FORCE RESULTS {'='*15}")
    for i in range(1, 26):

        print(f"Shift [{i:2d}]: ", end="") 
        
        for j in text:
            if j.isupper():
                a = ord(j) - 65
                b = a - i
                c = b % 26
                d = c + 65
                print(chr(d), end="")
            elif j.islower():
                a = ord(j) - 97
                b = a - i
                c = b % 26
                d = c + 97
                print(chr(d), end="")
            else: 
                print(j, end="")
        print()
    print("=" * 51)


def main():
    while True:
        
        print("\n" + "*" * 40)
        print("      ShadowCrack v1.0      ")
        print("*" * 40)
        print("[E] Encrypt a Message")
        print("[D] Decrypt a Message (Brute-Force)")
        print("[Q] Quit Program")
        print("-" * 40)
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'E':
            user_text = input("\nEnter the text to ENCRYPT: ")
            
            try:
                user_shift = int(input("Enter shift value (1-25): "))
                print("\n--- Encrypted Output ---")
                encrypt(text=user_text, shift=user_shift)
                print("------------------------")
            except ValueError:
                print("\n[!] Error: Shift value must be a whole number.")
                
        elif choice == 'D':
            user_text = input("\nEnter the text to DECRYPT: ")
            decrypt_brute_force(text=user_text)
            
        elif choice == 'Q':
            print("\n Goodbye!")
            break
            
        else:
            print("\n[!] Invalid choice! Please type E, D, or Q.")


if __name__ == "__main__":
    main()
    
