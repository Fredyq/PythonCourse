password = input("Введите пароль: ")
password1 = ""
if len(password) < 4:
    d = "Недопустимый пароль"
    print(d)
elif password.isdigit():
    if len(password) > 7:
        d = "Ненадежный пароль"
        print(d)
elif password.isalnum():
    if len(password) <= 10:
        d = "Слабый пароль"
        print(d)
if password.isalnum():
    if len(password) >10:
         d = "Надежный пароль"
         print(d)