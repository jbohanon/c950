# Name: Jacob Bohanon
# Student ID: 001091919
import datetime

from DataCache import DataCache
from Truck import Truck


dc = DataCache()

tr_1, tr_2, tr_3, tr_4 = Truck.load_trucks(dc)

tr_1, tr_1_miles = tr_1.sort_truck()
tr_2, tr_2_miles = tr_2.sort_truck()
tr_3, tr_3_miles = tr_3.sort_truck(datetime.time(9, 5, 0))
tr_4, tr_4_miles = tr_4.sort_truck(datetime.time(10, 20, 0))

miles = tr_1_miles + tr_2_miles + tr_3_miles + tr_4_miles

tr_1.print()
tr_2.print()
tr_3.print()
tr_4.print()

print(miles)
