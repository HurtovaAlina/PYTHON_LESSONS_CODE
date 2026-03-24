# Для матриці
# m = [[1,2,3], [4,5,6], [7,8,9]]
# вивести:
#
# 1 2 3
# 4 5 6
# 7 8 9

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in m:
    print(*i)

# Знайти суму всіх елементів матриці.
s = 0
for i in m:
    for j in i:
        s += j
print("SUM = ", s)
# варіант 2. s = sum(sum(row) for row in m)

# Знайти максимальний та мінімальний елемент.
max_val = m[0][0]
min_val = m[0][0]

for i in m:
    for j in i:
        if j > max_val:
            max_val = j
        elif j < min_val:
            min_val = j

print("MAX = ", max_val)
print("MIN = ", min_val)
# варіант 2.
# max_val = max(max(row) for row in m)
# min_val = min(min(row) for row in m)

# Знайти суму елементів головної діагоналі.
# (1 + 5 + 9)
s_diag = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if i == j:
            s_diag += m[i][j]

print("SUM DIAG ", s_diag)
# варіант 2.
# s_diag = 0
# for i in range(len(m)):
#     s_diag += m[i][i]
# s_diag= sum(m[i][i] for i in range(len(m)))


# Знайти суму елементів побічної діагоналі.
# (3 + 5 + 7)
s_rev_diag = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if j == (len(m) - 1) - i:
            s_rev_diag += m[i][j]

print("SUM REV DIAG ", s_rev_diag)

# варіант 2.
# for i in range(len(m)):
#   s_rev_diag += m[i][(len(m)-1)-i]
# s_rev_diag = sum(m[i][(len(m)-1)-i] for i in range(len(m)))
