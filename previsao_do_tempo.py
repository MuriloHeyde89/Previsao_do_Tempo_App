import tkinter
from tkinter import *
from tkinter import tkk

#Cores
co0 = "#444466"     #preta
c01 = "#feffff"     #branca
c02 = "#6f9fbd"     #azul


fundo_dia = "#6cc4cc"
fundo_noite = "484f60"
fundo_tarde = "#bfb86d"
fundo = fundo_dia


janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

tkk.Separator(janela, orient=HORIZONTAL).grid(row=0, coLumnspan=1, ipadx=157)

janela.mainloop()