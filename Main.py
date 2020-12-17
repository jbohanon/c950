# Name: Jacob Bohanon
# Student ID: 001091919
from DataCache import DataCache
from Truck import Truck


dc = DataCache()

tr_1, tr_2, tr_3, tr_4 = Truck.load_trucks(dc)

tr_1.sort_truck(dc.distances)

print()
