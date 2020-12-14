import csv

from typing import Dict

from Address import Address
from HashTable import HashTable
from Package import Package, Priority


def init_pkg_data(location_data: Dict[str, Address]):
    pkg_list = HashTable()

    with open('res/WGUPS_packages.csv') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            if row[5] == "9:00 AM":
                priority = Priority.HIGH
            elif row[5] == "10:30 AM":
                priority = Priority.MED
            else:
                priority = Priority.LOW

            pkg_list.put(int(row[0]),
                         Package(int(row[0]), location_data.get(row[1]).with_city(row[2]), priority, row[6], row[7],
                                 row[8], row[9]))

    return pkg_list


def init_location_data(distances: {}):
    locs = {}

    with open('res/WGUPS_locations.csv') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            row_dists = distances[row[1]]
            list_tuples_dists = []
            for key in row_dists:
                tup = (key, row_dists[key])
                list_tuples_dists.append(tup)
                def sort_func(tupl): return tupl[1]
                list_tuples_dists.sort(key=sort_func)
            locs[row[1]] = Address(row[0], row[1], None, "UT", row[2], list_tuples_dists)

    return locs


def init_distance_data():
    num_locations = 27
    distances = {}

    with open('res/WGUPS_distances.csv') as csvfile:
        r = csv.reader(csvfile)
        locs = ["" for i in range(num_locations + 1)]
        title_row = True

        for row in r:
            if title_row:
                title_row = False
                for i in range(1, (num_locations + 1)):
                    locs[i] = row[i]
                    distances[row[i]] = {}
                continue

            for i in range(1, (num_locations + 1)):
                distances[row[0]][locs[i]] = float(row[i])

    return distances
