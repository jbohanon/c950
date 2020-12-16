import datetime

from HashTable import HashTable
from Package import Package


class TruckManager:
    def __init__(self):
        self.dc = dc
    
    class Truck:
    
        mph = 18
    
        def __init__(self, truck_num, package_dict=None, stops=None):
            self.truck_num = truck_num
            self.package_addr_list = []
    
            if package_dict is None:
                self.package_dict = {}
            else:
                self.package_dict = package_dict
            if stops is None:
                self.stops = []
            else:
                self.stops = stops
    
        # Sort truck algorithm, taking dictionary of distance dictionaries for each address and truck depart time
        def sort_truck(self, distances: {}, origin_time=datetime.time(8, 0, 0)):
            # Copy of stops list for local use
            stops = self.stops
    
            # Declare hub as origin of route
            latest_stop = TruckManager.Stop.hub(origin_time)
    
            # Copy of truck's package dict for local use
            pkgs = self.package_dict
    
            # Create list of addresses on truck
            for i in pkgs:
                pkg: Package = pkgs[i]
                if not self.package_addr_list.__contains__(pkg.addr.addr):
                    self.package_addr_list.append(pkg.addr.addr)
    
            # cycle through finding shortest distance from latest_stop 3 times (greedy-3)
            # Choose shortest sum of greedy-3
            for i in pkgs:
                pkg: Package = pkgs[i]
                pkg_dists = pkg.addr.distances
                pkg_truck_dists = []
                for tup in pkg_dists:
                    if self.package_addr_list.__contains__(tup[0]) and not tup[0] == pkg.addr.addr:
                        pkg_truck_dists.append(tup)
    
            return TruckManager.Truck(self.truck_num, self.package_dict, stops)
        
        @classmethod
        def greedy_3(cls, stop, truck_pkgs, depth):
            stop_addr = stop.addr
    
        @staticmethod
        def intersect_dist_tuples(truck_package_list: {}, addr_distances_list: [()]):
            truck_distances_list = []
            for i in truck_package_list:
                truck_distances_list.append((i, truck_package_list[i]))
    
            return set(addr_distances_list).intersection(set(truck_distances_list))
    
    
        @staticmethod
        def load_trucks(packages: HashTable):
            # WGUPS only has (3) physical trucks and (2) drivers.
            # These trucks represent sequencing for drivers to get in trucks, not the physical trucks themselves
            truck_one = TruckManager.Truck.load_truck_one(packages)
            truck_two = TruckManager.Truck.load_truck_two(packages)
            truck_three = TruckManager.Truck.load_truck_three(packages)
            truck_four = TruckManager.Truck.load_truck_four(packages)
    
            # Truck 1: 11 packages
            # Truck 2: 12 packages
            # Truck 3: 11 packages
            # Truck 4: 6 packages
    
            return truck_one, truck_two, truck_three, truck_four
    
        @staticmethod
        def load_truck_one(packages: HashTable):
            truck_one = TruckManager.Truck(1)
            # Put remainder of MED priority packages on truck 1
            truck_one.package_dict[1] = packages.get(1)
            # Send 7 with 29 #
            truck_one.package_dict[29] = packages.get(29)
            truck_one.package_dict[7] = packages.get(7)
            ##################
            # Send 8 with 30 #
            truck_one.package_dict[30] = packages.get(30)
            truck_one.package_dict[8] = packages.get(8)
            ##################
            truck_one.package_dict[31] = packages.get(31)
            truck_one.package_dict[34] = packages.get(34)
            # Send 5 with 37 #
            truck_one.package_dict[37] = packages.get(37)
            truck_one.package_dict[5] = packages.get(5)
            ##################
            # Send 4 with 40 #
            truck_one.package_dict[40] = packages.get(40)
            truck_one.package_dict[4] = packages.get(4)
            ##################
            return truck_one
    
        @staticmethod
        def load_truck_two(packages: HashTable):
            truck_two = TruckManager.Truck(2)
    
            # Packages that must go on truck 2
            truck_two.package_dict[3] = packages.get(3)
            truck_two.package_dict[18] = packages.get(18)
            truck_two.package_dict[36] = packages.get(36)
            truck_two.package_dict[38] = packages.get(38)
    
            # Put packages that must go together on truck 2
            # Send 39 with 13 #
            truck_two.package_dict[13] = packages.get(13)
            truck_two.package_dict[39] = packages.get(39)
            ###################
            truck_two.package_dict[14] = packages.get(14)
            truck_two.package_dict[15] = packages.get(15)
            truck_two.package_dict[16] = packages.get(16)
            truck_two.package_dict[19] = packages.get(19)
            # Send 21 with 20 #
            truck_two.package_dict[20] = packages.get(20)
            truck_two.package_dict[21] = packages.get(21)
            ###################
    
            return truck_two
    
        @staticmethod
        def load_truck_three(packages: HashTable):
            truck_three = TruckManager.Truck(3)
    
            # Hold delayed packages for first truck to go out after 9:05 (truck 3)
            truck_three.package_dict[6] = packages.get(6)
            # Send 26 with 25 #
            truck_three.package_dict[25] = packages.get(25)
            truck_three.package_dict[26] = packages.get(26)
            ###################
            truck_three.package_dict[28] = packages.get(28)
            truck_three.package_dict[32] = packages.get(32)
            # Send 17 due to proximity to 6, 28/32
            truck_three.package_dict[17] = packages.get(17)
            # Send 11, 12, 22, 23, 24 due to route proximity
            truck_three.package_dict[11] = packages.get(11)
            truck_three.package_dict[12] = packages.get(12)
            truck_three.package_dict[22] = packages.get(22)
            truck_three.package_dict[23] = packages.get(23)
            truck_three.package_dict[24] = packages.get(24)
    
            return truck_three
    
        @staticmethod
        def load_truck_four(packages: HashTable):
            truck_four = TruckManager.Truck(4)
    
            # Some delayed packages above must be delivered by 10:30
            # Package 9 is not corrected until 10:20
            # Hold package 9 with wrong address for first truck to leave after 10:20 (truck 4)
            pkg_9: Package = packages.get(9)
            packages.put(9, pkg_9.with_address('410 S State St'))
    
            truck_four.package_dict[9] = packages.get(9)
            # Send 10 due to proximity to 9
            truck_four.package_dict[10] = packages.get(10)
            # Send 27/35 due to proximity to 9
            truck_four.package_dict[27] = packages.get(27)
            truck_four.package_dict[35] = packages.get(35)
            # Send 2 & 33 due to route proximity to 9
            truck_four.package_dict[2] = packages.get(2)
            truck_four.package_dict[33] = packages.get(33)
    
            return truck_four
