try:
    x = (input())
    if float(x) < 0:
        raise ValueError
except ValueError as error:
    print("Некорректный формат", error)
else:
    money = x.split(".")
    print("{} руб. {} коп.".format(money[0], money[1]))