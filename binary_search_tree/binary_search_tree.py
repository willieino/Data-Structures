class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value > value:
      #
      #elif value > self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

    elif value > self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target < self.value:
      if self.value is None:
        return False
      return self.left.contains(target)
    elif target > self.value:
      if self.value is None:
        return False
      return self.right.contains(target)
    else:
      return True
    
    ''' if (self.value == target):
    	return True
    elif self.value > target:
			if self.left:
			  return self.left.contains(target)
			else:
				return False
		else:
			if self.right:
				return self.right.contains(target)
			else:
        return False '''
   
   
   
 

  def get_max(self):
    if(self == None):
      return 
    res = self.value
    lres = get_max(self)
    rres = get_max(self.right)
    if (lres > res):
      res = lres
    if (rres > res):
      res = rres
    return res

  def for_each(self, cb):
    pass