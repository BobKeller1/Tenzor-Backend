number = input('Введите число: ')

sum_odd = 0
sum_even = 0
for i in number:
    if int(i) % 2 == 0:
        sum_even += int(i)
    else:
        sum_odd += int(i)

print((f'{sum_even} {sum_odd}'))



