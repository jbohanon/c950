import datetime

from Address import Address
from DataCache import DataCache
from Package import Package


class Stop:
    def __init__(self, num: int, time: datetime.time, addr: Address, dc: DataCache):
        self.dc = dc
        self.num = num
        self.time = time
        self.addr = addr

    @staticmethod
    def hub(dc: DataCache, time: datetime.time = datetime.time(8, 0, 0)):
        return Stop(0, time, dc.locations["4001 South 700 East"], dc)

    def greedy_3(self, truck_addrs):
        stop_list = [(self, self.num)]
        total = 0
        for i in range(1, 3):
            stop_list.append(stop_list[i-1][0].greedy_next(truck_addrs))
            # total += dist

        return stop_list, total


    @staticmethod
    def add_time(orig_time: datetime.time, dist):
        minutes = orig_time.minute
        hour = orig_time.hour
        # 18 miles / 60 min = dist miles / x min
        # x=(60*dist)/18
        time_elapsed = (dist*60)/18
        if minutes + time_elapsed > 60:
            hour += 1
            minutes = minutes + time_elapsed - 60

        return datetime.time(int(hour), int(minutes))

    def greedy_next(self, truck_addrs):

        # cycle through finding shortest distance from latest_stop 3 times (greedy-3)
        # Choose shortest sum of greedy-3
        # return (self.dc.locations[key] for key in self.addr.distances if key in truck_addrs)
        for tup in self.addr.distances:
            if self.dc.locations[tup[0]] in truck_addrs:
                return Stop(self.num+1, Stop.add_time(self.time, tup[1]),  self.dc.locations[tup[0]], self.dc), tup[1]
