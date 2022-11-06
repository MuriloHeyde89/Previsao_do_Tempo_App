#Instalar Bibliotecas
from tkinter import *
from time import sleep
import requests
from doctest import master
from tkinter import ttk


#Aplicação previsão do tempo API
def bot_click():
    cidade = entrada.get()
    api_key = '80a4ad981dc134d36cc8ddea8b67a00a'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br'
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    tempo = requisicao_dic['weather'][0]['description']
    temperatura = int(requisicao_dic['main']['temp'] - 273.15)
    umidade = requisicao_dic['main']['humidity']
    resultado['text'] = f'Condições climáticas: {tempo} \n Temperatura: {temperatura}ºC \n  Umidade: {umidade}%'

#Visual da Aplicação
master = Tk()
master.geometry('490x580+650+200')
master.title('Previsão do tempo')
fundo = PhotoImage(file='tela.png')
fundo_tela = Label(master, image=fundo)
fundo_tela.pack()
texto_inicial = Label(master, text='Previsão do tempo', font=('Verdana', 17, 'bold'), justify=CENTER, bg='#87CEFA')
texto_inicial.place(width=300, height=50, x=100, y=50)
texto_dois = Label(master, text='Digite abaixo o nome da cidade', font=('Verdana', 10, 'bold'), justify=CENTER, bg='#D9D9D9')
texto_dois.place(width=280, height=50, x=110, y=140)
entrada = Entry(master, font=('Verdana', 12, 'bold'), bg='#D9D9D9', justify=CENTER)
entrada.place(width=280, height=50, x=110, y=200)
botao = Button(master, text='Pesquisar', font=('Verdana', 12, 'bold'), bg='#D16D2E', command=bot_click)
botao.place(width=100, height=50, x=200, y=260)
resultado = Label(master, justify=CENTER)
resultado.place(width=300, height=200, x=100, y=330)



master.mainloop()