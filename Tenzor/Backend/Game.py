start = 1
end = 100
while True:
    number = (start+end)//2
    answer = input(f'Ваше число: {number}?\n(Верно, Больше, Меньше)\n')
    if answer == 'Верно':
        print('Tadaaaaaa!')
        break
    elif answer == 'больше':
        start = number + 1
    else:
        end = number - 1