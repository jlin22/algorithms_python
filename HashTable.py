class HashTable:
    def __init__(self):
        """Creates an empty array with 1000 values"""
        self.table = [None] * 10000

    def calculate_hash_value(self, string):
        """Calculates the hash value from the string"""
        return ord(string[0]) * 100 + ord(string[1])

    def store(self, string):
        """add the string to the hash table"""
        self.table[self.calculate_hash_value(string)] = [string]

    def lookup(self, string):
        """[] for dictionaries"""
        if self.table[self.calculate_hash_value(string)]:
            return self.calculate_hash_value(string)
        else:
            return -1

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))

