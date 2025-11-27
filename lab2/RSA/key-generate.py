from Crypto.PublicKey import RSA


cle= RSA.generate(2048)


cle_prive = cle.exportKey()
Fichier = open("fichier_cle_prive.pem", "wb")
Fichier.write(cle_prive)
Fichier.close()

cle_publique = cle.publickey().exportKey()
Fichier = open("fichier_cle_publique.pem", "wb")
Fichier.write(cle_publique)
Fichier.close()

print(cle_publique)
print(cle_prive)