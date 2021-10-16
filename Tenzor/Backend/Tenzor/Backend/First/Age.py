while True:
    age = input('Введите ваш возраст: ')
    exception = [11,12,13,14]
    if int(age[-2:]) in exception:
        print(f'Вам {age} лет')
    else:
        if int(age) % 10 == 1:
            print(f'Вам {age} год')
        else:
            if int(age) % 10 == 4 or int(age) % 10 == 3 or int(age) % 10 == 2:
                print(f'Вам {age} года')
            else:
                print(f'Вам {age} лет')

