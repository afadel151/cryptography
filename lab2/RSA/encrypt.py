import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

contenu_clepublique = RSA.importKey(open("fichier_cle_publique.pem","rb").read())
objet_cle_rsa = PKCS1_OAEP.new(contenu_clepublique)

def encrypt(message):
    return objet_cle_rsa.encrypt(message)
    

# print(contenu_clepublique)

