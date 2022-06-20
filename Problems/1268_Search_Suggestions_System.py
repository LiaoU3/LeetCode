from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        curr = products
        res = []
        for i, c in enumerate(searchWord):
            nxt = []
            for name in curr:
                if i<len(name) and c == name[i]:
                    nxt.append(name)
            res.append(nxt[:3])
            curr = nxt
        return res

if __name__ == '__main__':
    sol = Solution()
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    print(sol.suggestedProducts(products, searchWord))