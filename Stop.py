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

    # def greedy_3(self, truck_addrs: list):
    #     local_truck_addrs = []
    #     for item in truck_addrs:
    #         local_truck_addrs.append(self.dc.locations[item.addr])
    #     stop_dict = {self.num: self}
    #     base_stop_num = self.num
    #     total = 0.0
    #     for i in range(1, 4):
    #         st = stop_dict.get(i-1)
    #         greedy_next_stop, dist = st.greedy_next(local_truck_addrs)
    #         stop_dict[base_stop_num + i] = greedy_next_stop
    #         local_truck_addrs.remove(greedy_next_stop.addr)
    #         total += dist
    #
    #     return stop_dict, total

    def greedy_stop_algorithm(self, truck_addrs: list):
        local_truck_addrs = []
        for item in truck_addrs:
            local_truck_addrs.append(self.dc.locations[item.addr])
        stop_dict = {self.num: self}
        base_stop_num = self.num
        total = 0.0
        for i in range(1, len(truck_addrs) + 1):
            st = stop_dict.get(i-1)
            greedy_next_stop, dist = st.greedy_next(local_truck_addrs)
            stop_dict[base_stop_num + i] = greedy_next_stop
            local_truck_addrs.remove(greedy_next_stop.addr)
            total += dist

        return stop_dict, total

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
        else:
            minutes += time_elapsed

        return datetime.time(int(hour), int(minutes))

    def greedy_next(self, truck_addrs: list):

        strs = []
        for item in truck_addrs:
            strs.append(item.addr)

        # cycle through finding shortest distance from latest_stop 3 times (greedy-3)
        # Choose shortest sum of greedy-3
        for tup in self.addr.distances:
            if tup[0] in strs:
                num = self.num + 1
                stop_time = Stop.add_time(self.time, tup[1])
                stop_addr = self.dc.locations[tup[0]]
                return Stop(num, stop_time, stop_addr, self.dc), tup[1]
