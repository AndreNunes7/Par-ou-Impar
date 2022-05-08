# par ou impar V.2
import random
red = "\033[0;31m"
uncolor = "\033[0m"
green = "\033[1;32m"
purple = "\033[1;35m"
blue = "\033[1;34m"
blue2 = "\033[1;36m"
yellow = "\033[1;33m"
cont = 0
print(f"{blue2}-={uncolor}" * 20)
print(f"{green}Vamos jogar?{uncolor}")
print(f"{blue2}-={uncolor}" * 20)
while True:
    jogador = int(input(f"{green}Digite um numero: {uncolor}"))
    print(f"{blue2}-={uncolor}" * 20)
    computador = random.randint(1, 10)
    total = jogador + computador
    opcao = ' '
    while opcao not in "PI":
        opcao = str(input(f"{green}Qual você escolhe Par ou Impar? [P/I]: {uncolor}")).strip().upper()[0]
        print(f"{blue2}-={uncolor}"*20)
    print(f"{yellow}Você jogou {jogador} e o computador {computador}. O total deu {total}", end=' ')
    print(f"DEU PAR" if total % 2 == 0 else f"DEU IMPAR!{uncolor}")
    if opcao == "P":
        if total % 2 == 0:
            print(f"{blue2}-={uncolor}" * 20)
            print(f"{blue2}Você VENCEU!!{uncolor}")
            cont += 1
        elif total % 2 == 1:
            print(f"{blue2}-={uncolor}" * 20)
            print(f"{red}Você PERDEU!!{uncolor}")
            break
    else:
        if opcao == "I":
            if total % 2 == 1:
                print("-=" * 20)
                print(f"{blue2}Você VENCEU!!{uncolor}")
                cont += 1
            if total % 2 == 0:
                print(f"{red}Você PERDEU!!{uncolor}")
                break
print("-="*20)
print(f"{red}GAME OVER!!, Você perdeu jogo finalizado!!{uncolor}")
print("Você conseguiu vencer {} vezes!!".format(cont))
