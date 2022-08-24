class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        def boom(num):
            # will explode
            if stack and stack[-1] > 0 and num < 0:
                if stack[-1] == -num:
                    stack.pop()
                elif stack[-1] < -num:
                    stack.pop()
                    boom(num)
            else:
                stack.append(num)

        for num in asteroids:
            boom(num)

        return stack