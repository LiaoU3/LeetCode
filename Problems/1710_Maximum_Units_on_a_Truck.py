class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key= lambda x: x[1])
        unitCount = 0
        for box in boxTypes:
            if truckSize > box[0]:
                truckSize -= box[0]
                unitCount += box[0]*box[1]
            else:
                unitCount += truckSize*box[1]
                break
        return unitCount