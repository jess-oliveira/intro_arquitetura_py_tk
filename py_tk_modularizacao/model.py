# model.py responsável pelos dados e regras do sistema.
# Aqui ficam armazenados os atendentes e as funções que manipulam esses dados.


# Variável global que armazenará todos os atendentes.
atendentes = []


# Função responsável por adicionar um novo atendente.
def adicionar_atendente(nome):

    # Verifica se o parâmetro nome veio vazio.
    if not nome:
        return "vazio"

    # Verifica se o nome já existe na lista de atendentes.
    elif nome in [a["nome"] for a in atendentes]:
        return "duplicado"

    # Caso esteja tudo correto:
    else:

        # Adiciona um novo dicionário na lista atendentes.
        atendentes.append({
            "nome": nome,
            "vendas": 0
        })

        # Retorna ok informando que a operação deu certo.
        return "ok"


# Função responsável por limpar todos os atendentes.
def resetar_atendentes():

    # Aplica o método clear() removendo todos os itens da lista.
    atendentes.clear()


# Função responsável por incrementar +1 venda.
def incrementar_vendas(indice):

    # Acessa o atendente pelo índice recebido
    # e soma +1 no campo vendas.
    atendentes[indice]["vendas"] += 1


# Função responsável por retornar a lista de atendentes.
def obter_atendentes():

    # Retorna a lista completa.
    return atendentes