money = int(input('Введите сумму вклада: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(map(lambda deposit_rate: round(deposit_rate*money/100), per_cent.values()))
print('Суммы накопленных средств:',deposit)  
print('Максимальная сумма, которую вы можете заработать —', max(deposit))