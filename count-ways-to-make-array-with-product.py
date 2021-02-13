# queries = [[2,6], [5,1], [73,660]]
# output= [4, 1, 50734910]
# each query is independent.
# [2,6]: There are 4 ways to fill an array of size 2 that multiply to 6
# [1,6], [2,3], [3,2], [6,1]
# [5,1]: There is 1 way to fill an array of size 5 that multiply to 1.
# [1,1,1,1,1]
# [73, 660]: There are 1050734917 ways to fill an narray of size 73 that multiply to 660. 1050734917 modulo 10^9 + 7 = 50734910


# 6 -- 2 [2] 
# 3 -- 3 [3] 
# [1,6]
class Solution:
    def findWays(self, query):
        length, number = query
        divisors = []
        for num in range(2, number):
            if number == 0: break
            while number>0 and number % num == 0:
                number //= num
                divisors.append(num)

        print(divisors)
        return 1

    def waysToFillArray(self, queries):
        res = []
        for query in queries:
            ways = self.findWays(query)
            res.append(ways)
        return res

queryCount = int(input())
queries = []
for _ in range(queryCount):
    length, number = map(int, input().split())
    queries.append([length, number])
    
solution = Solution()
solution.waysToFillArray(queries)


