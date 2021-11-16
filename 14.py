def f():
    print("Введите число:")
    a = int(input())
    print("Введите число:")
    b = int(input())
    for i in range(a, b + 1):
        print(f"{i} " * i)
    f_ans()


def f_2():
    print("Введите число:")
    a = int(input())
    print("Введите число:")
    b = int(input())
    ans = a
    for i in range(a // b):
        ans -= b
    print(ans)
    f_ans()


def f_3():
    print("Введите число")
    a = int(input())
    ans, r = 0, 1
    while a > ans:
        ans += r
        r += 1
    r -= 1
    print(f"Наименьшее K: {r}")
    print(f"Сумма: {ans}")
    f_ans()


def f_4():
    print("Введите процент (0 < P < 25)")
    a = int(input())
    s = 1000
    ans = 0
    while s <= 1100:
        s += s * (a / 100)
        ans += 1
    print(f"За {ans} месяца размер вклада будет {s} рублей.")
    f_ans()


def f_5():
    print("Введите число")
    a = int(input())
    print("Введите степень")
    b = int(input())
    while a != b:
        sp = sorted([a, b])
        a, b = sp[1] - sp[0], sp[0]
    print(f"Наибольший общий делитель: {a}")
    f_ans()


def f_6():
    print(f"Введите число Фибоначчи:")
    word = int(input())
    a, b = 0, 1
    count = 2
    if word == 0:
        print("Порядковый номер в последовательности: 1")
    elif word == 1:
        print("Порядковый номер в последовательности: 2")
    else:
        while b != word:
            a, b = b, a + b
            count += 1
        print(f"Порядковый номер в последовательности: {count}")
    f_ans()


def f_ans():
    print("Выберите номер задания от 1 до 6:")
    print("Для завершения программы введите 0")
    ans = int(input())
    if ans == 0:
        print("Конец программы.")
    elif ans == 1:
        f()
    elif ans == 2:
        f_2()
    elif ans == 3:
        f_3()
    elif ans == 4:
        f_4()
    elif ans == 5:
        f_5()
    elif ans == 6:
        f_6()
    else:
        print("Error, try again")
        f_ans()


f_ans()
