# While Loop

i = 0

while i < 10:
    # print(i)
    i = i + 1

# # Loop infinito
# while True:
#     print(5)

# For loop

for i in range(10):
    # print(i)
    pass

comidas = ["Pizza", "Esfiha", "Hamburguer"]

for comida in comidas:
    # print(comida)
    pass

paises_origem = {
    "Pizza": "Itália",
    "Esfiha": "Síria",
    "Hamburguer": "Líbano"
}

for comida in comidas:
    # print(f"{comida} - {paises_origem[comida]}")
    pass


# Loop duplo, triplo, quádruplo, etc.
mesas = [1, 5, 7]

for mesa in mesas:
    for comida in comidas:
        # print(f"{mesa}: {comida}")
        pass

# Desafio - Refazer desafio 2 com loops
# Desafio - Sequência de Fibonacci