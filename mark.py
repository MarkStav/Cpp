import math
def solver1 (a,b,c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        print("Уравнение имеет 2 корня:  ", (- b + math.sqrt(D)) / 2 * a, ' ', (- b - math.sqrt(D)) / 2 * a)
    elif D == 0:
        print("Уравнение имеет 1 корнь:   ", (- b + math.sqrt(D)) / 2 * a)
    else:
        print(" Нет решения")
def solver2 (a,b,c,d):
    n = 1
    print("Найдем 1 корень с помощью схемы Горнера")
    print('|', a, '|', b, '|', c, '|', d, '|')
    while n <= abs(d):
        if d % n == 0:
            a1 = a
            b1 = a1 * n + b
            c1 = b1 * n + c
            d1 = c1 * n + d
            print('|', a1, '|', b1, '|', c1, '|', d1, '|')
            if d1 == 0:
                print("Первый корень:  ", n)
                solver1(a1,b1,c1)
                break
            a1 = a
            b1 = a1 * (-n) + b
            c1 = b1 * (-n) + c
            d1 = c1 * (-n) + d
            
            if d1 == 0:
                print("Первый корень:  ", n)
                solver1(a1, b1, c1)
                break
n += 1

print("[1] - квадратное \n[2] - кубическое")
n = int(input("Выберите уравнение для решения:   "))
if n == 1:
    print("Введите уравнение вида ax^2+bx+c")
    a,b,c = int(input()), int(input()), int(input())
    solver1(a, b,   c)
elif n == 2:
    
    print("Введите уравнение вида ax^3+bx^2+cx+d")
    a,b,c,d = int(input()),int(input()),int(input()),int(input())
    solver2(a, b, c, d)
