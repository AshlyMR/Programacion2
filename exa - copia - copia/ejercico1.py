N = int(input("Ingrese N: "))
num = 1
serie = []
while len(serie) < N:
    repeticiones = 2 * num - 1
    for i in range(repeticiones):
        serie.append(num)
        if len(serie) == N:
            break
    num += 1
print(serie)
