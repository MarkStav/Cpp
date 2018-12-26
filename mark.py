import math
def intInput():
    a = int(input())
    return a
def solver1(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        print("Уравнение имеет 2 корня:  ", (- b + math.sqrt(D)) / 2 * a, ' ', (- b - math.sqrt(D)) / 2 * a)
    elif D == 0:
        print("Уравнение имеет 1 корнь:   ", (- b + math.sqrt(D)) / 2 * a)
    else:
        print(" Нет решения")


def solver2(a, b, c, d):
    n = 1
    print("Найдем корень с помощью схемы Горнера")
    print('|', a, '|', b, '|', c, '|', d, '|')
    while n <= abs(d):
        if d % n == 0:
            a1 = a
            b1 = a1 * n + b
            c1 = b1 * n + c
            d1 = c1 * n + d
            print('|', a1, '|', b1, '|', c1, '|', d1, '|')
            if d1 == 0:
                print("Корень:  ", n)
                solver1(a1, b1, c1)
                break
            a1 = a
            b1 = a1 * (-n) + b
            c1 = b1 * (-n) + c
            d1 = c1 * (-n) + d
            
            if d1 == 0:
                print("Корень:  ", n)
                solver1(a1, b1, c1)
                break


n += 1
def solver3(a, b, c, d, e):
    n = 1
    print("Найдем корень с помощью схемы Горнера")
    print('|', a, '|', b, '|', c, '|', d, '|', e,'|')
    while n <= abs(e):
        if e % n == 0:
            a1 = a
            b1 = a1 * n + b
            c1 = b1 * n + c
            d1 = c1 * n + d
            e1 = d1 * n + e
            print('|', a1, '|', b1, '|', c1, '|', d1, '|', e,'|')
            if e1 == 0:
                print("Корень:  ", n)
                solver2(a1, b1, c1, d1)
                break
            a1 = a
            b1 = a1 * (-n) + b
            c1 = b1 * (-n) + c
            d1 = c1 * (-n) + d
            e1 = d1 * (-n) + e
            
            if e1 == 0:
                print("Корень:  ", n)
                solver2(a1, b1, c1, d1)
                break

n += 1
def solver4(a, b, c, d, e, f):
    n = 1
    print("Найдем корень с помощью схемы Горнера")
    print('|', a, '|', b, '|', c, '|', d, '|', e,'|', f, '|')
    while n <= abs(f):
        if f % n == 0:
            a1 = a
            b1 = a1 * n + b
            c1 = b1 * n + c
            d1 = c1 * n + d
            e1 = d1 * n + e
            f1 = e1 * n + f
            print('|', a1, '|', b1, '|', c1, '|', d1, '|', e1, '|', f1, '|')
            if f1 == 0:
                print("Корень:  ", n)
                solver3(a1, b1, c1, d1, e1)
                break
            a1 = a
            b1 = a1 * (-n) + b
            c1 = b1 * (-n) + c
            d1 = c1 * (-n) + d
            e1 = d1 * (-n) + e
            f1 = e1 * (-n) + f
            
            if f1 == 0:
                print("Корень:  ", n)
                solver3(a1, b1, c1, d1, e1)
                break

n += 1

print("[1] - квадратное \n[2] - кубическое \n[3] - мнгочлен с 4 степенью \n[4] - мнгочлен с 5 степенью")
n = int(input("Выберите уравнение для решения:   "))
if n == 1:
    print("Введите уравнение вида ax^2+bx+c")
    a, b, c = intInput(), intInput(), intInput()
    solver1(a, b, c)
elif n == 2:
    print("Введите уравнение вида ax^3+bx^2+cx+d")
    a, b, c, d = intInput(), intInput(), intInput(), intInput()
    solver2(a, b, c, d)
elif n == 3:
    print("Введите уравнение вида ax^4+bx^3+cx^2+dx+e")
    a,b,c,d,e = intInput(), intInput(), intInput(), intInput(), intInput()
    solver3(a,b,c,d,e)
elif n == 4:
    print("Введите уравнение вида ax^5+bx^4+cx^3+dx^2+ex+f")
    a, b, c, d, e, f = intInput(), intInput(), intInput(), intInput(), intInput(), intInput()
    solver4(a, b, c, d, e, f)
