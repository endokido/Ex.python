# CALCULADORA DE GRANDEZAS

import os
os.system('cls')

print('== Algoritmo para calcular grandezas elétricas (Lei de Ohm) ==')
print("")

# ENTRADA DE DADOS

v_tensao = float(input('Qual é o valor da tensão?'))
i_corrente = float(input('Qual é o valor da corrente?'))
r_resistencia = float(input('Qual é o valor da resistência?'))

print("")
print('== RESULTADO ==')
print("")

# PROCESSAMETNO E SAÍDA DE DADOS!

if v_tensao == 0:
    # V = R.I
    v_tensao = r_resistencia * i_corrente
    print(f'O resultado da tensão é {v_tensao:.0f}V')

elif i_corrente == 0:
    # I = V/R
    i_corrente = v_tensao / r_resistencia
    print(f'O resultado da corrente é {i_corrente:.0f}A')

elif r_resistencia == 0:
    # R = V/I
    r_resistencia  = v_tensao / i_corrente
    print(f'O resultado da resistência é {r_resistencia:.0f}Ω') 

