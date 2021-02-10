def sansaAndXOr(arr):
    if len(arr) % 2 == 0:
        return 0
    result = arr[0]
    for i in range(2, len(arr), 2):
        result ^= arr[i]
    return result
    
test = int(input())
for _ in range(test):
    int(input())
    arr = list(map(int, input().split()))
    result = sansaAndXOr(arr)
    print(result)
