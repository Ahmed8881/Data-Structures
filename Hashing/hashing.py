class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value  # Simplified (no collision handling here)

    def search(self, key):
        index = self.hash_function(key)
        return self.table[index]

hash_table = HashTable(10)
hash_table.insert("apple", 5)
print("Apple:", hash_table.search("apple"))

class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Siple hash function
    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:  # If a collision occurs
            index = (index + 1) % self.size  # Move to the next slot
            if index == original_index:  # Table is full
                print("Hash table is full!")
                return
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Return the value
            index = (index + 1) % self.size
            if index == original_index:  # We looped around and didn't find the key
                break
        return None

hash_table = LinearProbingHashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
print("Apple:", hash_table.search("apple"))
class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        i = 0
        while self.table[(index + i**2) % self.size] is not None:
            i += 1
            if i == self.size: 
                print("Hash table is full!")
                return
        self.table[(index + i**2) % self.size] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        i = 0
        while self.table[(index + i**2) % self.size] is not None:
            if self.table[(index + i**2) % self.size][0] == key:
                return self.table[(index + i**2) % self.size][1]
            i += 1
            if i == self.size:  # We looped around and didn't find the key
                break
        return None

hash_table = QuadraticProbingHashTable(10)
hash_table.insert("apple", 5)
print("Apple:", hash_table.search("apple"))
class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Primary hash function
    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    # Secondary hash function (must not return 0)
    def second_hash_function(self, key):
        return 7 - (sum(ord(char) for char in key) % 7)

    # Insert key-value pair using double hashing
    def insert(self, key, value):
        index = self.hash_function(key)
        step_size = self.second_hash_function(key)
        original_index = index
        while self.table[index] is not None:
            index = (index + step_size) % self.size
            if index == original_index:  # Table is full
                print("Hash table is full!")
                return
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        step_size = self.second_hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step_size) % self.size
            if index == original_index:  # We looped around and didn't find the key
                break
        return None

hash_table = DoubleHashingHashTable(10)
hash_table.insert("apple", 5)
print("Apple:", hash_table.search("apple"))
