class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity


  def append(self, item):

    if self.capacity == self.current:
      self.current = 0
    
    self.storage[self.current] = item
    self.current += 1


  def get(self):
    res = []
    
    for i in self.storage:
      if i:
        res.append(i)

    return res
