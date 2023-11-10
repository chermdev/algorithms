def insertionSort2(n, arr):
    arr = list(map(str, arr))
    for i in range(1, len(arr), 1):
        for j in range(i-1, -1, -1):
            if int(arr[i]) > int(arr[j]):
                arr.insert(j+1, arr.pop(i))
                print(' '.join(arr))
                break
            elif int(arr[i]) < int(arr[j]) and j == 0:
                arr.insert(j, arr.pop(i))
                print(' '.join(arr))


insertionSort2(7, [3, 4, 7, 5, 6, 2, 1])
