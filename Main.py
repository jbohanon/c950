from ReadCSV import init_distance_data, init_location_data, init_pkg_data
from Truck import Truck

distances = init_distance_data()
locations = init_location_data()
packages = init_pkg_data(locations)

Truck.load_trucks(packages)

print()
