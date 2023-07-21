# Booleanos

numero = 4

if numero > 4: # Condicional
    # print("Maior que 4")
    pass

if numero > 4:
    # print("Maior que 4")
    pass
else:
    # print("Menor ou igual a 4")
    pass

if numero > 4:
    print("Maior que 4")
elif numero == 4:
    print("4")
else:
    print("Menor que 4")


# List Comprehension

frutas = ["Maçã", "Abacaxi", "Manga", "Laranja", "Melancia"]
frutas_minusculo = []

for fruta in frutas: # Modo via loop externo
    frutas_minusculo.append(fruta.lower())

frutas_minusculo = [fruta.lower() for fruta in frutas] # Via list comprehension

frutas_minusculo = []
for fruta in frutas:
    if fruta != "Maçã":
        frutas_minusculo.append(fruta.lower())

frutas_minusculo = [fruta.lower() for fruta in frutas if fruta != "Maçã"]


# Dict Comprehension

primeira_letra = {}

for fruta in frutas: # Via loop externo
    primeira_letra[fruta] = fruta[0]

primeira_letra = {fruta:fruta[0] for fruta in frutas}

# Receber de inputs nome e altura, se a altura for maior ou igual a um limite, liberar a passagem para uma montanha
# russa, caso não, mandar embora

# Fizz Buzz



