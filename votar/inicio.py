#!/usr/bin/python3
from tkinter import *
import time

inicio_ventana = Tk()
photo = PhotoImage(file = "co.png")
inicio_ventana.iconphoto(False, photo)
sub_ventana = Frame(inicio_ventana, width="450", height="200")
avatar = PhotoImage(file="26411.gif")


def helloCallBack():
	if int(input_texto_edad.get()) >= 18 : 
		if int(input_texto_edad.get()) <= 70 :
			votar_si = "SI TIENE PERMITIDO PARA VOTAR\n "+ input_texto_nombre.get()
			votar_si_inprimir= Label(inicio_ventana,text=votar_si, bg="#33AA57")
			votar_si_inprimir.place(x=230, y=400)
		else:
			votar_no_70 = "NO TIENE PERMITIDO VOTAR  \nTIENES MAS DE 70 AÑOS\n"+ input_texto_nombre.get()
			texto22= Label(inicio_ventana,text=votar_no_70, bg="red")
			texto22.place(x=230, y=400)	

	else:
		
		nombre_menor = "NO TIENES PERMISO DE VOTAR\n POR SER MENOR DE EDAD\n" + input_texto_nombre.get()
		votar_no_18 = Label(inicio_ventana,text=nombre_menor, bg="red")
		votar_no_18.place(x=230, y=400)
		


inicio_ventana.title("VERIFICAR VOTO")
inicio_ventana.geometry("600x500")
inicio_ventana.resizable(width=False, height=False)
inicio_ventana.config(bg="#555753")

titulo_h2= Label(inicio_ventana,text="Comprobar si tiene \npermiso de votar", font=("Arial Bold", 22,), bg="#555753", fg="#87CB45")
titulo_h2.place(x=160, y=50)

sub_ventana.place(x=75, y=150)
sub_ventana.config(bg="#BABDB6")
 
texto_nombre = Label(sub_ventana,text="SU NOMBRE:",bg="#BABDB6", fg="#000000")
texto_nombre.place(x=180, y=30)
input_texto_nombre = Entry(sub_ventana, bg="#FFFFFF", fg="#000000")
input_texto_nombre.focus()
input_texto_nombre.place(x=180, y=60)

texto_edad = Label(sub_ventana,text="SU EDAD:", bg="#BABDB6", fg="#000000")
texto_edad.place(x=180, y=90)
input_texto_edad = Entry(sub_ventana,  bg="#FFFFFF", fg="#000000")
input_texto_edad.place(x=180, y=120)

imagenn=Label(sub_ventana, image=avatar)
imagenn.place(x=12, y=25)


exitButton = Button(sub_ventana, text="COMPROBAR", command=helloCallBack, borderwidth=6, bg="#F57900")
exitButton.place(x=220, y=150)




inicio_ventana.mainloop()
