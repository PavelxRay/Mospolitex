def f():
    print("Введите целое число N (N > 0)")
    sp = []
    a = int(input())
    arr = 1
    for i in range(a):
        sp.append(arr)
        arr += 2
    print(f"Массив: {sp}")
    f_ans()


def f_2():
    print("Введите длинну массива:")
    n = int(input())
    print("Введите первый элемент массива:")
    a = int(input())
    print("Введите знаменатель геометрической прогрессии:")
    d = int(input())
    sp = [a]
    for i in range(n - 1):
        arr = sp[i]
        arr *= d
        sp.append(arr)
    print(f"Массив: {sp}")
    f_ans()


def f_3():
    print("Введите длинну массива:")
    n = int(input())
    print("Введите первый элемент массива:")
    a = int(input())
    print("Введите второй элемент массива:")
    b = int(input())
    sp = [a, b]
    for i in range(n - 2):
        arr = sum(sp)
        sp.append(arr)
    print(f"Массив: {sp}")
    f_ans()


def f_4():
    print("Введите длинну массива")
    n = int(input())
    arr = 1
    sp = []
    sp1 = []
    for i in range(n):
        sp.append(arr)
        arr += 1
    print(f"Массив до изменений {sp}")
    if not(n % 2):
        for i in range(1, n // 2 + 1):
            sp1.append(sp[0])
            sp1.append(sp[-1])
            sp.pop(0)
            sp.pop(-1)
        print(f"Массив после изменений {sp1}")
    else:
        for i in range(1, n // 2 + 1):
            sp1.append(sp[0])
            sp1.append(sp[-1])
            sp.pop(0)
            sp.pop(-1)
        sp1.append(sp[0])
        sp.pop(0)
        print(f"Массив после изменений {sp1}")

    f_ans()


def f_5():
    print("Введите размер массива:")
    n = int(input())
    arr = 1
    sp = []
    spch = []
    spnch = []
    finalsp = []
    for i in range(n):
        sp.append(arr)
        arr += 1
    print(f"Массив до изменений {sp}")
    for i in sp:
        if i % 2:
            spnch.append(i)
        else:
            spch.append(i)
    spch = sorted(spch)
    spnch = sorted(spnch)

    for i in spnch:
        finalsp.append(i)
    for i in spch:
        finalsp.append(i)
    print(f"Массив после изменений: {finalsp}")
    f_ans()


def f_ans():
    print("Выберите номер задания от 1 до 5:")
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
    else:
        print("Error, try again")
        f_ans()


f_ans()
