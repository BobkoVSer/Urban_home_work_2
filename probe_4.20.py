team_num_1 = 5
print('в команде мастера кода участников %s !' % ('5'))

team_num_1 = 6
team_num_2 = 6
print('итого сегодня в командах участников %s и' % ('5'), ('6'))


score_2 = 42
print('команда Волшебники данных решили задач {}:'.format('42'))

real_time = 18015.2
print('Волшебники данных решили задачу за {0:5.1f} с '.format(real_time))

score_1 = 40
score_2 = 42
print(f'Команды решили - {score_1} и {score_2} задачи')

team_time_1 = 1552.512
team_time_2 = 2153.31451

task_total = 82
time_avg = 45.2
print(f'Сегодня было решено - {task_total} задач, в среднем - {time_avg} с. за одну задачу')

if score_1 > score_2 or score_1 == score_2 and team_num_1 > team_num_2:
    result = 'результат битвы: Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team_num_1 < team_num_2:
    result = 'результат битвы: Победа команды Волшебники Данных!'
else: result = ('Ничья!’')
print(f'{result}')