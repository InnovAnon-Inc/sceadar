from Operation.operation import Operation

class MaxOp (Operation):
	def __init__ (self, length, min_value, max_value):
		self.mx = min_value
		Operation.__init__ (self, length,
			#max_value, max_value)
			min_value, max_value)
	def update (self, elem):
		Operation.update (self, elem)
		if elem > self.mx: self.mx = elem
	def finish (self):
		self.value = self.mx
		Operation.finish (self)
	def validate (self):
		Operation.validate (self)
		if self.value is not self.max_value: raise Exception (
			"value:%s is not max:%s" % (self.value, self.max_value))
	def cupdates (self, elem): return Operation.cupdates (self, elem)