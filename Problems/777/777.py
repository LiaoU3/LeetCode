class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        start_sequence = []
        for i, c in enumerate(start):
            if c != 'X':
                start_sequence.append((c, i))

        result_sequence = []
        for i, c in enumerate(result):
            if c != 'X':
                result_sequence.append((c, i))

        if len(start_sequence) != len(result_sequence):
            return False

        for i in range(len(start_sequence)):
            if start_sequence[i][0] != result_sequence[i][0]:
                return False
            if start_sequence[i][0] == "R" and start_sequence[i][1] > result_sequence[i][1]:
                return False
            elif start_sequence[i][0] == "L" and start_sequence[i][1] < result_sequence[i][1]:
                return False
        return True
