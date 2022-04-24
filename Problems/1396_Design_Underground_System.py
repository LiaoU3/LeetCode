class Info:
    def __init__(self, station_in: str, time_in: int) -> None:
        self.station_in = station_in
        self.time_in = time_in

class UndergroundSystem:

    def __init__(self):
        self.passenger = {}
        self.travel = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger[id] = Info(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        travel_time = t - self.passenger[id].time_in
        if self.passenger[id].station_in + "_to_" + stationName in self.travel:
            self.travel[self.passenger[id].station_in + "_to_" + stationName].append(travel_time)
        else:
            self.travel[self.passenger[id].station_in + "_to_" + stationName] = [travel_time]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.travel[startStation + "_to_" + endStation])/len(self.travel[startStation + "_to_" + endStation])