class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [float("Inf")] * len(books)
        dp[0] = books[0][1]

        for i in range(1, len(books)):
            width = 0
            height = 0
            for j in range(i, -1, -1):
                width += books[j][0]
                height = max(height, books[j][1])
                if width > shelfWidth:
                    break    
                if j == 0:
                    dp[i] = height
                else:
                    dp[i] = min(dp[i], dp[j - 1] + height)

        return dp[-1]
