def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(sorted_list1, sorted_list2, arr):
    ptr1 = 0
    ptr2 = 0
    k = 0
    len_of_list1 = len(sorted_list1)
    len_of_list2 = len(sorted_list2)

    while ptr1 < len_of_list1 and ptr2 < len_of_list2:
        if sorted_list1[ptr1] <= sorted_list2[ptr2]:
            arr[k] = sorted_list1[ptr1]
            ptr1 += 1
        else:
            arr[k] = sorted_list2[ptr2]
            ptr2 += 1
        k += 1
    while ptr1 < len_of_list1:
        arr[k] = sorted_list1[ptr1]
        ptr1 += 1
        k += 1
    while ptr2 < len_of_list2:
        arr[k] = sorted_list2[ptr2]
        ptr2 += 1
        k += 1


if __name__ == "__main__":
    # a = [5, 8, 12, 56, 100]
    # b = [5, 9, 45, 51]
    # print(merge_two_sorted_lists(a, b))
    a = [1, 4, 3, 2, 4, 2, 5]
    merge_sort(a)
    print(a)

