# arr = [89, 86, 77, 78, 25, 69, 26, 20, 98, 56, 6, 7, 13, 97, 91, 27, 87, 74, 75, 36, 42, 23, 8, 13, 61, 7, 13, 11, 5,
#        74, 90, 29, 100, 36, 3, 20, 11,
#        89, 61, 11, 82, 62, 14, 5, 76, 72, 37, 26, 88, 21, 19, 8, 87, 21, 60, 22, 94, 14, 5, 2, 1, 88, 62, 63, 2, 93, 98,
#        69, 15, 80, 30, 92, 54, 65, 97, 96, 54,
#        91, 8, 33, 71, 77, 99, 5, 86, 12, 31, 9, 90, 97, 69, 88, 88, 7, 15, 29, 13, 57, 56, 92]
# expected output - 87

arr = [3, 2, 3, 5]
# expected = 4

_len = len(arr)
arr.sort()

"""code to make starting position 1"""
if arr[0] != 1:
    num_to_substract = arr[0] - 1
    arr = [i - num_to_substract for i in arr]

max_elem = arr[-1]
_start = 0
_next = 1

while _next < _len:
    if arr[_next] - arr[_start] > 1:
        arr[_next] = arr[_start] + 1
    _start += 1
    _next += 1

if arr[-1] > max_elem:
    print(max_elem)
elif arr[-2] == arr[-3]:
    print(max_elem)
else:
    print(arr[-1])
