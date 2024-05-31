def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        dict = []
        for j in range(m):
            dict.append(value)
        matrix.append(dict)
    return matrix
n = 2
m = 2
value = 555

result_matrix = get_matrix(n, m, value)
for dict in result_matrix:
    print(dict)