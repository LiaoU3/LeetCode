class Solution:
    def __init__(self):
        self.mark = None
        self.graph = None
    def isBipartite(self, graph) -> bool:
        n = len(graph)
        self.graph = graph
        self.mark = [None for _ in range(n)]
        self.mark[0] = True
        # return self.classify(self.mark[0], graph[0])

        cnt_total = 0

        ret, cnt = self.classify(self.mark[0], graph[0])
        cnt_total += cnt
        if not ret or cnt_total != 2:
            return False

        for i in range(1, n):
            if self.mark[i] is None:
                ret, cnt = self.classify(self.mark[i], graph[i])
                cnt_total += cnt
                if not ret or cnt_total != 2:
                    return False
        else:
            return True
    def classify(self, curr_mark, links):
        cnt = 1
        for link in links:
            if self.mark[link] is None:
                cnt = 2
                self.mark[link] = not curr_mark
                self.classify(not curr_mark, self.graph[link])
            elif self.mark[link] == curr_mark:
                return False, cnt
            else:
                continue
        return True, cnt

solution = Solution()
# graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[4],[],[4],[4],[0,2,3]]
print(solution.isBipartite(graph))