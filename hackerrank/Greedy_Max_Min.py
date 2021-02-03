def maxMin(k, arr):
    arr.sort()
    diff = float('inf')
    for i in range(0, len(arr)-k+1):
        if arr[i+k-1] - arr[i] < diff:
            diff = arr[i+k-1] - arr[i]
    return diff

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(maxMin(k, arr))
