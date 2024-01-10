#Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
#m = 2, n = 3 -> A(m,n) = 9
#m = 3, n = 2 -> A(m,n) = 29

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
m = int(input("m = "))
n = int(input("n = "))
result = ackermann(m, n)
print(f"A ({m}, {n}) = {result}")
