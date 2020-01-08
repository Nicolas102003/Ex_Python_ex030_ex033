dist = int(input('Qual a distancia da sua viagem ??'))
print('Para uma viagem de {} Km '.format(dist))
if dist <= 200:
    preco1 = dist * 0.50
    print('O preço da passagem é R$:{:.2f}'.format(preco1))
else:
    preco2 = dist *0.45
    print('O preço da Passagem será R$:{:.2f}'.format(preco2))