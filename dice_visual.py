import sys

from die import Die
import pygal

# Запрашивает количество кубиков.
dice = int(input('Number of dices, from 1 to 3: '))
# Если количество кубиков >3 или <1, выполнение программы завершается.
if dice > 3:
    print('Too many dice')
    sys.exit()

elif dice < 1:
    print('To few dice')
    sys.exit()
# Запрос на ввод количества граней кубика.
num_sides = int(input('Number of sides of the dice: '))
# Запрашивает количество бросков
rolls = int(input('Number of dice rolls: '))

# Создание кубика/ов.
die = Die(rolls=rolls, num_sides=num_sides, dices=dice)

# Принимаем результаты.
results = die.roll()
print(results)

# Анализ результатов.
frequencies = []
max_result = dice * num_sides
# Вычисляет, сколько раз выпал каждый из возможных вариантов.
for value in range(dice, max_result+1):
    frequency = results.count(value)  # Частота = список результатов.вернуть количество вхождений значения(1)
    frequencies.append(frequency)
print(frequencies)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = f"Results of rolling {dice} D{num_sides} dice {rolls} times."

hist.x_labels = [i for i in range(dice, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add(f'{dice} dice D{num_sides}', frequencies)
hist.render_to_file(f'{dice}_D{num_sides}_dice_{rolls}_rolls_visual.svg')
