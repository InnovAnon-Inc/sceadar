from Operation.operation import Operation

class MinOp (Operation):
	def __init__ (self, length, min_value, max_value):
		self.mn = max_value
		Operation.__init__ (self, length,
			#min_value, min_value)
			min_value, max_value)
	def update (self, elem):
		Operation.update (self, elem)
		if elem < self.mn: self.mn = elem
	def finish (self):
		self.value = self.mn
		Operation.finish (self)
	def validate (self):
		Operation.validate (self)
		if self.value is not self.min_value: raise Exception (
			"value:%s is not min:%s" % (self.value, self.min_value))
	def cupdates (self, elem): return Operation.cupdates (self, elem)