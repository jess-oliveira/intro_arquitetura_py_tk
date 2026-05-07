# app.py responsável por conectar a interface (view)
# com as regras de negócio (model).
# Aqui ficam os eventos, ações dos botões e atualização da interface.


# Importa messagebox para exibir mensagens na tela.
from tkinter import messagebox

# Importa tkinter.
import tkinter as tk

# Importa o model responsável pelos dados.
import model

# Importa os elementos visuais da view.
import view


# Função chamada ao clicar no botão adicionar.
def adicionar_atendente():

    # Captura o texto digitado no campo entrada_nome.
    # .get() pega o valor digitado.
    # .strip() remove espaços vazios no começo e fim.
    nome = view.entrada_nome.get().strip()


    # Envia o nome para o model validar e adicionar.
    resultado = model.adicionar_atendente(nome)


    # Verifica o retorno recebido do model.

    # Caso o nome esteja vazio:
    if resultado == "vazio":

        messagebox.showwarning(
            "Nome vazio",
            "Digite um nome!"
        )


    # Caso o nome já exista:
    elif resultado == "duplicado":

        messagebox.showinfo(
            "Duplicado",
            "Atendente já existe."
        )


    # Caso tudo tenha dado certo:
    elif resultado == "ok":

        # Limpa o campo de texto.
        view.entrada_nome.delete(0, tk.END)

        # Atualiza os elementos exibidos na interface.
        atualizar_interface()


# Função responsável por resetar todos os atendentes.
def resetar_atendentes():

    # Exibe mensagem de confirmação antes de apagar os dados.
    if messagebox.askyesno(
        "Resetar",
        "Tem certeza que deseja resetar todos os dados?"
    ):

        # Chama o model para limpar os dados.
        model.resetar_atendentes()

        # Atualiza interface.
        atualizar_interface()


# Função responsável por incrementar vendas.
def incrementar_vendas(indice):

    # Chama o model para incrementar a venda.
    model.incrementar_vendas(indice)

    # Atualiza interface.
    atualizar_interface()


# Função responsável por redesenhar os elementos da interface.
def atualizar_interface():

    # Percorre todos os widgets dentro de quadro_atendentes.
    for widget in view.quadro_atendentes.winfo_children():

        # Remove widgets antigos da interface.
        widget.destroy()


    # Percorre a lista de atendentes.
    # enumerate retorna:
    # i -> índice
    # atendente -> item atual da lista
    for i, atendente in enumerate(model.obter_atendentes()):

        # Monta texto exibindo nome e vendas.
        texto = f"{atendente['nome']}: {atendente['vendas']} vendas"


        # Cria rótulo de texto dentro do quadro.
        rotulo = tk.Label(
            view.quadro_atendentes,
            text=texto
        )


        # Posiciona o rótulo na linha correspondente.
        rotulo.grid(
            row=i,
            column=0,
            sticky="w"
        )


        # Cria botão responsável por incrementar vendas.
        botao_incrementar = tk.Button(
            view.quadro_atendentes,
            text="+1",

            # lambda cria uma função temporária.
            # indice=i salva o índice correto daquele botão.
            command=lambda indice=i: incrementar_vendas(indice)
        )


        # Posiciona botão ao lado do rótulo.
        botao_incrementar.grid(
            row=i,
            column=1
        )


# Conecta os botões da view às funções do app.
view.botao_adicionar.config(command=adicionar_atendente)

view.botao_resetar.config(command=resetar_atendentes)


# Atualiza interface inicial.
atualizar_interface()


# Mantém a janela aberta.
view.janela.mainloop()