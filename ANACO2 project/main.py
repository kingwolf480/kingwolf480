from tkinter import *
import time


# variable indispensables :
bordure = 1


#def
def horaireactuelle():
    heure=str(time.strftime("%H"))
    minute=str(time.strftime("%M"))
    if int(time.strftime("%S"))%2!=0:
        tik_clock_graph=" "
    else:
        tik_clock_graph=":"

    heureactuelle=str(heure)+str(tik_clock_graph)+str(minute)
    label_clock.config(text=heureactuelle)
    label_clock.after(1000,horaireactuelle)






# creer la fenetre princ "window"
window = Tk()
# importation des differentes image :
icone_reglage = PhotoImage(file='icones/reglages.png')
icone_graphique = PhotoImage(file='icones/graphique.png')
icone_accueil = PhotoImage(file='icones/accueil.png')
# personalisation de la fenetre
window.title("Capteur de CO2")
window.geometry("1080x720")
window.config(background='white')
window.iconbitmap("icones/nuage-de-co2.ico")

# creation de la frame principale (tout sauf menu)
frame_main = Frame(window, bg='white', bd=bordure, relief=SUNKEN)

# creation de la frame de l'horloge
frame_clock = Frame(frame_main, bg='white', bd=bordure, relief=SUNKEN)

label_clock = Label(frame_clock, text="a", font=("Arial", 40), bg='white', fg='black')
label_clock.pack()

# creation frame du capteur
frame_capteur = Frame(frame_main, bg='white', bd=bordure, relief=SUNKEN)

label_capteur = Label(frame_capteur, text="capteur", font=("Arial", 40), bg='white', fg='black')
label_capteur.pack()

# creation frame "autre"
frame_autre = Frame(frame_main, bg='white', bd=bordure, relief=SUNKEN)

label_autre = Label(frame_autre, text="autre", font=("Arial", 40), bg='white', fg='black')
label_autre.pack()

# creation frame menu
frame_menu = Frame(window, bg='white', bd=bordure, relief=SUNKEN)
# bouton accueil
button_accueil = Button(frame_menu, image=icone_accueil, bg='white', bd=bordure, relief=SOLID)
button_accueil.pack()
# bouton graphique
button_graphique = Button(frame_menu, image=icone_graphique, bg='white', bd=bordure, relief=SOLID)
button_graphique.pack()
# bouton reglages
button_reglage = Button(frame_menu, image=icone_reglage, bg='white', bd=bordure, relief=SOLID)
button_reglage.pack()



# ajoue des frames
frame_menu.pack(side=RIGHT, fill=Y)
frame_clock.grid(row=0, column=0, sticky=W)
frame_capteur.grid(row=1, column=1, sticky=W)
frame_autre.grid(row=1, column=2, sticky=W)
frame_main.pack(fill=BOTH)

horaireactuelle()
# afficher la fenetre
window.mainloop()
