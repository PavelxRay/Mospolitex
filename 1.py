def f():
    a = int(input())
    b = int(input())
    print(f"S = {a * b}")
    print(f"P = {2 * (a + b)}")


def f_2():
    P = 3.14
    d = int(input())
    print(P * d)


def f_3():
    a = int(input())
    b = int(input())
    print((a + b) / 2)


def f_4():
    a = int(input())
    b = int(input())
    print(f"Сумма квадратов a и b: {a ** 2 + b ** 2}")
    print(f"Разность квадратов a и b: {a ** 2 - b ** 2}")
    print(f"Произведение квадратов a и b: {a ** 2 * b ** 2}")
    print(f"Разность квадратов a и b: {a ** 2 / b ** 2}")


def f_5():
    a = int(input())
    b = int(input())
    print(f"Сумма: {abs(a) + abs(b)}")
    print(f"Разность: {abs(a) - abs(b)}")
    print(f"Произведение: {abs(a) * abs(b)}")
    print(f"Разность: {abs(a) / abs(b)}")


f()
f_2()
f_3()
f_4()
f_5()