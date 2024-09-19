# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import tkinter
from tkinter import messagebox
import tkinter as tk

print('Estou fazendo um teste')
print('Estou fazendo um teste')
print('Estou fazendo um teste')

root = tkinter.Tk()
root.withdraw()  # Oculta a janela principal

# Exibe a caixa de diálogo com a mensagem
messagebox.showinfo("Título do Diálogo", "Esta é uma mensagem na caixa de diálogo!")


# Cria a janela principal (necessária, mas não visível)
root = tkinter.Tk()
root.withdraw()  # Oculta a janela principal

# Exibe uma caixa de diálogo de pergunta
resposta = messagebox.askyesno("Confirmação", "Você deseja continuar?")

if resposta:
    messagebox.showinfo("Título do Diálogo", "Usuário escolheu 'Sim'")
else:
    print("Usuário escolheu 'Não'")
    


# Função que faz a soma dos números
def somar():
    try:
        num1 = float(entry1.get())  # Pega o valor do primeiro campo de entrada
        num2 = float(entry2.get())  # Pega o valor do segundo campo de entrada
        resultado = num1 + num2     # Soma os dois números
        label_resultado.config(text=f"Resultado: {resultado}")  # Exibe o resultado
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")  # Erro caso não sejam números

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de Soma")
janela.geometry("300x200")

# Campo de entrada para o primeiro número
label1 = tk.Label(janela, text="Número 1:")
label1.place(x=50, y=130)

label1.pack()

entry1 = tk.Entry(janela)
entry1.pack()

# Campo de entrada para o segundo número
label2 = tk.Label(janela, text="Número 2:")
label2.pack()

entry2 = tk.Entry(janela)
entry2.pack()

# Botão para somar
botao_somar = tk.Button(janela, text="Somar", command=somar)
botao_somar.pack()

# Rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()    