# gui/tela_principal.py
import tkinter as tk
from src.loja import Loja

def SaborRapidoApp():
    loja = Loja()

    janela = tk.Tk()
    janela.title("Sistema de Loja")

    label = tk.Label(janela, text="Sistema de Loja")
    label.pack(pady=10)

    janela.mainloop()