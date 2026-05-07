# Introdução à Arquitetura com Python e Tkinter

Projeto acadêmico desenvolvido durante estudos de:

- Python
- Tkinter
- interfaces gráficas (GUI)
- modularização
- fundamentos de arquitetura de software

O projeto foi construído acompanhando aulas práticas e evoluindo gradualmente conforme novos conceitos eram apresentados.

---

# 📚 Objetivo do estudo

O objetivo principal foi entender:

- como criar interfaces gráficas com Tkinter
- manipular listas e dicionários
- trabalhar com funções e eventos
- atualizar elementos da interface dinamicamente
- identificar problemas de código monolítico
- iniciar conceitos de separação de responsabilidades e modularização

---

# 🟥 Versão 1 — py_tk_monolitico

Primeira implementação do sistema.

## Características

- todo o código em um único arquivo
- interface, dados e lógica juntos
- foco em fundamentos do Tkinter e lógica básica

## Estrutura

```plaintext
py_tk_monolitico/
└── app.py
```

## Conceitos praticados

- criação de janelas
- botões
- caixas de texto
- labels
- eventos
- listas
- dicionários
- funções
- lambda
- atualização dinâmica da interface

---

# 🟩 Versão 2 — py_tk_modularizacao

Segunda implementação do mesmo sistema, agora com separação de responsabilidades.

## Estrutura

```plaintext
py_tk_modularizacao/
├── model.py
├── view.py
└── app.py
```

## Divisão dos módulos

| Arquivo  |          Responsabilidade           |
|   ---    |                 ---                 |
| model.py | dados e regras                      |
| view.py  | interface visual                    |
| app.py   | integração entre interface e lógica |

## Conceitos praticados

- modularização
- separação de responsabilidades
- organização de código
- reutilização de lógica
- início de conceitos inspirados em MVC

---

# 🧠 Aprendizados durante o projeto

Durante o desenvolvimento foi possível compreender melhor:

- diferença entre interface e lógica
- problemas de aplicações monolíticas
- importância da organização de código
- reutilização de funcionalidades
- impacto da arquitetura na manutenção do software

---

# 💬 Sobre os comentários no código

Os comentários foram utilizados como apoio de estudo e fixação dos conceitos aprendidos durante as aulas.

O objetivo foi documentar o raciocínio e facilitar revisões futuras do conteúdo.

---

# 🛠️ Tecnologias utilizadas

- Python
- Tkinter