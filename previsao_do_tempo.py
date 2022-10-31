import tkinter
from tkinter import *
from tkinter import ttk

#Importar bibliotecas
from PIL import ImageTk, Image
import requests
import datetime
import time

from datetime import datetime
import pytz
import pycountry_convert as pc

#Dados
import json

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

#Frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_principal = Frame(janela, width=320, height=50,bg=c01, pady=0, padx=0, relief="flat",)
frame_principal.grid(row=1, column=0)

frame_quadros = Frame(janela, width=320, height=300,bg=fundo, pady=12, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)

janela.mainloop()