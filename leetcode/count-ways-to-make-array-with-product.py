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

from math import comb

class Solution:
    MOD = (10 ** 9) + 7
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

    def _find_ways(self, query):
        ways = 1
        length, number = query

        for prime in self.primes:
            current_prime_count = 0
            while number % prime == 0:
                number //= prime
                current_prime_count += 1
            ways *= comb(length - 1 + current_prime_count, current_prime_count)
        
        if number != 1:
            ways *= length
        
        return ways % self.MOD

    def waysToFillArray(self, queries):
        return [self._find_ways(query) for query in queries]

query_count = int(input())
queries = []
for _ in range(query_count):
    length, number = map(int, input().split())
    queries.append([length, number])
    
solution = Solution()
solution.waysToFillArray(queries)



