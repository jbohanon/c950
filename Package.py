from enum import Enum
import Address


class Status(Enum):
    HUB = "At the Hub"
    ENROUTE = "En route"
    DELIVERED = "Delivered"


class Package:

    def with_status(self, status):
        return Package(self.pkgid, self.addr, self.deadline, self.weight, self.notes, status)

    def __init__(self, pkgid, addr: Address.Address, deadline, weight, notes, pairings=None, truck=-1, status=Status.HUB):
        self.pkgid = pkgid
        self.addr = addr
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.pairings = (list() if pairings is None else pairings)
        self.truck = truck
        self.status = status
        self.manual_load = (True if (notes != '' or pairings != '' or truck != '') else False)


