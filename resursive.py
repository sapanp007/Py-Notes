"""
Steps:
1. prepare base case where we know the exact return
2. get the pattern and then relate
"""

#print sum of all non negative ints up to n
# def sum(n):
# 	if n == 0:
# 		return 0
# 	else:
# 		return sum(n-1)+n
# print(sum(8))


l1 = [4, 90, 1, 3, 81, 98, 81, 98]
l2 = [{90: 5}, 5, [2, 3, 4], [{81: 9, 98: 1}, {81: 9, 98: 2}], 9, 0, 9, 0]
z1 = sorted(list(zip(l1, l2)))
print(z1)
l3 = [4, 90, 1, 3, 81, 98, 81, 98]
l4 = [{90: 5}, 5, [2, 3, 4], {81: 9, 98: 2}, {81: 9, 98: 1}, 9, 0, 9, 0]
z2 = sorted(list(zip(l3, l4)))
print(z2)
final_z = sorted(list(zip(z1, z2)))
print(final_z)

# for i in final_z:
# 	if i[0][1] != i[1][1]:

