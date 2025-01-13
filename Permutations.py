class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length=len(nums)
        results=[]
        current_sol=[]
        def backtracking():
            if len(current_sol)==length:
                results.append(current_sol[:])
                return
            for num in nums:
                if num not in current_sol:
                    current_sol.append(num)
                    backtracking()
                    current_sol.pop()
        backtracking()
        return results