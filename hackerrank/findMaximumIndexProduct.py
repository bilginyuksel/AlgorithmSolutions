def findMaximumIndexProduct(arr):
    leftClosestNumbers = getClosestNumbers(arr, range(len(arr)))
    rightClosestNumbers = getClosestNumbers(arr, range(len(arr)-1, -1, -1))

    return max([left * right for left, right in zip(leftClosestNumbers, rightClosestNumbers)])

def getClosestNumbers(arr, forRange: range):
    closestNumbers = [0 for _ in range(len(arr))]
    stack = []

    for i in forRange:
        currentValue = arr[i]
        while len(stack) > 0 and arr[stack[-1]] <= currentValue:
            stack.pop()

        closestNumbers[i] = (stack[-1]+1) if len(stack) > 0 else 0
        stack.append(i)

    return closestNumbers

arrLength = int(input())
arr = list(map(int, input().split()))
product = findMaximumIndexProduct(arr)
print(product)