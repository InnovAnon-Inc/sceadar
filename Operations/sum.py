from Operations.operations import Operations

class Sum (Operations):
	@staticmethod
	def sop (value1, value2): return value1 + value2
	def __init__ (self,
		min_value1, max_value1,
		min_value2, max_value2):
		min_value = Sum.sop (min_value1, min_value2)
		max_value = Sum.sop (max_value1, max_value2)
		Operations.__init__ (self, min_value, max_value,
			(min_value1, max_value1),
			(min_value2, max_value2))
	def op (self, value1, value2):
		Operations.op (self, value1, value2)
		ret = Sum.sop (value1, value2)
		self.validateOp (ret)
		return ret