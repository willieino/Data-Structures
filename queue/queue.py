class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    self.size += 1
    
  
  def dequeue(self):
    if self.size > 0:
      self.storage.pop()
      self.size -= 1

  def len(self):
    i = 0
    while i < self.size:
      i += 1
    return i