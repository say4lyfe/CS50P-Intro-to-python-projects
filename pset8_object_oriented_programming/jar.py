class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity <= 0:
            raise ValueError("invalid")
        self._capacity = capacity
        self._size = size
        

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size = self.size + n
            return self.size 
        else:
            raise ValueError("invalid")
        
    def withdraw(self, n):
        if self.size - n >= 0:
            self.size = self.size - n
            return self.size
        else:
            raise ValueError("invalid")

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity > self.capacity:
            raise ValueError("invalid")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("invalid")
        self._size = size
    