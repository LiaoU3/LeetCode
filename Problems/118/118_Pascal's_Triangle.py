from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            curr = [1]
            for j in range(len(ans[-1])-1):
                    curr.append(ans[-1][j] + ans[-1][j+1])
            curr.append(1)
            ans.append(curr)
        return ans
