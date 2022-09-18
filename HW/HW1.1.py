message = "Пароль принят"
message_error = "Пароль не принят"
password = input("Введите пароль: ")
password_second = input("Подтверите пароль: ")
if password == password_second:
    print(message)
else:
    print(message_error)
# test
