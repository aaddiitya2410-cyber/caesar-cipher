print(" Caesar Cipher Tool ")
choice = input("Kya karna chahte hain? (1 for Encrypt, 2 for Decrypt): ")


encrypt_rules = {"a": "b", "b": "c", "c": "d","d": "e","e": "f", "f": "g","g": "h", "h": "i", "l": "m", "o": "p"}


decrypt_rules = {"b": "a", "c": "b", "d": "c", "i": "h", "m": "l", "p": "o"}

if choice == "1":
    text = input("Encrypt karne ke liye text likhe : ")
    result = ""
    for char in text:
        if char in encrypt_rules:
            result += encrypt_rules[char] 
        else:
            result += char               
    print("Encrypted Code:", result)

elif choice == "2":
    text = input("Decrypt karne ke liye code likhe : ")
    result = ""
    for char in text:
        if char in decrypt_rules:
            result += decrypt_rules[char] 
        else:
            result += char                
    print(" Decrypted code:", result)

else:
    print("Wrong choice! Sirf 1 ya 2 likhein.")

