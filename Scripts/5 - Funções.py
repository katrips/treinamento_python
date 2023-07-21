# Funções

# print("A")
# algo = input("Digite algo: \n")
# algo = algo.upper()

# Funções próprias

def minha_funcao():  # Criar a função
    print("Função")


# minha_funcao() # Executar a função
# minha_funcao() # Executar a função
# minha_funcao() # Executar a função
# minha_funcao() # Executar a função
# minha_funcao() # Executar a função
# minha_funcao() # Executar a função


# Função com parâmetro
def saudação(nome):
    nome = nome.upper()  # As variáveis dentro da função são locais exceto quando mencionado contrário
    print(f"Olá {nome}")


# saudação()  # Quando requisitado um parâmetro é necessário que ele esteja no argumento da função na chamada
# saudação("Henrique")  # Chamando por ordem de parâmetros
# saudação(nome="Katrip")  # Chamando por nome de parâmetros


# print(nome) # por nome ser local a função, nome não é definido globalmente

# Função com retorno

def dobrar_meta(meta):
    meta = meta * 2
    return meta


# print(saudação("Henrique"))  # Funções sem retorno definido, retornam None
# print(dobrar_meta(5))  # Função com retorno definido

# Importar bibliotecas

import random as rd  # Importe bibliotecas no topo do código, é uma boa prática, está aqui somente por ilustração

numero_aleatorio = rd.randint(0, 100)

print(numero_aleatorio)

lista_1 = ["Pizza", "Esfiha", "Batata"]

# Importar funções

from random import choice

print(choice(lista_1))

# Importar biblioteca inteira sem chama-lá

from random import *  # Não mto recomendado, pode dar conflito com outras bibliotecas

print(randint(0, 20))

# Desafio - Fazer uma calculadora
# Na calculadora vc pode escolher um número ou um aleatório entre 0 e 100
