RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range(6):
    if i < 3:
        print(f'{WHITE}{" " * 15}{END}')
    else:
        print(f'{RED}{" " * 15}{END}')

print()

for i in range(5):
    if i == 0:
        print(f'{WHITE}{" " * 20}{END}')
    if i == 1:
        print(f'{" " * 8}{WHITE}{" " * 5}{END}')
    if i == 2:
        print(f'{WHITE}{" " * 20}{END}')
    if i == 3:
        print(f'{" " * 2}{WHITE}{" " * 4}{END}{" " * 8}{WHITE}{" " * 4}{END}')
    if i == 4:
        print(f'{WHITE}{" " * 20}{END}')

plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 0.5          # <-- здесь была степень 3, заменил на 0.5

step = round(abs(result[0] - result[9]) / 9, 2)
print(step)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8 - i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k + 1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)

print('\t0t1 2 3 4 5 6 7 8 9')

file = open('sequence.txt', 'r')
numbers = []
for line in file:
    numbers.append(float(line))
file.close()
first_half = numbers[:125]
second_half = numbers[125:250]
first_avg = sum(abs(x) for x in first_half) / len(first_half)
second_avg = sum(abs(x) for x in second_half) / len(second_half)
print(f'Среднее по модулю первых 125 чисел: {first_avg}')
print(f'Среднее по модулю вторых 125 чисел: {second_avg}')