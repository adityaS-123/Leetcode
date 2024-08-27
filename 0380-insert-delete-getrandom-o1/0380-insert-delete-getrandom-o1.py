import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}  # To store the value and its index in the list
        self.list = []  # To store the values

    def insert(self, val):
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        if val not in self.dict:
            return False
        # Get the index of the element to remove
        index = self.dict[val]
        # Swap the element with the last element in the list
        last_element = self.list[-1]
        self.list[index] = last_element
        self.dict[last_element] = index
        # Remove the last element from the list
        self.list.pop()
        # Remove the element from the dictionary
        del self.dict[val]
        return True

    def getRandom(self):
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
