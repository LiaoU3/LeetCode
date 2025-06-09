class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail2nameidx = defaultdict(list)
        for i, account in enumerate(accounts):
            for mail in account[1:]:
                mail2nameidx[mail].append(i)

        rank = [1] * len(accounts)
        parent = [i for i in range(len(accounts))]

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return True
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            parent[p2] = p1
            rank[p1] += rank[p2]
            return False

        for i, account in enumerate(accounts):
            for mail in account[1:]:
                for j in mail2nameidx[mail]:
                    union(i, j)

        grouped = defaultdict(list)
        for mail in mail2nameidx:
            root = find(mail2nameidx[mail][0])
            grouped[root].append(mail)

        res = []
        for root, mails in grouped.items():
            name = accounts[root][0]
            res.append([name] + sorted(mails))
        return res
