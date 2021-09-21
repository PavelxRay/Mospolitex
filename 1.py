print("Выберите число от 1 до 5")
ans = int(input())


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


if ans == 1:
    f()
elif ans == 2:
    f_2()
elif ans == 3:
    f_3()
elif ans == 4:
    f_4()
elif ans == 5:
    f_5()
else:
    print("Error, try again")
    ans = int(input())
