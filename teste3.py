import tkinter as tk
from tkinter import messagebox

# Função para mostrar a mensagem de informação
def show_info():
    messagebox.showinfo("Informação", "Esta é uma mensagem informativa")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de MessageBox")

# Botão para acionar a mensagem
info_button = tk.Button(root, text="Mostrar Informação", command=show_info)
info_button.pack(pady=20)

# Executar o loop principal
root.mainloop()