check = True
while check:
    try:
        card = (input("Введите номер карты(16 цифр): "))
        if not len(card) == 16 or not card.isdigit():
            raise ValueError
    except ValueError as error:
        print("Невереный формат")
    else:
        print(card[:4] + '*' * 8 + card[-4:])
        check = False