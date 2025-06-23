class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def is_mirror_10_base(num: int):
            mirror = 0
            curr = num
            while curr:
                mirror *= 10
                mirror += curr % 10
                curr //= 10
            return mirror == num

        def plus_one(nums):
            carry = True
            res = nums.copy()
            for i in range(len(res)):
                if not carry:
                    break
                res[i] += 1
                carry = True if res[i] == k else False
                res[i] %= k
            if carry:
                res.append(1)
            return res

        def mirror_odd(nums):
            return nums[::-1] + nums[1:]

        def mirror_even(nums):
            return nums[::-1] + nums

        def k_base_to_10_base(nums):
            curr = 0
            for i, num in enumerate(nums):
                curr += num * k ** i
            return curr

        res = 0
        digits = 1
        while n:
            base = [0] * (digits - 1) + [1]
            curr = base.copy()
            while len(curr) == len(base):
                nums = mirror_odd(curr)
                num = k_base_to_10_base(nums)
                if is_mirror_10_base(num):
                    res += num
                    n -= 1
                    if n == 0:
                        break
                curr = plus_one(curr)
            if n == 0:
                break
            base = [0] * (digits - 1) + [1]
            curr = base.copy()
            while len(curr) == len(base):
                nums = mirror_even(curr)
                num = k_base_to_10_base(nums)
                if is_mirror_10_base(num):
                    res += num
                    n -= 1
                    if n == 0:
                        break
                curr = plus_one(curr)

            digits += 1

        return res

# TLE
# class Solution:
#     def kMirror(self, k: int, n: int) -> int:

#         def is_mirror_k_base_list(nums):
#             l = 0
#             r = len(nums) - 1
#             while l < r:
#                 if nums[l] != nums[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True

#         def is_mirror_10_base(num: int):
#             mirror = 0
#             curr = num
#             while curr:
#                 mirror *= 10
#                 mirror += curr % 10
#                 curr //= 10
#             return mirror == num

#         def plus_one(nums):
#             carry = True
#             for i in range(len(nums)):
#                 if not carry:
#                     break
#                 nums[i] += 1
#                 carry = True if nums[i] == k else False
#                 nums[i] %= k
#             if carry:
#                 nums.append(1)


#         def k_base_to_10_base(nums):
#             curr = 0
#             for i, num in enumerate(nums):
#                 curr += num * k ** i
#             return curr

#         res = 0
#         curr = [1]

#         while n:
#             if is_mirror_k_base_list(curr):
#                 num = k_base_to_10_base(curr)
#                 if is_mirror_10_base(num):
#                     res += num
#                     n -= 1
#             plus_one(curr)

#         return res


k = 3
n = 7
sol = Solution()
print(sol.kMirror(k, n))
