"""
Steps:
1. prepare base case where we know the exact return
2. get the pattern and then relate
"""
# d = {}
#
#
# def sum_r(n):
#     if n - 1 in d:
#         return n + d[n - 1]
#     else:
#         if n == 1:
#             return 1
#         else:
#             d[n - 1] = sum_r(n - 1)
#             return n + d[n-1]
#
#
# def sum_d(n):
#     if n == 1:
#         return 1
#     else:
#         return sum_d(n-1) + n
#
#
# # print(sum_r(5))
# for i in range(1, 1001):
#     print(i, sum_r(i))
