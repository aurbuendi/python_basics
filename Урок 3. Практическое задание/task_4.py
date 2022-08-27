"""
4. Программа принимает действительное положительное число x
   и целое отрицательное число y.
   Необходимо выполнить возведение числа x в степень y.
   Задание необходимо реализовать в виде функции my_func(x, y).

   При решении задания необходимо обойтись без встроенной функции
   возведения числа в степень!

   ВНИМАНИЕ: использование встроенной функции = задание не принято
   Постараться придумать свой алгоритм без **
"""


# Не смог себя заставить определить переменные через x и y ://
def my_func(user_x, user_y):
    x_deg = user_x
    while user_y < -1:
        user_x = user_x * x_deg
        user_y += 1
    x_pow_y = 1 / user_x
    return x_pow_y


u_quit = 0
while u_quit != "1":
    # Вводим х с проверкой.
    us_x = input(f"Введите x. Любое действительное число "
                 f"будет положительным: ")
    if type(us_x) != float:
        while type(us_x) != float:
            try:
                us_x = abs(float(us_x))
            except ValueError:
                print("Внимательнее! Введите число.")
                us_x = input(f"Введите x. Любое действительное число "
                             f"будет положительным: ")
    print(f"Полученное число: {us_x}")
    # Вводим y с проверкой.
    us_y = input(f"Введите y. Любое число будет целым "
                 f"отрицательным: ")
    if type(us_y) != int:
        while type(us_y) != int:
            try:
                us_y = -(abs(int(us_y)))
            except ValueError:
                print("Внимательнее! Введите целое число.")
                us_y = input(f"Введите y. Любое число будет целым "
                             f"отрицательным: ")
    print(f"Полученное число: {us_y}")

    print(f" my_func: Возведение в степень x на y: {my_func(us_x, us_y)}")
    print(f"  Python: Возведение в степень x на y: {us_x ** us_y}")
    u_quit = input("QUIT - 1: ")
