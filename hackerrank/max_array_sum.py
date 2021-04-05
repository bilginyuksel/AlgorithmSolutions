class MaxArraySum:

    def maxSum(self, arr):
        # non adjacent element count
        sums = [0 for _ in range(len(arr) + 2)]
        sums[0] = max(arr[0], 0)
        sums[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            sums[i] = max(sums[i-1], sums[i-2] + arr[i], sums[i-2])

        return sum(sums)

solution = MaxArraySum()
solution.maxSum([3, 7, 4, 6, 5])
solution.maxSum([2, 1, 5, 8, 4])
solution.maxSum([3, 5, -7, 8, 10])