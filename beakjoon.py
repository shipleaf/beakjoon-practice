# 27433번

# a = 1
# p = int(input())

# if p == 0:
#     a=1
# else:    
#     for i in range (1, p+1):
#         a = a*i

# print(a)


# 2566

# ex_array = list(map(int, input().split()))
# print(ex_array)

# max_array = [list(map(int, input().split())) for _ in range(9)]

# max = 0
# row = 0
# column = 0

# for i in range(9):
#     for j in range(9):
#         if max_array[i][j]>=max:
#             max = max_array[i][j]
#             row = i+1
#             column = j+1

# print(max)
# print(row, column, sep=' ')

# 2501

# n, k = map(int, input().split())
# list = []

# for i in range(1,n+1):
#     if n % i == 0:
#         list.append(i)

# if len(list) >= k:
#     print(list[k-1])
# else:
#     print(0)

# 10870

n = int(input())
a = 0
b = 1
c = 0

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(2, n+1):
        c = a+b
        a = b
        b = c
    print(c)
        

