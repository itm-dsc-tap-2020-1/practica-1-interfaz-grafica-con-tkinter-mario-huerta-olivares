import tkinter as tk
from tkinter import ttk
from tkinter import Menu

vida = []
ventana = tk.Tk()
opcionRadio = tk.IntVar()
Pasatiempos = dict.fromkeys(["Futbol", "Leer", "correr", "Nadar", "Saltar"], None)
Estado = ["Con 2 ","Soltero","viudo", "casado"]
Str = ["Nombre","Apellido Materno:", "Apellido Paterno", "Direccion", "Colonia", "Ciudad", "Municipio"]
str= []
EntryArr = []
ComboArr = []
pestana1 = None
pestana2 = None

def click2():   
    hola = "Estado Civil \n" +  Estado[opcionRadio.get()] + "\n"
    hola = hola + "Pasatiempos\n" 
    for key in Pasatiempos:
        if Pasatiempos[key].get() == 1:
            hola = hola + key +"\n" 
    hola +="Objetivo de Vida: \t" + vida[0].get() + "\n"  
    tk.Label(tab2, text = hola).grid(column = 2, row = 12)

def click1():
    fin = []
    for x in EntryArr:
        if x.get():
            fin.append(x.get())
        else:
            tk.Label(tab1, text = "Complete los datos").grid(row = 3, column = 3)
            return
    jojo = ""
    index = 0 
    for i in fin:
        jojo += Str[index] +" :\t" + i +"\n" 
        index += 1
    for i in str:
        jojo += Str[index] +" :\t" + i.get() +"\n" 
        index +=1
    tk.Label(tab1, text = jojo).grid(row = 12, column = 4)

def salir():
    ventana.quit()
    ventana.destroy()
    exit()

def clickimprimri():
    fin = []
    for x in EntryArr:
        if x.get():
            fin.append(x.get())
        else:
            tk.Label(tab1, text = "Complete los datos").grid(row = 3, column = 3)
            return
    jojo = ""
    index = 0 
    for i in fin:
        jojo += Str[index] +" :\t" + i +"\n" 
        index += 1
    for i in str:
        jojo += Str[index] +" :\t" + i.get() +"\n" 
        index +=1
    jojo += "Estado Civil \n" +  Estado[opcionRadio.get()] + "\n"
    jojo += "Pasatiempos\n" 
    for key in Pasatiempos:
        if Pasatiempos[key].get() == 1:
            jojo = jojo + key +"\n"  
    jojo +="Objetivo de Vida: \t" + vida[0].get() + "\n"  
    tk.Label(tk.Tk(), text = jojo).grid(column = 1, row = 12)
        
def acerca():
    help = tk.Tk() 
    help.title("Acerca de")  
    tk.Label(help, text = "Autor:\tMario Huerta Olivares").grid(column = 2, row = 2 ) 

def barramenu():
    barra_menu = Menu(ventana) 
    ventana.config(menu = barra_menu)
    opcio_1 = Menu(barra_menu)
    opcio_1.add_command(label = "Imiprimir", command = clickimprimri)
    opcio_1.add_separator()    
    opcio_1.add_command(label = "Salir", command = salir)
    opcio_2 = Menu(barra_menu)
    opcio_2.add_command(label = "Acerca de", command = acerca)
    barra_menu.add_cascade(label = "Sistema", menu = opcio_1)
    barra_menu.add_cascade(label = "Ayuda", menu = opcio_2)

def pestan2():
    ttk.Label(tab2, text = "PASATIEMPOS").grid(column = 1, row = 0)
    icol = 0
    for key in Pasatiempos:
        Pasatiempos[key] = tk.IntVar()
        tk.Checkbutton(tab2, text = key, variable = Pasatiempos[key]).grid(column = icol, row = 1, padx = 10)
        icol += 1
    ttk.Label(tab2, text = "ESTADO CIVIL").grid(column = 1, row = 4, pady = 10)
    icol = 0
    for x in Estado:
        ttk.Radiobutton(tab2, text = x, variable = opcionRadio, value = icol).grid(padx= 10, pady = 5, row = 6, column = icol)
        icol = icol + 1  
    ttk.Label(tab2, text = "OBJETIVO EN LA VIDA").grid(column = 1, row = 7, pady = 10)
    vida.append(tk.StringVar())
    caja = ttk.Entry(tab2, width = 30, textvariable = vida[0])
    caja.grid(column = 1, row = 8)
    tk.Button(tab2, text = "Imprimir Datos Personales", command = click2).grid(column = 3, row = 8)
    

def pestan1():
    Str = ["Nombre","Apellido Materno:", "Apellido Paterno", "Direccion", "Colonia", "Ciudad", "Municipio"]
    #Hacer 4 Entrys primera pestana
    for i in range (4):
        EntryArr.append(tk.StringVar())
        ttk.Label(tab1, text = Str[i]).grid(column =0, row = i, padx = 40)
        ttk.Entry(tab1, width = 12, textvariable = EntryArr[i]).grid(column = 2,row = i)  
    #Hacer 3 Labels
    for i in range (3):
        ttk.Label(tab1, text = Str[4+i]).grid(column =0, row =4+i, padx = 70)
        str.append(tk.StringVar())
        ComboArr.append(ttk.Combobox(tab1, width = 12, textvariable = str[i], state = 'readonly'))
        ComboArr[i].grid(row = 4+i, column = 2)
    ComboArr[0]['values'] = ["Amor", "me quiero", "suicidar"]  
    ComboArr[1]['values'] = ["Morelia","CDMX", "Monterrey"]
    ComboArr[2]['values'] = ["Villas","Chilolandia","v. de Pedregal"]
    ComboArr[0].current(0)
    ComboArr[1].current(0)
    ComboArr[2].current(0)
    tk.Button(tab1, text = "Imprimir Datos Personales", command = click1).grid(column = 3, row = 8)

tabcontrol = ttk.Notebook(ventana)
tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text = "Datos Personales")
tabcontrol.pack(expand = 1, fill = "both")
pestan1()
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab2, text = "Extras")
pestan2()

def menuayuda():
    #Menu Ayuda
    menu_ayuda = Menu(ventana, tearoff = 0)
    menu_ayuda.add_command(label =  "Acerca de ")
    menu_ayuda.add_cascade(label = "Ayuda", menu =  menu_ayuda)

def main():
    barramenu()
    menuayuda()
    ventana.mainloop()

main()