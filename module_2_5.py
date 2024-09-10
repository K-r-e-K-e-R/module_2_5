def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list = []
        for j in range(m):
            list.append(value)

        matrix.append(list)
    return matrix


n = 4
m = 6
value = 28
matrix = get_matrix(n, m, value)
for result in matrix:
    print(result)
