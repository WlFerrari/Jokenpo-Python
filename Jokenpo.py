from random import randint
from time import sleep

lista = ("Pedra", "Papel", "Tesoura")
emojis = ["🪨", "📄", "✂️"]

computador = randint(0, 2)

perguntar = int(input(f'''Escolha uma opcao para se jogar: 

[0] Pedra {emojis[0]}
[1] Papel {emojis[1]}
[2] Tesoura {emojis[2]}
 
Digite sua escolha: '''))

print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POOH!!!\n")

print("-="*20)
print(f"O computador escolheu: {lista[computador]} {emojis[computador]}")
print(f"O jogador escolheu: {lista[perguntar]} {emojis[perguntar]}")
print("-="*20)

# Ajuste das regras do jogo
if computador == perguntar:
    print("Empate!")
elif (computador == 0 and perguntar == 2) or (computador == 1 and perguntar == 0) or (computador == 2 and perguntar == 1):
    print("Computador venceu!")
else:
    print("Jogador venceu!")
