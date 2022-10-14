
from tkinter import *
import sys
import os
from turtle import color
sys.path.append(os.path.abspath("/Users/italovargas/Library/CloudStorage/GoogleDrive-vargasserrano.asociados@gmail.com/My Drive/1-Contabilidad/2-SGC/PYTHON"))
from DatosClientes import *

root=Tk()

frame=Frame(root)#,bg="black")

frame.pack(fill="both",expand="True")

root.title("VARGAS SERRANO & ASOCIADOS - V:1.3")
root.geometry('250x850+500+0')
root.config(bg="green")
#root.resizable(False,True)





#frame.config(width="300", height="200")

Ins=Label(frame,text="INSERTA NOMBRE CLIENTE ").pack()


BuscNombre=Entry(frame,text="inserta el nombre a buscar")
#BuscNombre.place(x=100,y=100,height = 20, width = 2)
BuscNombre.pack()#,textvariable=NOMBRE)
#BuscNombre.grid(row=0,column=2)

Ins=Label(frame,text="Nombre. ").pack()
E1=Entry(frame, width = 30)
E1.pack()

Ins=Label(frame,text="C.U.R.P. ").pack()
E2=Entry(frame, width = 30)
E2.pack()

Ins=Label(frame,text="R.F.C. ").pack()
E3=Entry(frame, width = 30)
E3.pack()

Ins=Label(frame,text="S.I.E.C.").pack()
E4=Entry(frame, width = 30)
E4.pack()

Ins=Label(frame,text="MAIL.").pack()
E5=Entry(frame, width = 30)
E5.pack()

Ins=Label(frame,text="WhatsApp.").pack()
E11=Entry(frame, width = 30)
E11.pack()

Ins=Label(frame,text="C.P. ").pack()
E6=Entry(frame, width = 30)
E6.pack()

Ins=Label(frame,text="Reg. Fiscal. ").pack()
E7=Entry(frame, width = 30)
E7.pack()

Ins=Label(frame,text=" Pass. eFirma ").pack()
E8=Entry(frame, width = 30)
E8.pack()

Ins=Label(frame,text="Clave Producto ").pack()
E9=Entry(frame, width = 30)
E9.pack()

Ins=Label(frame,text="Dirección ").pack()
E10= Text(frame, wrap= WORD, font= ('Menlo 14'))

E10.place(x=25, y= 650, width= 200, height= 130)


#E10=(frame, width = 100)


def b1():
    #E1=Entry(root)
    #E1.delete(0,END) 
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)  
    E5.delete(0,END)
    E6.delete(0,END)
    E7.delete(0,END)
    E8.delete(0,END)
    E9.delete(0,END)
    #E10.delete(END,END)
    E11.delete(0,END)

    nombre=BuscNombre.get()
    nombre = nombre.upper()
    Nombre=DIC_NOMBRES.get(nombre)
    RFC=DIC_RFC.get(nombre)
    PASS=DIC_PASS.get(nombre)
    MAIL=DIC_MAIL.get(nombre)
    CURP=DIC_CURP.get(nombre)
    CP=DIC_CP.get(nombre)

    RF=DIC_RF.get(nombre)
    PASSEF=DIC_PASSEF.get(nombre)
    CLAVEPROD=DIC_CLAVEPROD.get(nombre)
    DIRECCION=DIC_DIRECCION.get(nombre)
    CEL=DIC_CEL.get(nombre)


    E1.insert(0,Nombre)
    E1.pack()
      
    E2.insert(0,CURP)
    E2.pack()
  
    E3.insert(0,RFC)
    E3.pack()
    
    
    E4.insert(0,PASS)
    E4.pack()
    
    
    E5.insert(0,MAIL)
    E5.pack()

    E11.insert(0,CEL)
    E11.pack()

    E6.insert(0,CP)
    E6.pack()

    E7.insert(0,RF)
    E7.pack()

    E8.insert(0,PASSEF)
    E8.pack()

    E9.insert(0,CLAVEPROD)
    E9.pack()

    E10.insert(END,DIRECCION)
    E10.pack()


    #E10.insert(0,DIRECCION)
    #E10.pack()


#frame.bind('<Return>', b1)


def b2():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    E6.delete(0,END)
    E7.delete(0,END)
    E8.delete(0,END)
    E9.delete(0,END)
    #E10.delete(0,END)
    return None
      

Boton=Button(frame,text="BUSCAR.",command=b1,height = 2, width = 20,fg='green')#,state='disabled')
Boton.pack()



clear=Button(frame,text="Borrar.",command=b2,fg='white')#,state='disabled')
clear.pack()

#root.bind('<Return>', b1)

#Ins.pack()






root.mainloop()

#frame.mainloop()


 

