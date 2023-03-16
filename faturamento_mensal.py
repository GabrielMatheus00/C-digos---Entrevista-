SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.5
estados = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}
valores = estados.values()
total = sum(valores)
for estado in estados.keys():
    percentual = (estados[estado] / total) * 100
    print(f'O percentual do total de {estado} referente ao total é de {percentual:.2f}%')

