import string


def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


def verification(login, password, yes, no):
    text = ['в пароле нет ни одной буквы',
            'в пароле нет ни одной заглавной буквы',
            'в пароле нет ни одной строчной буквы',
            'в пароле нет ни одной цифры']
    if not any([i for i in password if i.isalpha() and (i in string.ascii_lowercase or i in string.ascii_uppercase)]):
        failure(login, text[0])
    elif not any([i for i in password if i.isupper() and i in string.ascii_uppercase]):
        failure(login, text[1])
    elif not any([i for i in password if i.islower() and i in string.ascii_lowercase]):
        failure(login, text[2])
    elif not any([i for i in password if i.isdigit()]):
        failure(login, text[3])
    else:
        success(login)


assert (verification('Daniil', 'Riseup123', success, failure)) == success('Daniil')
assert (verification('Mihail', 'Пароль444', success, failure)) == failure('Mihail', 'в пароле нет ни одной буквы')

print('Тест пройден!')
