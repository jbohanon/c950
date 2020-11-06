import math

class HashTable:
    def __init__(self):
        self.array = [None] * 50
        self.collision_safety = 3

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def contains_key(self):
        pass

    def _hash_func(self, key_seed):
        try:
            return (math.e ** key_seed) % len(self.array)
        except():
            print("key_seed not a number")
