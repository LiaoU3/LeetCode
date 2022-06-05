from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        decks = [[nums[0]]]
        for num in nums[1:]:
            for deck in decks:
                if num <= deck[-1]:
                    deck.append(num)
                    break
            else:
                decks.append([num])
                if len(decks) == 3:
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    nums = [6,7,1,2]
    print(sol.increasingTriplet(nums))