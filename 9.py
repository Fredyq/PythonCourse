moneyInBank = {2000: 10, 1000: 10, 500: 10, 200: 10, 100: 10, 50: 10, 10: 10}
result = {2000: 0, 1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 10: 0}
money = int(input('Действующие банкноты:,2000,1000,500,200,100,50,10\nВведите сумму:'))
for key in moneyInBank.keys():
    current = money // key 
    if current > moneyInBank[key]:
        money = money - (moneyInBank[key] * key)
        result[key] = moneyInBank[key]
    else:
        money = money % key
        result[key] = current
print("Ваша наличка : " + str(sum([k * v for k, v in zip(result.keys(), result.values())])))
print(result)