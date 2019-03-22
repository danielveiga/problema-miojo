# -*- encoding: utf-8 -*-

from ampulheta import Ampulheta
from miojo import Miojo
from utils import calcula_mdc
import sys

# Captura tempo de preparo do miojo inserido pelo usuário
tempo_preparo_miojo = input("Insira o tempo de preparo do miojo: ")

# Captura tempo da primeira ampulheta inserido pelo usuário
tempo_ampulheta_1 = input("Insira o tempo da primeira ampulheta "
        "(deve ser maior que {}): ".format(tempo_preparo_miojo))

# Enquanto o usuário não digitar um valor válido, pede um novo valor
while tempo_ampulheta_1 <= tempo_preparo_miojo:
    tempo_ampulheta_1 = input("Valor deve ser maior que o "
        "tempo de preparo do miojo, insira o tempo da primeira "
        "ampulheta novamente: ")

# Captura tempo da segunda ampulheta inserido pelo usuário
tempo_ampulheta_2 = input("Insira o tempo da segunda ampulheta "
        "(deve ser maior que {}): ".format(tempo_preparo_miojo))

# Enquanto o usuário não digitar um valor válido, pede um novo valor
while tempo_ampulheta_2 <= tempo_preparo_miojo:
    tempo_ampulheta_2 = input("Valor deve ser maior que o "
        "tempo de preparo do miojo, insira o tempo da segunda" 
        "ampulheta novamente: ")

# tempo_maximo_preparo = input("Insira o maximo para preparo do miojo: ")

# Cria instancias para as ampulhetas e miojo
ampulheta_1 = Ampulheta(tempo_ampulheta_1)
ampulheta_2 = Ampulheta(tempo_ampulheta_2)
miojo = Miojo(tempo_preparo_miojo)

# Calcula MDC dos valores das ampulhetas
mdc = calcula_mdc(ampulheta_1.get_tempo(), ampulheta_2.get_tempo())

# Verifica se é possível calcular o tempo com as ampulhetas informadas
if miojo.get_tempo_preparo() % mdc:
    print("Não é possível obter o tempo de cozimento exato com os" 
          "valores das ampulhetas informadas.")
    sys.exit()

tempo_total_preparo = 0
tempo_cozimento = 0
tempo_ampulheta_1_aux = ampulheta_1.get_tempo() 
tempo_ampulheta_2_aux = ampulheta_2.get_tempo()

# Faz iterações com as ampulhetas, utilizando o maior valor possivel para um inteiro como o maior tempo de preparo,
# exagero apenas para testarmos o programa.
while tempo_total_preparo < sys.maxint:
    tempo_cozimento = tempo_ampulheta_1_aux if tempo_ampulheta_1_aux < tempo_ampulheta_2_aux else tempo_ampulheta_2_aux

    if tempo_cozimento == miojo.get_tempo_preparo():
        tempo_total_preparo += tempo_cozimento
        break
    else:
        if tempo_ampulheta_1_aux > tempo_ampulheta_2_aux:
            tempo_ampulheta_1_aux = tempo_ampulheta_1_aux - tempo_ampulheta_2_aux
            tempo_total_preparo += tempo_ampulheta_2_aux
            tempo_ampulheta_2_aux = ampulheta_2.get_tempo()
        else:
            tempo_ampulheta_2_aux = tempo_ampulheta_2_aux - tempo_ampulheta_1_aux
            tempo_total_preparo += tempo_ampulheta_1_aux
            tempo_ampulheta_1_aux = ampulheta_1.get_tempo()

print("Tempo das ampulhetas: {} e {} minutos.".format(ampulheta_1.get_tempo(), ampulheta_2.get_tempo()))
print("Tempo total de preparo do miojo: {} minutos.".format(tempo_total_preparo))
print("Tempo de cozimento do miojo: {} minutos.".format(tempo_cozimento))