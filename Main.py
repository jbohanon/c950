# Name: Jacob Bohanon
# Student ID: 001091919
from DataCache import DataCache
from Truck import TruckManager


dc = DataCache()
tm = TruckManager(dc)

tr_1, tr_2, tr_3, tr_4 = tm.Truck.load_trucks(dc.packages)

tr_1.sort_truck(dc.distances)

print()
