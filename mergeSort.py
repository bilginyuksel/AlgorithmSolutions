def merge(arr, left, right, inversionCount):
    i = j = k = 0
    while i < len(left) and j < len(right):
        currentTaken = None
        if left[i] <= right[j]:
            currentTaken = left[i]
            i += 1
        else:
            inversionCount[0] += 1
            print(left[i], right[j])
            currentTaken = right[j]
            j += 1
        arr[k] = currentTaken
        k+= 1
    
    while i < len(left):
        placedCount = (len(left) - i)
        arr[k] = left[i]
        inversionCount[0] += k - placedCount
        i += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1

    print(arr, left, right)

def mergeSort(arr, inversionCount):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    mergeSort(left, inversionCount)
    mergeSort(right, inversionCount)
    merge(arr, left, right, inversionCount)

def sort(arr):
    inversionCount = [0]
    mergeSort(arr, inversionCount)
    print('sortedArray= %s' % arr)
    return inversionCount[0]

res = sort([2, 3, 3, 1, 9, 5, 6])
print(res)
