# Listas

lista_1 = ["Pizza", "Esfiha", "Batata"]
lista_vazia = []

# print(type(lista_1)) # Tipo "list"
# print(lista_1) # Visualizar lista
# print(lista_1[1]) # Selecionar elementos

lista_1.append("Hamburguer") # Adicionar itens
lista_1.pop(lista_1.index("Batata")) # Remover itens / Obter índice

# print(lista_1)


# Tuplas

tupla_1 = ("Pizza", "Esfiha", "Batata")

# print(type(tupla_1)) # Tipo "tuple"
# print(tupla_1) # Visualizar tupla
# print(tupla_1[0]) # Selecionar elementos

tupla_1.index("Esfiha") # Não é possível alterar a tupla
tupla_1.count("Esfiha")


# Set/Conjunto

conjunto_1 = {1, 3, 5, 2, 2}
# print(conjunto_1) # Conjuntos não possuem valores duplicados
conjunto_2 = {2, 3, 5, 6}

uniao_conjuntos = conjunto_1 | conjunto_2
intersec_conjuntos = conjunto_1 & conjunto_2
diff12_conjuntos = conjunto_1 - conjunto_2
diff21_conjuntos = conjunto_2 - conjunto_1

# Dicionários

dicionario_1 = {"Pizza": "Massa", "Esfiha": "Massa", "Batata": "Vegetal"}

dicionario_2 = {
    "Pizza": "Itália",
    "Esfiha": "Síria",
    "Batata": "Terra",
    "Feijoada": "Brasil"
} # Criação identada - Mais fácil de ler

dicionario_vazio = {}

# print(type(dicionario_1)) # Tipo "Dict"
# print(dicionario_1) # Visualizar dicionário
# print(dicionario_1["Pizza"]) # Acessar valores do dicionário

dicionario_1["Hamburguer"] = "Carne" # Adicionar valores no dicionário

# print(dicionario_1["Hamburguer"])

# Funções, .get(), .items()


# Desafio: fazer um script que guarde 4 nomes e "printe" em ordem inversa