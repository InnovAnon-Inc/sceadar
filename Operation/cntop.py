from Operation.operation import Operation

class CntOp (Operation):
	def __init__ (self, length, min_value, max_value):
		self.c = 0
		Operation.__init__ (self, length, length, length)
		#Operation.__init__ (self, length, 1, length)
	def update (self, elem):
		Operation.update (self, elem)
		#Operation.update (self, 1 * self.length)
		if self.c is self.length: raise Exception (
			"c:%s is length" % self.c)
		self.c += 1
	def finish (self):
		self.value = self.c
		Operation.finish (self)
	def validate (self):
		Operation.validate (self)
		if self.value is not self.length: raise Exception (
			"value:%s is not length:%s" % (self.value, self.length))
	def cupdates (self, elem): return Operation.cupdates (self, self.length)