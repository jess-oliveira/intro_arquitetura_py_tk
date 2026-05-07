# Importar biblioteca tinkter, serve para criar janelas, botões, telas.
import tkinter as tk
#importar messagebox , que permite criar caixar de mensagem. Do tkinter importa modulo mb
from tkinter import messagebox


# Variável global: 
atendentes = []

#Criar função para adcionar atendente.
def adicionar_atendente():
     # Cria variavel nome que vai pegar (.get) o que for inserido em entrada_nome e ira reirar os espaços (.strip)
    nome = entrada_nome.get().strip()
    
    # Condição para para adicionar nome:
    if not nome:
    # Se não tiver nada digitado ira retornar mensagem de aviso:
        messagebox.showwarning("Nome vazio", "Digite um nome!")
        return

    # O colchete externo cria uma nova lista contendo os valores da chave "nome" de cada objeto a (onde a é cada item percorrido em atendentes), e o if verifica se nome está dentro dessa lista.
    if nome in [a["nome"] for a in atendentes]:
        # Se encontrar nome em atendentes irá retornar a mensgagem:
        messagebox.showinfo("Duplicado", "Atendente já existe.")
        return

    atendentes.append({"nome": nome, "vendas": 0})
    entrada_nome.delete(0, tk.END)
    atualizar_interface()


#função para limpar a lista de atendentes:
def resetar_atendentes():
    #para não o usuario nao deletar por engano, primeiro ira confirmar com mensagem:
    if messagebox.askyesno("Resetar", "Tem certeza que deseja resetar todos os dados?"):
        #Se sim ira executar o clear do python
        atendentes.clear()
        atualizar_interface()


# Cria função incrementar_vendas que recebe um índice (posição do atendente na lista)
def incrementar_vendas(indice):
    # Acessa o atendente correspondente em atendentes[indice], pega o valor da chave "vendas" e incrementa +1 nesse valor
    atendentes[indice]["vendas"] += 1
    atualizar_interface()


# Redesenha a interface sempre que os dados mudarem:
def atualizar_interface():

    # Percorre todos os widgets dentro de quadro_atendentes:
    for widget in quadro_atendentes.winfo_children():
     # Remove o widget da interface:
        widget.destroy()

    # Percorre a lista de atendentes com índice e dados:
    for i, atendente in enumerate(atendentes):

        # Monta o texto com nome e número de vendas:
        texto = f"{atendente['nome']}: {atendente['vendas']} vendas"

        # Cria um rótulo de texto dentro do quadro:
        rotulo = tk.Label(quadro_atendentes, text=texto)

        # Posiciona o rótulo na linha correspondente:
        rotulo.grid(row=i, column=0, sticky="w")

        # Cria o botão para incrementar as vendas:
        botao_incrementar = tk.Button(
            quadro_atendentes,
            text="+1",
            command=lambda indice=i: incrementar_vendas(indice)
        )

        # Posiciona o botão ao lado do rótulo:
        botao_incrementar.grid(row=i, column=1)



# cria uma variavel "janela" que vai receber tk.TK() jeito de criar a janela principal com tinkter.
janela = tk.Tk()

# Adiciona um titulo a janela criada:
janela.title("Controle de Vendas - SmartView")

# Cria uma variavel onde sera criada uma caixa para digitação de texto curto e essa caixa estara dentro da janela criada.
entrada_nome = tk.Entry(janela)

# Mostra essa caixa criada na janela:
# colocar borda no eixo y :
entrada_nome.pack(pady=5)

# Cria botão na janela define o texto que ira aparecer no botao e o comando sera a função executada ao ser clicado)
botao_adicionar = tk.Button(janela, text="Adicionar Atendente", command=adicionar_atendente)
botao_adicionar.pack()

botao_resetar = tk.Button(janela, text="Resetar", command=resetar_atendentes)
botao_resetar.pack()

# Com tk.frame sera pego um pedaço de janela onde sera criado um container para guardar coisas
quadro_atendentes = tk.Frame(janela)
quadro_atendentes.pack(pady=10)

atualizar_interface()

# Manter a janela aberta: 
janela.mainloop()
