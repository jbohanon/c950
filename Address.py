

class Address:

    def with_city(self, city):
        return Address(self.name, self.addr, city, self.state, self.zipcode, self.distances)

    def __init__(self, name, addr, city, state, zipcode, distances):
        self.name = name
        self.addr = addr
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.distances = distances

    @staticmethod
    def test_addr():
        return Address("test", "test", "test", "test", "test", [])
