import socket
import _thread as thread
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from decrypt import decrypt
def Traiter_Connexion(connexion_avec_client,adresse_client):
    # global objet_cle_rsa_prive,contenu_clepublique
    MessageRec=b""

    print ("Connexion de la machine = ", adresse_client)
    try:
        while True:
            MessageRec=connexion_avec_client.recv(1024)
            # Dechiffre le message recu (MessageRec)
            # Utilisez la methode decrypt de la cle prive (objet_cle_rsa_prive)
            # Affectez le resulta du dechiffrement a MessageRec
            # (A FAIRE 2) ajoutez l'instruction dans cette ligne
            clair = decrypt(MessageRec)
            if MessageRec==b"Fin":
                break

            print("Client" ,adresse_client," a dit :",clair)
    except:
        print("Deconnexion")
    print("Deconnexion de :",adresse_client)
    try:
        connexion_avec_client.close()
    except:
        pass


SocketServeur = socket.socket()
host = socket.gethostname()
port = 9500
SocketServeur.bind(("127.0.0.1", port))

SocketServeur.listen(5)

# contenu_clepublique = open("fichier_cle_publique.pem","rb").read()
# contenu_cleprive = RSA.importKey(open("fichier_cle_prive.pem","rb").read())

# objet_cle_rsa_prive = PKCS1_OAEP.new(contenu_cleprive)

print("Lancement serveur")

while True:
    ConnexionAUnClient, addrclient = SocketServeur.accept()
    thread.start_new_thread(Traiter_Connexion,(ConnexionAUnClient,addrclient))