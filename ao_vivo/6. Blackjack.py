# importar bibliotecas necessárias
import random as rd

def valor_carta(carta):
    if carta in ["J", "Q", "K"]:
        return 10
    elif carta == "A":
        return 11
    else:
        return int(carta)

def valor_mao(mao):
    soma = 0
    for carta in mao:
        soma += valor_carta(carta)
    return soma

# definir as cartas - uma lista
# definir os valores das cartas - funções

naipe_1 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

player_estourou = False
player_ingame = True

mao_jogador = [rd.choice(naipe_1), rd.choice(naipe_1)]
mao_dealer = [rd.choice(naipe_1), rd.choice(naipe_1)]

print(f"PlayerHand {mao_jogador}")
print(f"DealerHand {mao_dealer}")
print(f"Carta a Mostra: {mao_dealer[0]}")
print(valor_carta(mao_dealer[0]) + valor_carta(mao_dealer[1]))
print(valor_mao(mao_dealer))


hit_choice = 0
while player_ingame:
    hit_choice = input("hit or stand? \n")
    if hit_choice.lower() == "hit":
        mao_jogador.append(rd.choice(naipe_1))
    else:
        player_ingame = False
    soma_jogador = valor_mao(mao_jogador)
    print(soma_jogador)
    if soma_jogador > 21:
        player_ingame = False
        player_estourou = True

    print(f"PlayerHand {mao_jogador}")

# Selecionar um par de cartas aleatório
# Selecionar as cartas do dealer e mostrar apenas uma carta - colocar random para mostrar uma do dealear

# Mostrar a soma do jogador

# Colocar a opção do jogador dar hit ou não
# Stand finaliza
