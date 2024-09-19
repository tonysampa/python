# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:09:18 2024

@author: tonysampaio
"""

import tkinter as tk

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
janela.geometry("300x200")  # Define a largura e a altura da janela

# Campo de entrada para o primeiro número
label1 = tk.Label(janela, text="Número 1:")
label1.place(x=20, y=20)  # Define a posição left (x) e top (y)

entry1 = tk.Entry(janela)
entry1.place(x=100, y=20)  # Define a posição do campo de entrada

# Campo de entrada para o segundo número
label2 = tk.Label(janela, text="Número 2:")
label2.place(x=20, y=60)  # Define a posição left (x) e top (y)

entry2 = tk.Entry(janela)
entry2.place(x=100, y=60)  # Define a posição do campo de entrada

# Vincula o evento FocusOut ao campo entry2
entry2.bind("<FocusOut>", lambda event: somar())

# Botão para somar (opcional, caso queira manter o botão também)
botao_somar = tk.Button(janela, text="Somar", command=somar)
botao_somar.place(x=100, y=100)  # Define a posição do botão

# Rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.place(x=100, y=140)  # Define a posição do resultado

# Inicia o loop principal da interface gráfica
janela.mainloop()