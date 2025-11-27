
from Crypto.Cipher import AES


input_file = "text_to_hash.txt"   
output_file = "encrypted_file.bin"   
key_file = "key.bin"                 

with open(input_file, "rb") as f:
    content = f.read()

taille_originale = len(content)
bourrage = (16 - (taille_originale % 16)) % 16 



print("bourrage", bourrage)
content += bytes([0x00] * bourrage)
cle_16_octet = b"fadelakram123456"



with open(key_file, "wb") as f:
    f.write(cle_16_octet)

aes = AES.new(cle_16_octet, AES.MODE_ECB)
contenu_chiffre = aes.encrypt(content)

contenu_final = bytes([bourrage]) + contenu_chiffre
with open(output_file, "wb") as f:
    f.write(contenu_final)

print(f"{bourrage} octets de bourrage.")

