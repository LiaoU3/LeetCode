# O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        max_freq = 0
        for num in hash_map:
            freq = hash_map[num]
            max_freq = max(max_freq, freq)
            buckets[freq].append(num)

        res = []
        for i in range(max_freq, -1, -1):
            if not buckets[i]:
                continue
            res.extend(buckets[i])
            if len(res) == k:
                break
        return res

#  O(n log(k))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1
        hp = []
        for num in hash_map:
            freq = hash_map[num]
            if len(hp) < k:
                heappush(hp, (freq, num))
            else:
                if hp[0][0] < freq:
                    heappop(hp)
                    heappush(hp, (freq, num))
        res = []
        for _ in range(k):
            res.append(heappop(hp)[1])
        return res

# O(n log(n))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        # O(n)
        for num in nums:
            freq[num] += 1
        
        # O(n log(n))
        hp = []
        for num in freq:
            heappush(hp, (-freq[num], num))
        
        # O(k log(n))
        res = []
        for _ in range(k):
            res.append(heappop(hp)[1])
        return res