moeda = str(input('Digite o nome da moeda: '))
buy = float(input('Digite o preço de compra da moeda {}: '.format(moeda)))
stop = float(input('Agora digite o preço do StopLoss: '))

diff = stop - buy
percent = (diff / buy) * 100
calc = percent / 100
alocar = (0.01 / calc) * 100


print(' Considerando que a distância do seu stop esta a {:.2f}% de distância'.format(percent))
print('Você tera que investir {:.2f}% do capital '.format(alocar))