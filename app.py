#Projet de développement d'un logiciel de chiffrement en python avec le module Tkinter
#Réalisé par Pierre VASSEUR, en collaboration avec Jawad EL ABDI
#Date de création : 15/06/2021
#Dernière mise à jour : 15/06/2021

#Importation de la bibliothèque Tkinter
from tkinter import *
#Importation d'un sous-module Tkinter
from tkinter.filedialog import *

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

#Label du chemin de fichier à selectionner
label_import = Label(frame, text = "Ou importez un fichier au format .txt : ", font = ("Arial", 12))
#Placement du label dans la fenêtre du logiciel
label_import.pack()

#Définition de la variable "FILETYPES" (Le format du fichier devra être un .txt)
FILETYPES = [ ("text files", "*.txt") ]
#Définition de la variable "filename" qui permettra de récupérer le chemin du fichier .txt
filename = StringVar(window)

#Fonction permettant de récupérer le chemin du fichier au format .txt
def set_filename():
    filename.set(askopenfilename(filetypes=FILETYPES))
    print(filename.get())

#Bouton permettant d'aller chercher un fichier au format .txt  
button_filePath = Button(frame, text='Parcourir', command=set_filename)
#Placement du bouton dans la fenêtre du logiciel
button_filePath.pack()

#Ouverture du fichier au format .txt désiré
def read_filename():
    #La variable fileOpen ouvre le fichier choisi en mode lecture
    fileOpen = open(filename.get(), 'r')
    #Retourne le contenu du fichier texte
    return fileOpen.read()

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
#Placement du label dans la fenêtre du logiciel
label_crypted.pack()

#Fonction du code césar
def cesarCode():
    #listMin de l'alphabet en minuscules
    listMin=['a','b','c','d','e','f','g','h','i','j','k','m','n','l','o','p','q','r','s','t','u','v','w','x','y','z']
    #listMin de l'alphabet en majuscules
    listCap=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    #Initialisation de la variable "message" en indiquant qu'il s'agit d'un string
    message = str()

    #Si la zone d'entrée de texte n'est pas vide
    if entry_message.get() != '':
        #La variable message prend comme valeur ce qui a été entré dans la textbox "entry_message"
        message = entry_message.get()
    else:
        #La variable message prend comme valeur le contenu du fichier texte selectionné
        message = read_filename()

    #Initialisation de la variable message_code, en indiquant que c'est un string
    message_code = str()

    #Si la zone d'entrée de la clé est vide
    if entry_cle.get()=='':
        label_crypted['text'] = "Il faut saisir une clé de chiffrement"
        label_crypted['fg'] = "red"
        return

    #Si la zone d'entrée de la clé contient autre chause qu'un nombre
    if not entry_cle.get().isnumeric():
        label_crypted['text'] = "La clé doit être un nombre"
        label_crypted['fg'] = "red"
        return

    #La variable clé prend comme valeur ce qui a été entré dans la textbox "entry_cle"
    cle = int(entry_cle.get())

    #Pour chaque caractère dans le message
    for lettre in message:
        #Si le caractère ne fait pas partie des deux listes de lettres
        if lettre not in listMin and lettre not in listCap:
            message_code += lettre
        else:
            for alphabetMinLettre in listMin:
                #Si la lettre est une lettre minuscule
                if(lettre == alphabetMinLettre):
                    for i in range (len(listMin)):
                        if listMin[i]==lettre:
                            #Ajout de la lettre minuscule crypté dans la variable message_code
                            message_code += str(listMin[(i+cle) % 26])
            
            for alphabetCapLettre in listCap:
                #Si la lettre est une majuscule
                if(lettre == alphabetCapLettre):
                    for i in range (len(listCap)):
                        if listCap[i]==lettre:
                             #Ajout de la lettre majuscule crypté dans la variable message_code
                            message_code += str(listCap[(i + cle) % 26])

    #Affichage du message crypté
    label_crypted['text'] = message_code
    label_crypted['fg'] = "green"

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