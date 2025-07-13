class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        res = 0
        for player in players:
            while i != len(trainers):
                player -= trainers[i]
                i += 1
                if player <= 0:
                    res += 1
                    break
        return res


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        heapify(players)
        heapify(trainers)
        res = 0
        while players and trainers:
            player = heappop(players)
            while trainers:
                trainer = heappop(trainers)
                player -= trainer
                if player <= 0:
                    res += 1
                    break
        return res
