import socket

from encrypt import encrypt

SocketClient = socket.socket()
host = socket.gethostname()
port = 9500
SocketClient.connect(("127.0.0.1", port))
Cle_publique=b""



while True:
    recu=SocketClient.recv(1024)
    Cle_publique+=recu
    if b'-----END PUBLIC KEY-----' in Cle_publique:
        break


print("Lancement serveur")
while True:
    message=input()
    crypted = encrypt(message)
    # Chiffre le message lu du clavier (MessageATransmettre)
    # Utilisez la methode encrypt de objet_cle_rsa_publique
    # Mettez le resultat dans resultat_chiffre
    # (A FAIRE 2) ajoutez l'instruction dans cette ligne
    SocketClient.send(crypted)


    if(crypted==b"Fin"):
        print( "Deconnexion ")
        break
# ConnexionAUnClient.close()