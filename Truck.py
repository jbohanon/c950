from typing import Dict

from Address import Address
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
    def load_trucks(packages: HashTable, locations: Dict[str, Address]):
        truck_one = Truck(1)
        truck_two = Truck(2)
        truck_three = Truck(3)

        # Packages that must go on truck 2
        truck_two.package_list.put('3', packages.get('3'))
        truck_two.package_list.put('18', packages.get('18'))
        truck_two.package_list.put('36', packages.get('36'))
        truck_two.package_list.put('38', packages.get('38'))

        # Hold delayed packages for last truck
        truck_three.package_list.put('6', packages.get('6'))
        truck_three.package_list.put('25', packages.get('25'))
        truck_three.package_list.put('28', packages.get('28'))
        truck_three.package_list.put('32', packages.get('32'))

        # Hold package with wrong address for last truck
        pkg_9: Package = packages.get('9')
        packages.put('9', pkg_9.with_address('410 S State St'))
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
