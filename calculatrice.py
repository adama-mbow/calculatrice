#Noir: #101419
#Bleu: #476C9B
#Rouge: #984447

from tkinter import *

expression = "" #créer la variable experssion
#créer une finction touche  qui renvoit le resultats de calcul lors qu'on appuie sur la touche =
def appuyer(touche):
    if touche == "=":
        calculer()
        return
    global expression
    expression += str(touche)
    equation.set(expression)

# créer une fonction calculer qui evalue le variable expression avec la fonction eval
def calculer():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total) # la valeur stocker dans equation sera mis sur la variable total
        expression = total # la reable expression prendra la valeur de la variable total
    except:
        equation.set("erreur")
        expression = ""

def effacer():
    global expression
    expression = ""
    equation.set(" ")

gui = Tk()
    #faire une couleur de fond pour l'interface
gui.configure(background="#101419")
    # titre de l'interface
gui.title("calculatrice")
    # taille de l'interface
gui.geometry("")
gui.resizable(0,0) #fixer la taille de la fenetre
gui.minsize(width=250, height=250)
#gui.attributes('-fullscreen', True)
#gui.bind('<Escape>',lambda e: gui.destroy())

 

    #variable pour stocker les contenues
equation = StringVar()

    #boite de résultats
resultat = Label(gui, bg="#101419",fg="#FFF", textvariable=equation, height="2" )
resultat.grid(columnspan=5)
    # creation des boutons
boutons = ["log","ln","√","/","sin",7,8,9,"*","cos",4,5,6,"-","tan",1,2,3,"+","π","+/-",0,".","e","="]
ligne = 1
colonne = 0
for bouton in boutons:
    b = Label(gui, text=str(bouton), bg= "#476c98", fg = "#FFF", height= 5, width= 8 )
    #rendre le texte clicable
    b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))
    b.grid(row = ligne, column= colonne)
    # maintenir les 5 element pour chaque ligne
    colonne +=1
    if colonne == 5:
        colonne = 0
        ligne +=1
b = Label(gui, text="effacer", bg= "#984444", fg = "#FFF", height= 5, width= 26)
b.bind("<Button-1>", lambda e: effacer())
b.grid(columnspan=5)
gui.mainloop()
    