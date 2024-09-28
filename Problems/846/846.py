from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hash_map = {}
        for num in hand:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num] += 1
        keys = list(hash_map)
        keys.sort()
        for key in keys:
            for _ in range(hash_map[key]):
                for i in range(groupSize):
                    if key + i not in hash_map:
                        return False
                    if hash_map[key + i] == 0:
                        return False
                    hash_map[key + i] -= 1
        return True


s = Solution()
hand = [1,1,2,2,3,3]
groupSize = 3
print(s.isNStraightHand(hand, groupSize))