import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP





contenu_cleprive = RSA.importKey(open("fichier_cle_prive.pem","rb").read())
objet_cle_rsa_prive = PKCS1_OAEP.new(contenu_cleprive)


def decrypt(message):
    return objet_cle_rsa_prive.decrypt(message)