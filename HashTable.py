class HashTable:
    def __init__(self):
        """Creates an empty array with 1000 values"""
        self.table = [None] * 1000

    def store(self, string):
        self.table[calculate_hash_value(string)] = string

    def lookup(self, string):
        return self.table[calculate_hash_value(string))]if self.table[calculate_hash_value(string)] is not null
        else -1

    def calculate_hash_value(string):
        """Calculates the hash value from the string"""
        return ord(string[0]) * 100 + ord(string[1]


