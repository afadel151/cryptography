from Crypto.Cipher import AES

input_file = "encrypted_file.bin"
output_file = "decrypted_text.txt"
key_file = "key.bin"

with open(key_file, "rb") as f:
    cle_16_octet = f.read()

with open(input_file, "rb") as f:
    contenu_chiffre = f.read()

bourrage = contenu_chiffre[0]
print("Bourrage à enlever :", bourrage)

aes = AES.new(cle_16_octet, AES.MODE_ECB)
contenu_dechiffre = aes.decrypt(contenu_chiffre[1:])

if bourrage > 0:
    contenu_dechiffre = contenu_dechiffre[:-bourrage]

with open(output_file, "wb") as f:
    f.write(contenu_dechiffre)

print("Complete")
