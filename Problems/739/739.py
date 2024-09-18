class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # it stores [temp, index]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, index = stack.pop()
                res[index] = i - index
            stack.append([temp, i])
        return res
