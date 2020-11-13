import csv

from Package import Package


def init_pkg_data():

    pkg_list = list()

    r = csv.reader('res/packages.csv', ',')
    for row in r:
        pkg_list.append(Package(row[]))


def init_location_data():
