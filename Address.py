

class Address:

    def with_city(self, city):
        return Address(self.name, self.addr, city, self.state, self.zipcode)

    def __init__(self, name, addr, city, state, zipcode):
        self.name = name
        self.addr = addr
        self.city = city
        self.state = state
        self.zipcode = zipcode
        # self.distances = [str, int] * 27

    @staticmethod
    def test_addr():
        return Address("test", "test", "test", "test", "test")
