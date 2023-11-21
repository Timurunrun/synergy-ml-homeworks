def nod(x, y):
    while y:
        x, y = y, x % y
    return x

def nok(a, b):
    return abs(a * b) // nod(a, b)

a = int(input())
b = int(input())

result = nok(a, b)
print(result)

