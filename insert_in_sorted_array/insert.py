from numpy import insert


def insertInSortedArr(arr, el):
    n = len(arr)
    if not n:
        return [el]
    if n == 1:
        if el > arr[0]:
            return arr + [el]
        else:
            return [el] + arr
    if el >= arr[n//2 - 1] and el <= arr[n//2]:
        return arr[:n//2] + [el] + arr[n//2:]
    elif el < arr[n//2 - 1]:
        return insertInSortedArr(arr[:n//2], el) + arr[n//2:]
    else:
        return arr[:n//2] + insertInSortedArr(arr[n//2:], el)


if __name__ == '__main__':
    arr = insertInSortedArr(
        [-2, 5, 6, 11, 18, 33, 33, 39, 50, 111, 1543], 11151)
