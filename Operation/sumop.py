from Operation.operation import Operation

class SumOp (Operation):
	@staticmethod
	def doop (elem, length): return elem * length
	def __init__ (self, length, min_value, max_value):
		self.s = 0
		Operation.__init__ (self, length,
			#length * min_value, length * max_value)
			SumOp.doop (min_value, length), SumOp.doop (max_value, length))
	def update (self, elem):
		Operation.update (self, elem)
		#Operation.update (self, elem * self.length)
		self.s += elem
	def finish (self):
		self.value = self.s
		Operation.finish (self)
	def cupdates (self, elem): return Operation.cupdates (self,
		#elem * self.length)
		SumOp.doop (elem, self.length))