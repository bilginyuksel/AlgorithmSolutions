from typing import ByteString


class Solution:

    def getSumSet(self, nums, i, currentSum, subset):
        if i >= len(nums):
            subset.add(currentSum)
            return None

        self.getSumSet(nums, i+1, currentSum+nums[i], subset)
        self.getSumSet(nums, i+1, currentSum, subset)

    def findClosestNumber(self, subset, elem, goal):
        leftIdx, rightIdx = 0, len(subset)-1
        closestDiff = float('inf')

        while leftIdx <= rightIdx:
            midIdx = (leftIdx + rightIdx) // 2
            potentialClosestNum = subset[midIdx]
            currentSum = elem + potentialClosestNum
            currentDiff = abs(goal - currentSum)
            closestDiff = min(closestDiff, currentDiff)

            if currentDiff == 0:
                return 0

            if currentSum > goal:
                rightIdx = midIdx - 1
            elif currentSum < goal:
                leftIdx = midIdx + 1

        return closestDiff

    def minAbsDifference(self, nums, goal):
        n = len(nums)
        leftSet, rightSet = set(), set()

        self.getSumSet(nums[:n//2], 0, 0, leftSet)
        self.getSumSet(nums[n//2:], 0, 0, rightSet)

        sortedRightSet = sorted(list(rightSet))
        minDiff = float('inf')
        for elem in leftSet:
            potentialMinDiff = self.findClosestNumber(
                sortedRightSet, elem, goal)
            minDiff = min(potentialMinDiff, minDiff)

        return minDiff

solve = Solution()
diff = solve.minAbsDifference([5, -7, 3, 5], 6)
print(diff)