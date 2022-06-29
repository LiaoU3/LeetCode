from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        queue = [[-1, -1] for _ in range(len(people))]
        for man in people:
            height, infront = man
            cnt = 0
            for i, el in enumerate(queue):
                if cnt == infront and el[0]==-1:
                    queue[i] = man
                    break
                if el[0]==-1 or el[0]==height:
                    cnt += 1   
        return queue

if __name__ == '__main__':
    sol = Solution()
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(sol.reconstructQueue(people))