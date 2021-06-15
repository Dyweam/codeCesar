#Projet de développement d'un logiciel de chiffrement en python avec le module Tkinter
#Réalisé par Pierre VASSEUR, en collaboration avec Jawad EL ABDI
#Date de création : 15/06/2021
#Dernière mise à jour : 15/06/2021

#Importation de la bibliothèque Tkinter
from tkinter import *

#Création de la fenêtre du logiciel
window = Tk()

#Titre de la fenêtre du logiciel
window.title("Code César")
#Dimensions de la fenêtre (en pixel)
window.geometry("720x480")
#Dimensions minimales de la fenêtre (en pixel)
window.minsize(480, 360)
#Icône de la fenêtre du logiciel
window.iconbitmap("cesar.ico")

#Création d'un frame dans la fenêtre du logiciel
frame = Frame(window)

#Label titre du logiciel
label_title = Label(frame, text = "Logiciel de chiffrement", font = ("Arial", 32))
#Placement du label dans la fenêtre du logiciel
label_title.pack(side = "top")

#Label du message à crypter
label_message = Label(frame, text = "Entrez votre message à crypter : ", font = ("Arial", 12))
#Placement du label dans la fenêtre du logiciel
label_message.pack()
#Zone d'entrée de texte pour le message de l'utilisateur
entry_message = Entry(frame, font = ("Arial", 12))
#Placement de la zone d'entrée de texte
entry_message.pack()

#Label du message à crypter
label_cle = Label(frame, text = "Entrez votre clé de cryptage : ", font = ("Arial", 12))
#Placement du label dans la fenêtre du logiciel
label_cle.pack()
#Zone d'entrée de texte pour le message de l'utilisateur
entry_cle = Entry(frame, font = ("Arial", 12))
#Placement de la zone d'entrée de texte
entry_cle.pack()

#Label du message crypté
label_crypted = Label(frame, text = "Votre message crypté apparaîtra ici", font = ("Arial", 12), fg = "green")
label_crypted.pack()

#Fonction du code césar
def cesarCode():
    #listMin de l'alphabet en minuscules
    listMin=['a','b','c','d','e','f','g','h','i','j','k','m','n','l','o','p','q','r','s','t','u','v','w','x','y','z']
    #listMin de l'alphabet en majuscules
    listCap=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    message = entry_message.get()
    cle = int(entry_cle.get())
    message_code = str()

    for lettre in message:
        if lettre not in listMin and lettre not in listCap:
            message_code += lettre
        else:
            for alphabetMinLettre in listMin:
                if(lettre == alphabetMinLettre):
                    for i in range (len(listMin)):
                        if listMin[i]==lettre:
                            message_code += str(listMin[(i+cle) % 26])
            
            for alphabetCapLettre in listCap:
                if(lettre == alphabetCapLettre):
                    for i in range (len(listCap)):
                        if listCap[i]==lettre:
                            message_code += str(listCap[(i + cle) % 26])

    label_crypted['text'] = message_code

#Bouton "submit" afin de crypter le message
bt_submit = Button(frame, text = "Crypter", font = ("Arial", 12), command = cesarCode)
bt_submit.pack()

#Copyright
label_copyright = Label(window, text = "Projet réalisé par Pierre VASSEUR & Jawad EL ABDI", fg = "blue")
label_copyright.pack(side="bottom")

#Placement de la frame dans la fenêtre du logiciel
frame.pack(expand = "yes")

#Affichage de la fenêtre
window.mainloop()