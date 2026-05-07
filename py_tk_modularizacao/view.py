# view.py responsável pela parte visual do sistema.
# Aqui ficam janelas, botões, caixas de texto e containers visuais.


# Importar biblioteca tkinter, usada para criar interfaces gráficas.
import tkinter as tk


# Cria a janela principal da aplicação.
janela = tk.Tk()

# Define o título da janela.
janela.title("Controle de Vendas - MVC")

# Define tamanho e posição inicial da janela.
janela.geometry("500x200+700+350")


# Cria caixa de entrada de texto dentro da janela.
entrada_nome = tk.Entry(janela)

# Exibe a caixa de texto na tela.
# pady adiciona espaçamento vertical.
entrada_nome.pack(pady=5)


# Cria botão adicionar atendente.
botao_adicionar = tk.Button(
    janela,
    text="Adicionar Atendente"
)

# Exibe o botão na tela.
botao_adicionar.pack()


# Cria botão resetar.
botao_resetar = tk.Button(
    janela,
    text="Resetar"
)

# Exibe o botão na tela.
botao_resetar.pack()


# Cria um Frame/container para armazenar os atendentes exibidos.
quadro_atendentes = tk.Frame(janela)

# Exibe o container na interface.
quadro_atendentes.pack(pady=10)