import hashlib
import base64
import getpass

def derive_password_deterministic(master_password: str, domain: str, length: int = 16) -> str:
    # Generate a deterministic hash
    salt = hashlib.sha512(domain.encode()).digest()
    derived_key = hashlib.pbkdf2_hmac('sha512', master_password.encode(), salt, 100000)
    encoded_password = base64.urlsafe_b64encode(derived_key).decode()

    # Ensure required characters
    special_chars = "@#$%&*()_-+=!?"
    uppercase = next((c for c in encoded_password if c.isupper()), 'A')
    lowercase = next((c for c in encoded_password if c.islower()), 'a')
    number = next((c for c in encoded_password if c.isdigit()), '0')
    special = special_chars[(sum(bytearray(master_password.encode())) % len(special_chars))]  # Deterministic choice

    # Fill remaining length deterministically
    required_chars = [uppercase, lowercase, number, special]
    remaining_length = length - len(required_chars)
    password_body = encoded_password[:remaining_length]  # Truncate instead of random selection

    # Combine required characters with the truncated hash
    final_password = required_chars + list(password_body)
    return ''.join(final_password)

def main():
    # Example usage
    master_password = getpass.getpass("Enter Masterpassword: ") 
    domain = input("Enter domain: ") 
    
    mp_enc = derive_password_deterministic(master_password, domain, 150)
    #print(mp_enc)
    
    dom_enc = derive_password_deterministic(mp_enc, domain, 150)
    #print(dom_enc)
    
    for r in range(1,10):
        mp_enc = derive_password_deterministic(mp_enc, dom_enc, 16)
        #print(mp_enc)
    
    print(mp_enc)
    
    #print(derive_password_deterministic(master_password, domain, 50))  # Generates a consistent password 
if __name__ == "__main__":
    main()
