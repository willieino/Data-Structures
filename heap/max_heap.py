class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    parent = index // 2
	  if index <= 1:
		  return
		elif self.heap[index] > self.heap[parent]:
			self.__swap(index, parent)
      self._bubble_up(parent)

  def _sift_down(self, index):
    pass

  def __swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
