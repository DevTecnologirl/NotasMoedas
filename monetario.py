# Função para calcular o número de notas e moedas
def calcular_notas_moedas(valor):
    # Definindo as notas e moedas disponíveis
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

    # Armazenando a quantidade de cada nota e moeda
    resultado_notas = {}
    resultado_moedas = {}

    # Convertendo o valor para centavos para facilitar o cálculo
    valor_cents = int(round(valor * 100))

    # Calculando notas
    for nota in notas:
        num_notas = valor_cents // (nota * 100)  # Convertendo nota para centavos
        resultado_notas[nota] = num_notas
        valor_cents %= (nota * 100)

    # Calculando moedas
    for moeda in moedas:
        num_moedas = valor_cents // int(moeda * 100)  # Convertendo moeda para centavos
        resultado_moedas[moeda] = num_moedas
        valor_cents %= int(moeda * 100)

    return resultado_notas, resultado_moedas

# Entrada
valor = float(input())

# Chamando a função e imprimindo o resultado
resultado_notas, resultado_moedas = calcular_notas_moedas(valor)

print("NOTAS:")
for nota in [100, 50, 20, 10, 5, 2]:
    print(f"{resultado_notas[nota]} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
for moeda in [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]:
    print(f"{resultado_moedas[moeda]} moeda(s) de R$ {moeda:.2f}")
