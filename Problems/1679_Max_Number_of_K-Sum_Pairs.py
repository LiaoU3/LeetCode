class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = 0
        un_paired = {}

        for num in nums:
            # add this line will make it faster cause there is no negative number in nums
            if num < k:
                if k - num in un_paired and un_paired[k - num]:
                    un_paired[k - num] -= 1
                    count += 1
                else:
                    un_paired[num] = un_paired.get(num, 0) + 1
        return count

def main():
    nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
    k = 3
    solution = Solution()
    print(solution.maxOperations(nums, k))

if __name__ == '__main__':
    main()