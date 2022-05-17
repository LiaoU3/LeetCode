from collections import defaultdict
from typing import List
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        def _find_roots(i):
            if roots[i] != i:
                roots[i] =  _find_roots(roots[i])
            return roots[i]

        roots = list(range(len(s)))
        for x, y in pairs:
            root0 = _find_roots(x)
            root1 = _find_roots(y)
            if root0 != root1 :
                roots[root1] = root0

        classify = defaultdict(list)
        
        for i, el in enumerate(roots):
            classify[_find_roots(el)].append(i)  

        res = list(s)
        for key in classify.keys():
            index_list = classify[key]
            string = [res[index] for index in index_list]
            string.sort()
            
            for i, c in zip(index_list, string):
                res[i] = c
        return ''.join(res)
def main():
    solution = Solution()
    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    # pairs = [[0,3],[1,2],[0,2]]
    print(solution.smallestStringWithSwaps(s, pairs))

if __name__ =='__main__':
    main()