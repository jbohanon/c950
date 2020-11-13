import math

from Package import Package


class HashTable:
    def __init__(self):
        self.array = [list()] * 50
        self.collision_safety = 10

    def put(self, key, value):
        try:
            loc = self._hash_func(key)
            if len(self.array[loc]) > self.collision_safety:
                self.resize()
                loc = self._hash_func(key)
        except ValueError as ve:
            raise ve

        self.array[loc].append(value)

    def get(self, key):
        try:
            for item in self.array[self._hash_func(key)]:
                for pkg in item:
                    if pkg.pkgid == key:
                        return pkg
        except ValueError as ve:
            raise ve
        finally:
            raise ValueError("key not found")

    def contains_key(self, key):
        try:
            for item in self.array[self._hash_func(key)]:
                if item == key:
                    return True
        except():
            raise ValueError
        finally:
            return False

    def _hash_func(self, key_seed):
        try:
            return (math.e ** key_seed) % len(self.array)
        except():
            raise ValueError("key_seed not a number")

    def resize(self):
        tmp_arr = self.array
        self.array = [list()] * len(tmp_arr) * 2
        for location in tmp_arr:
            for item in location:
                p: Package = item
                self.put(p.pkgid, p)
