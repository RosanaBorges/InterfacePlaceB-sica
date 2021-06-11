from tkinter import*
import tkinter as tk 



janela = tk.Tk()
lb = Label (janela, text='Cadastro de Funcionário')
lb.place(x=75, y=0)



lb1= Label (janela, text='Nome completo')
lb1.place(x=5, y=50)

lb2= Label (janela, text='E-mail')
lb2.place (x=5, y=100)

lb3= Label (janela, text='Digite senha')
lb3.place (x=5, y=150)

lb4= Label (janela, text='Confirmar senha')
lb4.place (x=5, y=200)

def bt_onclick1():
    print(entrada1.get(), entrada2.get(), entrada3.get(), entrada4.get())
    

    
bt= Button( janela, width=20, text="Cadastrar", command=bt_onclick1,)
bt.place(x=75, y=250)

   
entrada1= Entry(janela)
entrada1.place(x=100, y=50)

entrada2= Entry(janela)
entrada2.place(x=100, y=100)

entrada3= Entry(janela)
entrada3.place(x=100, y=150)

entrada4= Entry(janela)
entrada4.place(x=100, y=200)

janela.geometry ('300x300+200+200')
janela.mainloop()
