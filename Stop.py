import datetime

from Address import Address
from DataCache import DataCache


class Stop:
    def __init__(self, num: int, time: datetime.time, addr: Address, dc: DataCache):
        self.dc = dc
        self.num = num
        self.time = time
        self.addr = addr

    @staticmethod
    def hub(dc: DataCache, time: datetime.time = datetime.time(8, 0, 0)):
        return Stop(0, time, dc.locations["4001 South 700 East"], dc)

    # Per comments below, core_routing_algoritm runs in O(n)
    def core_routing_algorithm(self, truck_addrs: list):
        local_truck_addrs = []

        # Making a list of unique addresses will run in sublinear space and time for any n > 16
        # since 16 is the maximum number of addresses that could be found on a truck
        for item in truck_addrs:
            local_truck_addrs.append(self.dc.locations[item.addr])

        stop_dict = {self.num: self}
        base_stop_num = self.num
        total = 0.0

        # Because len(truck_addrs) is <= 16 per the stated 16 package/truck max,
        # this loop will always run at most 16 times, and will not scale with n.
        # Therefore, 16 * O(n) = O(n)
        for i in range(1, len(truck_addrs) + 1):
            # dict.get should run in constant time https://wiki.python.org/moin/TimeComplexity#dict
            st = stop_dict.get(i-1)
            # Stop.greedy_next() runs in O(n) time and space as shown in comments below
            greedy_next_stop, dist = st.greedy_next(local_truck_addrs)
            stop_dict[base_stop_num + i] = greedy_next_stop
            # list.remove runs in linear time https://wiki.python.org/moin/TimeComplexity#list
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

    # For the reasons given in comments below, greedy_next runs in O(n) time and space
    def greedy_next(self, truck_addrs: list):

        list_of_string_addresses_on_truck = []
        # For datasets where n > 16, this aggregation loop will always run per-truck at a sub-n rate
        # Therefore, it will not contribute appreciably to the space or time complexity
        for item in truck_addrs:
            list_of_string_addresses_on_truck.append(item.addr)

        # self.addr.distances is already sorted ascending by distance
        # Because distances is equal to n and every operation is in constant time,
        # This loop runs in O(n) time and space
        for tuple_of_address_distances in self.addr.distances:
            current_checking_address = tuple_of_address_distances[0]
            current_checking_distance = tuple_of_address_distances[1]
            # while x in s is an O(n) operation, len(list_of_string_addresses_on_truck) and therefore n here <= 16
            # So this x in s is insignificant for input of meaningful size
            if current_checking_address in list_of_string_addresses_on_truck:
                num = self.num + 1
                # Stop.add_time is a O(1) operation
                stop_time = Stop.add_time(self.time, current_checking_distance)
                stop_addr = self.dc.locations[current_checking_address]
                return Stop(num, stop_time, stop_addr, self.dc), current_checking_distance
