a = 16
b = 4

def division(a, b):
    if b == 0:
        print("Помилка: Ділення на нуль!")
        return None
    else:
        return a / b

c = division(a, b)

if c is not None:
    print("a =", a)
    print("b =", b)
    print("c =", c)
