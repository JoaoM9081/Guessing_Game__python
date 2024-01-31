# Importando as bibliotecas necessárias
from random import choice
from interface import*
from validação_resposta import*
import json

# Tentando abrir e carregar o arquivo JSON
try:
    with open("Código/words.json", encoding="utf8") as f:
        words = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    print("Erro ao abrir o arquivo JSON.")
    exit()

# Escolhendo uma palavra aleatória do arquivo JSON
choice_c = choice(list(words.keys()))
n_choice = 3
win = False

cabeçalho('Olá seja bem vindo !')

# Loop principal do jogo
while n_choice > 0:
    print(f'\033[1;36mDica: {words[choice_c]}\033[m')
    print('\033[1;36mData: DDMMAAAA\033[m\n')
    answer_user = input("\033[1mDigite a data: \033[m")
    print(linha())

    # Verificando a resposta do usuário
    win, valid_input = verificar_resposta(answer_user, choice_c)
    if win:
        break

    if valid_input:
        n_choice -= 1

# Imprimindo o resultado final do jogo
if win:
    print('\033[1;32mVITÓRIA !!!\033[m')
else:
    print('\033[1;31mDERROTA !!!\033[m')
    print(f'\033[1mA resposta era: "{choice_c}"\033[m')