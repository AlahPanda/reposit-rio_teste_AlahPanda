import os
from tkinter import *
import subprocess

def fechar_root():
    root.destroy()

def ipconfig():
    COMMAND = 'start cmd /k "color 0c && ipconfig"'
    coiso = subprocess.run(COMMAND, shell=True)
    print(coiso.stdout)
 
def drivers():
    COMMAND = 'start cmd /k "color 0c && DRIVERQUERY -v"'
    coiso = subprocess.run(COMMAND, capture_output=True, text=True, shell=True)
    print(coiso.stdout)

def sistema():
    if os.name == 'posix':
        print("Este é um sistema operacional compatível com POSIX.")
    elif os.name == 'nt':
        print("Este é um sistema operacional Windows.")
    else:
        print(f"Este é um sistema operacional desconhecido: {os.name}") 

def performance():
    command = "perfmon"
    coiso = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(coiso.stdout)
def processos():
    command = "tasklist"
    coiso = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(coiso.stdout)

def utilizador():
    command = "whoami"
    coiso = subprocess.run(command, capture_output=True, text=True, shell=True)
    print("O utilizador deste dispositivo é " + coiso.stdout)

def pastas():
    command = "start cmd /k telnet towel.blinkenlights.nl"
    coiso = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(coiso.stdout)

def bateria():
    command = "powercfg /batteryreport"
    coiso = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(coiso.stdout)
    command = "start "

def systeminfo():
    command = "systeminfo"
    coiso = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(coiso.stdout)

def net():
    command = "net accounts"
    coiso = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(coiso.stdout)

def rpg():
    command = 'start cmd /k "color 0a && telnet ateraan.com 4002"'
    coiso = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(coiso.stdout)

def cleanmgr():
    command = "cleanmgr"
    coiso = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(coiso.stdout)



root = Tk()
root.geometry('250x90')
root.title('Terminal Beta')
root.resizable(False,False)
texto = Label(root, text='Seja bem-vindo a nova versão do terminal \nclique entrar pra usufruir!')
texto.grid(column=0, row=0)
butao = Button(root, text='Entrar', command=fechar_root)
butao.place(relx=0.40,rely=0.35)
root.mainloop()


root = Tk()
root.geometry('600x200')
root.title('Terminal beta 2.1.21')
root.configure(bg="black")
root.resizable(False,False)

butao = Button(root, text='IP do dispositivo', command=ipconfig)
butao2 = Button(root, text="Nome do sistema operacional", command=sistema)
butao3 = Button(root, text="Lista de drivers", command=drivers)
butao4 = Button(root, text="Performance do dispositivo", command=performance)
butao5 = Button(root, text="Processos em execução", command=processos)
butao6 = Button(root, text="Utilizador", command=utilizador)
butao7 = Button(root, text="Star Wars", command=pastas)
butao8 = Button(root, text="Estado da bateria", command=bateria)
butao9 = Button(root, text="Informações do hardware", command=systeminfo)
butao10 = Button(root, text="Configurações da rede", command=net)
butao11 = Button(root, text="RPG", command=rpg)
butao12 = Button(root, text="Limpar aqv temporários", command=cleanmgr)

butao.grid(row=0, column=0, padx=20, pady=10)
butao2.grid(row=0, column=1, padx=20, pady=10)
butao3.grid(row=0, column=2, padx=20, pady=10)
butao4.grid(row=1, column=0, padx=20, pady=10)
butao5.grid(row=1, column=1, padx=20, pady=10)
butao6.grid(row=1, column=2, padx=20, pady=10)
butao7.grid(row=2, column=0, padx=20, pady=10)
butao8.grid(row=2, column=1, padx=20, pady=10)
butao9.grid(row=2, column=2, padx=20, pady=10)
butao10.grid(row=3, column=0, padx=20, pady=10)
butao11.grid(row=3, column=1, padx=20, pady=10)
butao12.grid(row=3, column=2, padx=20, pady=10)

root.mainloop()