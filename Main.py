# Name: Jacob Bohanon
# Student ID: 001091919

from ReadCSV import init_distance_data, init_location_data, init_pkg_data
from Truck import Truck

distances = init_distance_data()
locations = init_location_data()
packages = init_pkg_data(locations)

tr_1, tr_2, tr_3, tr_4 = Truck.load_trucks(packages)

print()
