class UndergroundSystem:

    def __init__(self):
        # Maps user ID to (stationName, time)
        self.check_ins = {}
        # Maps (startStation, endStation) to [total_time, count]
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_ins:
            start_station, start_time = self.check_ins.pop(id)
            route = (start_station, stationName)
            duration = t - start_time
            
            # Update route statistics
            stats = self.routes.get(route, [0, 0])
            stats[0] += duration
            stats[1] += 1
            self.routes[route] = stats

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.routes[(startStation, endStation)]
        return total_time / count