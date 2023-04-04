class UndergroundSystem:

    def __init__(self):
        self.checkedinstore = {}
        self.timeStore = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedinstore[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time_diff = t - self.checkedinstore[id][1]
        self.timeStore[(self.checkedinstore[id][0], stationName)].append(time_diff)

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        average = sum(self.timeStore[(startStation, endStation)])/ len((self.timeStore[(startStation, endStation)]))

        return average


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)