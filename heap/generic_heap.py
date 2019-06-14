class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.last += 1             
    if value.last <= value.length:
      value.heap[value.last] = value
    else:
      value.length += 1           
      value.heap += [None]
      value.heap[value.last] = value
    value.bubble_up()

  def delete(self):
    pass

  def get_priority(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    while index > 0:
      parent = index - 1 / 2
      if self.storage[index] > self.storage[parent]:
        store = self.storage[index]

        self.storage[index] = self.storage[parent]
        self.storage[parent] = store
        index = parent
      else:
        break

  def _sift_down(self, index):
    pass
