from typing import List

class Solution:
    def coinChange(self, nums: List[int], target: int) -> int:
        memo = {}  # used for memoization
        def dfs(remainder):
            if remainder in memo:  # already solved this problem?
                return memo[remainder]  # then return what we got last time
            if remainder<0:
                return None
            if remainder==0:
                return []
            shortest_combination=None
            for num in nums:
                result = dfs(remainder-num)
                if result!=None:
                    combination=[*result,num]
                    if shortest_combination==None or len(combination)<len(shortest_combination):
                        shortest_combination=combination
            memo[remainder] = shortest_combination  # memoize this solution
            return shortest_combination

        return -1 if dfs(target)==None else len(dfs(target))


s=Solution()
print(s.coinChange([162, 349, 35],1279))