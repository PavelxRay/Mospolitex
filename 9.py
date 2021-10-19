def f():
    print("Введите количество секунд с начала новых суток:")
    a = int(input())
    print(f"Количество секунд, прошедших с начала последней минуты: {int(a % 60)}")
    f_ans()


def f_2():
    sl = {1: "Понедельник",
          2: "Вторник",
          3: "Среда",
          4: "Четверг",
          5: "Пятница",
          6: "Суббота",
          0: "Воскресенье"}
    print("Введите день этого года:")
    a = int(input())
    print(f"День недели этого дня: {sl[a % 7]}")
    f_ans()


def f_3():
    sl = {1: "Понедельник",
          2: "Вторник",
          3: "Среда",
          4: "Четверг",
          5: "Пятница",
          6: "Суббота",
          0: "Воскресенье"}
    print("Введите день этого года:")
    a = int(input())
    print("Введите день недели для 1 января:")
    key_list = list(sl.keys())
    val_list = list(sl.values())
    b = key_list[val_list.index(input())]
    print(f"День недели этого дня: {sl[a % 7 + (b - 1)]}")
    f_ans()


def f_4():
    print("Введите сторну A:")
    a = int(input())
    print("Введите сторну B:")
    b = int(input())
    print("Введите сторну C:")
    c = int(input())
    print(f"Квадратов со строной C помещается: {(a // c) * (b // c)}")
    print(f"Незанятая площадь: {(a * b) - (((a // c) * (b // c)) * c ** 2)}")
    f_ans()


def f_5():
    print("Введите номер года:")
    a = int(input())
    if a % 100:
        print(f"{a // 100 + 1} номер столетия")
    else:
        print(f"{a // 100} номер столетия")
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
