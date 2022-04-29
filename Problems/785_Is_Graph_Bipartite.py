class Solution:
    def __init__(self):
        self.mark = None
        self.graph = None
        self.flag = True
    def isBipartite(self, graph) -> bool:
        n = len(graph)
        self.graph = graph
        self.mark = [None for _ in range(n)]
        self.mark[0] = True

        for i in range(n):
            if self.mark[i] is None:
                self.mark[i] = True
            self.classify(self.mark[i], graph[i])

        return self.flag
    def classify(self, curr_mark, links):
        for link in links:
            if self.flag == False:
                return
            if self.mark[link] is None:
                self.mark[link] = not curr_mark
                self.classify(not curr_mark, self.graph[link])
            elif self.mark[link] == curr_mark:
                self.flag = False
            else:
                continue

solution = Solution()
# graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# graph = [[4],[],[4],[4],[0,2,3]]
# graph = [[1],[0,3],[3],[1,2]]
# graph =[[3],[2,4],[1],[0,4],[1,3]]
# graph = [[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]
graph = [[1,3],[0,2],[1,3],[0,2]]
print(solution.isBipartite(graph))