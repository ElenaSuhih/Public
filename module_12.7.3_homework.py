per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input("введите сумму, которую планируете внести"))
promoney=int(money/100)

tkb=int((per_cent['ТКБ'])*promoney)
skb=int((per_cent['СКБ'])*promoney)
vtb=int((per_cent['ВТБ'])*promoney)
sber=int((per_cent['СБЕР'])*promoney)

deposit=[tkb,skb,vtb,sber]
print('you can have in each bank:', deposit)
print("maximum amount of the sum you can get - ", max(deposit))

