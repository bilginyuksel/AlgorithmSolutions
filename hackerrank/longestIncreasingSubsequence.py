def longestIncreasingSubsequence(arr):
    sequence = [0 for _ in range(len(arr))]
    sequence[0] = 1

    for i in range(1, len(arr)):
        currentValue = arr[i]
        for j in range(i+1, -1, -1):
            if currentValue > arr[j]:
                sequence[i] = max(sequence[i], sequence[j] + 1)
            else:
                sequence[i] = max(sequence[i], 1)

    return max(sequence)


