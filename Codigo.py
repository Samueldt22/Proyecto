
#%%

import subprocess as sub
import time
from tkinter import*
from tkinter import messagebox,ttk
from datetime import datetime




    
class Time:
    def tiempo(self):
        self.tiem=time.sleep(5)
        
        return self.tiempo()



class Salud(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("600x700")
        self.config(bg="cyan")
        self.resizable(0,0)
        self.program={
        "Notepad": r"C:\WINDOWS\system32\notepad.exe",
        "Word": r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE",
        "Discord": r"C:\Users\Dionisio\AppData\Local\Discord\app-1.0.9004\Discord.exe",
        "League Of Legends": r"C:\Riot Games\League of Legends\LeagueClient.exe"
        }

        
        self.widgets()
        
    def mostrar(self):
        now=datetime.now()
        hora=now.hour
        min=now.minute
        secon=now.second
        self.tre.insert("",0,text=self.programas.get(),values=(f"{hora}:{secon}:{min}"))
        
    def abrir(self):
        tarea=self.program[self.programas.get()]
        sub.Popen(tarea)
        self.mostrar()
        time.sleep(30)
        self.cerrar(tarea)

    def cerrar(self,tarea):
        tare=tarea.split("\\")
        tare=tare[-1]
        sub.call(f"TASKKILL /IM {tare} /F",shell=True)
        
    
    def recuperar(self):
        self.programa.delete(0,END)
        valor=self.tre.item(self.tre.selection())['values'][0]
        self.programa.insert(0,valor)

        
    def widgets(self):

        self.programas=ttk.Combobox(self,font="16",values=list(self.program.keys()))
        self.programas.place(x=20,y=10,width=150)
        lblprograma=Label(self,text="PROGRAMAS",bg="cyan",font="16")
        lblprograma.place(x=20,y=40,width=120)
        self.btn=Button(self,text="Abrir", font="16",command=self.abrir)
        self.btn.place(x=200,y=10)
      
        self.programa=Entry(self,font="16")
        self.programa.place(x=300,y=10,width=150)
        self.btn1=Button(self,text="SELECCIONAR", font="16",command=self.recuperar)
        self.btn1.place(x=340,y=40)
        self.btn1=Button(self,text="CERRAR", font="16",command=self.cerrar)
        self.btn1.place(x=480,y=10)
      
        self.frame=Frame(self,bg="gold")
        self.frame.place(x=10,y=100,width=580,height=580)
        self.tre=ttk.Treeview(self.frame,height=40, columns=("#0","#1"))
        self.tre.place(x=0,y=0,width=580,height=580)
        for i in range(3):
            self.tre.column(f"#{i}",width=290)
        self.tre.heading("#0",text="APP")
        self.tre.heading("#1",text="INICIO")

 
if __name__ =="__main__":
    app=Salud()
    app.mainloop()
    
# %%
