import math

a, b, c = input().split()
print(round(float(a), 2))
print(math.sqrt(int(b)))
print(math.floor(float(c)))

def process_input():
    input_line = input()

    parts = input_line.split()

    first_float = float(parts[0])
    second_int = int(parts[1])
    third_float = float(parts[2])

    rounded_first = round(first_float, 2)
    sqrt_second = math.sqrt(second_int)
    floor_third = math.floor(third_float)

    print(rounded_first)
    print(sqrt_second)
    print(floor_third)

# ТЕСТЫ
def test1():
    print("\n Тест 1: обычные числа ")

    x = round(3.14159, 2)
    print("Округление 3.14159:", x, "✓" if x == 3.14 else "✗")

    y = math.sqrt(16)
    print("Корень из 16:", y, "✓" if y == 4.0 else "✗")

    z = math.floor(5.8)
    print("Округление 5.8 вниз:", z, "✓" if z == 5 else "✗")

def test2():
    print("\n Тест 2 отрицательные числа ")
    x = round(-1.234, 2)
    print("Округление -1.234:", x, "✓" if x == -1.23 else "✗")

    y = math.sqrt(9)
    print("Корень из 9:", y, "✓" if y == 3.0 else "✗")

    z = math.floor(-2.3)
    print("Округление -2.3 вниз:", z, "✓" if z == -3 else "✗")

def test3():
    print("\n Тест 3 большие числа ")
    x = round(5.678, 2)
    print("Округление 5.678:", x, "✓" if x == 5.68 else "✗")

    y = math.sqrt(10000)
    print("Корень из 10000:", y, "✓" if y == 100.0 else "✗")

    z = math.floor(7.999)
    print("Округление 7.999 вниз:", z, "✓" if z == 7 else "✗")

def test4():
    print("\n Тест 4: маленькие числа ")
    x = round(0.001, 2)
    print("Округление 0.001:", x, "✓" if x == 0.0 else "✗")

    y = math.sqrt(1)
    print("Корень из 1:", y, "✓" if y == 1.0 else "✗")

    z = math.floor(0.001)
    print("Округление 0.001 вниз:", z, "✓" if z == 0 else "✗")

def test5():
    print("\n Тест 5: проверка всех операций ")
    res1 = round(2.675, 2)
    res2 = math.sqrt(144)
    res3 = math.floor(9.999)

    print("Округление 2.675:", res1, "✓" if res1 == 2.68 else "✗")
    print("Корень из 144:", res2, "✓" if res2 == 12.0 else "✗")
    print("Округление 9.999 вниз:", res3, "✓" if res3 == 9 else "✗")

# запуск тестов
print("\n zapusk ТЕСТОВ ")
test1()
test2()
test3()
test4()
test5()
print("\n ТЕСТЫ ЗАВЕРШЕНЫ ")
