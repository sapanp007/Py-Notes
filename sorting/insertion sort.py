
def insertion_sort(arr):
    for i in range(1, len(arr)):
        anchor = a[i]
        j = i-1
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = anchor


if __name__ == "__main__":
    a = [5, 3, 8, 1, 6, 8]
    insertion_sort(a)
    print(a)
