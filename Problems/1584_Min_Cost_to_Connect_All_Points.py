class Solution:
    def minCostConnectPoints(self, points) -> int:
        kruskal = Kruskal(points)
        kruskal.create_graph()
        return kruskal.go()

class Kruskal():
    def __init__(self, points):
        self.points = points
        self.graph = []
        self.n = len(points)
        self.roots = [i for i in range(self.n)]

    def create_graph(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                self.graph.append([i, j, self.manhattan_distance(self.points[i], self.points[j])])
        self.graph.sort(key = lambda point : point[2])
        
    def manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    
    def go(self):
        cnt = 0
        index = 0
        total_distance = 0
        while cnt < self.n-1:
            point1 = self.graph[index][0]
            point2 = self.graph[index][1]
            if self.roots[point1] != self.roots[point2]:
                point2_temp = self.roots[point2]
                for i in range(self.n):
                    if self.roots[i] == point2_temp:
                        self.roots[i] = self.roots[point1]
                total_distance += self.graph[index][2]
                cnt += 1
            index += 1
        return total_distance

def main():
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    # points = [[3,12],[-2,5],[-4,1]]
    s = Solution()
    print(s.minCostConnectPoints(points))

if __name__ == '__main__':
    main()