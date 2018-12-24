class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []
        solution = []
        start = 0
        self.dfs(candidates, target, solution, res, start)
        return res


    def dfs(self, candidates, target, solution, res, start):
        if target == 0:
            res.append(solution[:])
            return
        elif target < 0:
            return

        for i in range(start, len(candidates)):
            if target < candidates[i]:
                continue
            solution.append(candidates[i])
            self.dfs(candidates, target - candidates[i], solution, res, i)
            solution.pop()


if __name__ == "__main__":
    temp = Solution()
    candidates = [2,2,3,6,8,7]
    target = 7
    res = temp.combinationSum(candidates, target)
