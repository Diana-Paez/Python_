#CICLOS ANIDADOS
matriz = [
    [1,2,3],
    [3,4,5],
    [6,7,8]
]
print(matriz)

print("---------------------")
print(matriz[0][1])
print("---------------------")
for row in matriz:
    print(row)
    for column in row:
        print(column)
        