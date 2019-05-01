matrix = [[1,2,3],
          [2,3,3],
          [5,4,6]]

# Podemos ver toda la matriz
# print(matrix)

# Podemos recorrerla por filas
# for fila in matrix:
#     print(fila)

# Podemos recorrerla por elementos
for fila in matrix:
    for elemento in fila:
        print(elemento)

# Para obtener un elemento dado su indice
# print(matrix[0][2])

# Recorramos las filas por indices
# for i in range(len(matrix)):
#     print(matrix[i])

# Recorrer por indices cada elemento
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
