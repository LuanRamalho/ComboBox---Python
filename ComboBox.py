import tkinter as tk
from tkinter import ttk

def mostrar_opcao(event):
    opcao_selecionada = combo.get()
    label_resultado.config(text=f'Você selecionou: {opcao_selecionada}')

# Criando a janela principal
root = tk.Tk()
root.title("Combobox Exemplo")
root.geometry("300x200")
root.configure(bg="#ffcc00")  # Cor de fundo

# Estilo da fonte
estilo = ttk.Style()
estilo.configure("TCombobox", font=("Helvetica", 12), padding=5)
estilo.configure("TLabel", font=("Helvetica", 14), background="#ffcc00", foreground="#000")

# Criando a Combobox
opcoes = ["Opção 1", "Opção 2", "Opção 3", "Opção 4", "Opção 5", "Opção 6"]
combo = ttk.Combobox(root, values=opcoes, font=("Helvetica", 12))
combo.bind("<<ComboboxSelected>>", mostrar_opcao)
combo.pack(pady=20)

# Label para mostrar o resultado
label_resultado = ttk.Label(root, text="", font=("Helvetica", 14))
label_resultado.pack(pady=20)

# Executando a janela
root.mainloop()
