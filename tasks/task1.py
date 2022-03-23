"""
Нужно сначала вывести средний балл всех учеников и сравнить со своим баллом
если ваш балл ниже среднего значить False а если выше
нужно вернуть True
"""

def better_then_average(class_points, your_points):
    # return True if (sum(class_points) / len(class_points)) < your_points else False
    if (sum(class_points) / len(class_points)) < your_points:
        return True
    else:
        return False

# better_then_average(class_points=[2, 3, 100, 40, 60], you_points=70)
#========================================================================================================================
"""
Вы решили арендовать машину , Арендатель вам говорит
Аренда в день стоит 40$ 
Если вы будете арендовать больше или равно 7 дней , он дает скидку 50$
Если вы арендуете меньше 7 дней но больше 3 дней , он дает скидку 20$
"""

def seishely(d):
    if d >= 7:
        return (d * 40) - 50
    elif d > 3 and d < 7:
        return (d * 40) - 20
    else:
        pass

day_1 = 1
day_2 = 4
day_3 = 8

print(seishely(day_3))