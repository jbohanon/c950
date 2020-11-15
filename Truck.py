from typing import Dict

from HashTable import HashTable
from Package import Package


class Truck:
    def __init__(self, truck_num, package_list=None, stops=None):
        self.truck_num = truck_num

        if package_list is None:
            self.package_list = HashTable()
        if stops is None:
            self.stops = []

    @staticmethod
    def load_trucks(packages: HashTable):
        truck_one = Truck(1)
        truck_two = Truck(2)
        truck_three = Truck(3)

        # Manually hold packa
        truck_three.package_list.put('9', packages.get('9'))
        zips = {}
        for k in packages:
            v = packages[k]
            z = v.addr.zipcode
            if v.truck == '2':
                truck_two.package_list.put(k, v)
            if not zips.get(z):
                zips[z] = []
            zips[z].append(v)
        truck_one.package_list = zip(zips['84115'], zips['84119'])
