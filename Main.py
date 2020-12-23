# Name: Jacob Bohanon
# Student ID: 001091919
import datetime

import UI
from DataCache import DataCache
from Truck import Truck


dc = DataCache()

dc.trucks[1], dc.trucks[2], dc.trucks[3], dc.trucks[4] = Truck.load_trucks(dc)

dc.trucks[1], tr_1_miles = dc.trucks[1].sort_truck()
dc.trucks[2], tr_2_miles = dc.trucks[2].sort_truck()
dc.trucks[3], tr_3_miles = dc.trucks[3].sort_truck(max(min(dc.trucks[1].end_time, dc.trucks[2].end_time), datetime.time(9, 5)))
dc.trucks[4], tr_4_miles = dc.trucks[4].sort_truck(max(max(dc.trucks[1].end_time, dc.trucks[2].end_time), datetime.time(10, 20)))

miles = tr_1_miles + tr_2_miles + tr_3_miles + tr_4_miles

print("Routing complete; total distance traveled: " + str(int(miles)) + " miles")
for i in range(1, 5):
    print("Truck " + str(i) + ":")
    for n in range(len(dc.trucks[i].stops)):
        print(dc.trucks[i].stops[n].num, dc.trucks[i].stops[n].time, dc.trucks[i].stops[n].addr.addr)

UI.core_loop(dc)
