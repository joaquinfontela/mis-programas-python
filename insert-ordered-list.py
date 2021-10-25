def insert_elem_in_sorted_array(elem, arr):
    n = len(arr)
    if not n or elem > arr[n-1]:
        arr.append(elem)
        return arr
    if elem < arr[0]:
        arr.insert(0, elem)
        return arr
    st = 0
    end = n-1
    i = (end - st) // 2
    tried_end_equals_i = False
    while not (elem >= arr[i-1] and elem <= arr[i]):
        if elem < arr[i-1]:
            end = i
            i = (end - st) // 2 + st
        else:
            st = i
            i = (end - st) // 2 + st
        if st == i and not tried_end_equals_i:
            i = end
            tried_end_equals_i = True
    arr.insert(i, elem)
    return arr
    