from turtle import Turtle, Screen, textinput
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)

user_bet = screen.textinput(title="Pronto?", prompt="Ready?")

# Laranja, vinho, verde, vermelho
colors = [
    "#f7941e",  # Laranja
    "#9a1d28",  # Vinho
    "#00413a",  # Verde
    "#da212a",  # Vermelho
]

nomes = {
    "#f7941e": "Katrip",
    "#9a1d28": "Pedro",
    "#00413a": "Marlon",
    "#da212a": "Enzo",
}

turtle_distance = 600 / (len(colors) - 1)

turtle_list = []

for i in range(len(colors)):
    turtle_list.append(Turtle(shape="turtle"))
    turtle_list[i].color(colors[i])
    turtle_list[i].penup()

for i in range(len(colors)):
    if nomes[colors[i]] in ["Katrip", "Enzo"]:
        turtle_list[i].goto(x=-500, y=300 - turtle_distance * i)
    else:
        turtle_list[i].goto(x=-400, y=300 - turtle_distance * i)

# for i in range(3):
#     turtle_list[i].goto(x=-230, y=turtle_distance*2.5 - turtle_distance*i)
#     turtle_list[i+3].goto(x=-230, y=-turtle_distance/2-turtle_distance*i)

if user_bet != 50:
    is_race_on = True

max_length = 420

while is_race_on:
    for ind_turt, turtle in enumerate(turtle_list):
        if turtle.xcor() > max_length:
            is_race_on = False
            winning_color = ind_turt
            max_length = turtle.xcor()

        rand_distance = random.randint(5, 35)
        turtle.forward(rand_distance)

textinput("Temos um vencedor", f"Parabéns {nomes[colors[winning_color]]}!. Você ganhou! 🏆")

screen.exitonclick()
