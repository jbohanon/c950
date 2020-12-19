import datetime

from DataCache import DataCache
from HashTable import HashTable
from Package import Package
from Stop import Stop


class Truck:

    mph = 18

    def __init__(self, truck_num, dc: DataCache, package_dict=None, package_addr_list=None, stops=None):
        self.dc: DataCache = dc
        self.truck_num = truck_num

        if package_dict is None:
            self.package_dict = {}
        else:
            self.package_dict = package_dict

        if package_addr_list is None:
            self.package_addr_list = []
        else:
            self.package_addr_list = package_addr_list

        if stops is None:
            self.stops = []
        else:
            self.stops = stops

    def with_address_list(self):
        # Copy of truck's package dict for local use
        pkgs = self.package_dict

        addr_list = []

        # Create list of addresses (strings) on truck
        for i in pkgs:
            pkg: Package = pkgs[i]
            if self.dc.locations[pkg.addr.addr] not in addr_list:
                addr_list.append(self.dc.locations[pkg.addr.addr])

        return Truck(self.truck_num, self.dc, self.package_dict, addr_list)

    # Sort truck algorithm, taking dictionary of distance dictionaries for each address and truck depart time
    def sort_truck(self, distances: {}, origin_time=datetime.time(8, 0, 0)):
        # Copy of stops list for local use
        stops = self.stops

        # Declare hub as origin of route
        latest_stop = Stop.hub(self.dc, origin_time)

        next_addr = latest_stop.greedy_3(self.package_addr_list)
        print()

        return Truck(self.truck_num, self.package_dict, self.package_dict, self.package_addr_list, stops)

    @classmethod
    def greedy_3(cls, last_stop, truck_pkgs, depth=0):
        stop_addr = last_stop.addr.addr


    @staticmethod
    def intersect_dist_tuples(truck_package_list: {}, addr_distances_list: [()]):
        truck_distances_list = []
        for i in truck_package_list:
            truck_distances_list.append((i, truck_package_list[i]))

        return set(addr_distances_list).intersection(set(truck_distances_list))


    @staticmethod
    def load_trucks(dc: DataCache):
        # WGUPS only has (3) physical trucks and (2) drivers.
        # These trucks represent sequencing for drivers to get in trucks, not the physical trucks themselves
        truck_one = Truck.load_truck_one(dc)
        truck_two = Truck.load_truck_two(dc)
        truck_three = Truck.load_truck_three(dc)
        truck_four = Truck.load_truck_four(dc)

        # Truck 1: 11 packages
        # Truck 2: 12 packages
        # Truck 3: 11 packages
        # Truck 4: 6 packages

        return truck_one, truck_two, truck_three, truck_four

    @staticmethod
    def load_truck_one(dc: DataCache):
        truck_one = Truck(1, dc)
        # Put remainder of MED priority packages on truck 1
        truck_one.package_dict[1] = dc.packages.get(1)
        # Send 7 with 29 #
        truck_one.package_dict[29] = dc.packages.get(29)
        truck_one.package_dict[7] = dc.packages.get(7)
        ##################
        # Send 8 with 30 #
        truck_one.package_dict[30] = dc.packages.get(30)
        truck_one.package_dict[8] = dc.packages.get(8)
        ##################
        truck_one.package_dict[31] = dc.packages.get(31)
        truck_one.package_dict[34] = dc.packages.get(34)
        # Send 5 with 37 #
        truck_one.package_dict[37] = dc.packages.get(37)
        truck_one.package_dict[5] = dc.packages.get(5)
        ##################
        # Send 4 with 40 #
        truck_one.package_dict[40] = dc.packages.get(40)
        truck_one.package_dict[4] = dc.packages.get(4)
        ##################
        return truck_one.with_address_list()

    @staticmethod
    def load_truck_two(dc: DataCache):
        truck_two = Truck(2, dc)

        # Packages that must go on truck 2
        truck_two.package_dict[3] = dc.packages.get(3)
        truck_two.package_dict[18] = dc.packages.get(18)
        truck_two.package_dict[36] = dc.packages.get(36)
        truck_two.package_dict[38] = dc.packages.get(38)

        # Put packages that must go together on truck 2
        # Send 39 with 13 #
        truck_two.package_dict[13] = dc.packages.get(13)
        truck_two.package_dict[39] = dc.packages.get(39)
        ###################
        truck_two.package_dict[14] = dc.packages.get(14)
        truck_two.package_dict[15] = dc.packages.get(15)
        truck_two.package_dict[16] = dc.packages.get(16)
        truck_two.package_dict[19] = dc.packages.get(19)
        # Send 21 with 20 #
        truck_two.package_dict[20] = dc.packages.get(20)
        truck_two.package_dict[21] = dc.packages.get(21)
        ###################

        return truck_two.with_address_list()

    @staticmethod
    def load_truck_three(dc: DataCache):
        truck_three = Truck(3, dc)

        # Hold delayed packages for first truck to go out after 9:05 (truck 3)
        truck_three.package_dict[6] = dc.packages.get(6)
        # Send 26 with 25 #
        truck_three.package_dict[25] = dc.packages.get(25)
        truck_three.package_dict[26] = dc.packages.get(26)
        ###################
        truck_three.package_dict[28] = dc.packages.get(28)
        truck_three.package_dict[32] = dc.packages.get(32)
        # Send 17 due to proximity to 6, 28/32
        truck_three.package_dict[17] = dc.packages.get(17)
        # Send 11, 12, 22, 23, 24 due to route proximity
        truck_three.package_dict[11] = dc.packages.get(11)
        truck_three.package_dict[12] = dc.packages.get(12)
        truck_three.package_dict[22] = dc.packages.get(22)
        truck_three.package_dict[23] = dc.packages.get(23)
        truck_three.package_dict[24] = dc.packages.get(24)

        return truck_three.with_address_list()

    @staticmethod
    def load_truck_four(dc: DataCache):
        truck_four = Truck(4, dc)

        # Some delayed packages above must be delivered by 10:30
        # Package 9 is not corrected until 10:20
        # Hold package 9 with wrong address for first truck to leave after 10:20 (truck 4)
        pkg_9: Package = dc.packages.get(9)
        dc.packages.put(9, pkg_9.with_address(dc.locations['410 S State St']))

        truck_four.package_dict[9] = dc.packages.get(9)
        # Send 10 due to proximity to 9
        truck_four.package_dict[10] = dc.packages.get(10)
        # Send 27/35 due to proximity to 9
        truck_four.package_dict[27] = dc.packages.get(27)
        truck_four.package_dict[35] = dc.packages.get(35)
        # Send 2 & 33 due to route proximity to 9
        truck_four.package_dict[2] = dc.packages.get(2)
        truck_four.package_dict[33] = dc.packages.get(33)

        return truck_four.with_address_list()
