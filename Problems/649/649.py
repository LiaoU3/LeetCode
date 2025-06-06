class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiants = deque()
        dires = deque()
        for i, c in enumerate(senate):
            if c == "R":
                radiants.append(i)
            else:
                dires.append(i)

        while radiants and dires:
            r_turn = radiants.popleft()
            d_turn = dires.popleft()
            if r_turn < d_turn:
                radiants.append(r_turn + len(senate))
            else:
                dires.append(d_turn + len(senate))

        return "Radiant" if radiants else "Dire"
