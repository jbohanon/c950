import unittest

from Address import Address
from HashTable import HashTable
from Package import Package


class HashTableTestCase(unittest.TestCase):
    def test_put(self):
        ht = HashTable()
        for i in range(1, 1001):
            ht.put(i, Package(i, Address.test_addr(), "test", "test", "test"))
        ht.put(200, Package(200, Address.test_addr(), "test2", "test2", "test2"))
        self.assertEqual(ht.get(200).deadline, "test2")


if __name__ == '__main__':
    unittest.main()
