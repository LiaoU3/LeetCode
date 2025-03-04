# O(n ** 2 * log(n))
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        hash_map = defaultdict(list)
        for i in range(len(points)):
            for j in range(i, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                hash_map[i].append((d, j))
                hash_map[j].append((d, i))

        seen = set()
        res = 0
        hp = [(0, 0)]  # distance, point
        while len(seen) < len(points):
            d, p = heappop(hp)
            if p in seen:
                continue
            seen.add(p)
            res += d
            for d2, p2 in hash_map[p]:
                if p2 in seen:
                    continue
                heappush(hp, (d2, p2))

        return res

# O(n ** 2 * log(n))
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        rank = [1] * len(points)
        parent = [i for i in range(len(points))]

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            parent[p2] = p1
            rank[p1] += rank[p2]
            return True
        
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(edges, (d, i, j))
        
        res = 0
        cnt = 0
        while edges and cnt < len(points) - 1:
            d, i, j = heappop(edges)
            if union(i, j):
                res += d
                cnt += 1
        return res



def main():
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    # points = [[3,12],[-2,5],[-4,1]]
    s = Solution()
    print(s.minCostConnectPoints(points))

if __name__ == '__main__':
    main()