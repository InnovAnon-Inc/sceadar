from Operation.operation import Operation

class Coder (Operations):
	@staticmethod
	def sop (value1, value2): return 2.0 / (1.0 / value1 + 1.0 / value2)
	def __init__ (self,
		length1, min_value1, max_value1):
		if 0 in xrange (min_value1, max_value1 + 1): raise Exception (
			"0 in [%s, %s]" % (min_value1, max_value1))
		if 0 in xrange (min_value2, max_value2 + 1): raise Exception (
			"0 in [%s, %s]" % (min_value2, max_value2))
		
		min_value = HarmonicDifference.sop (min_value1, min_value2)
		max_value = HarmonicDifference.sop (max_value1, max_value2)

		Operations.__init__ (self, min_value, max_value,
			(length1, min_value1, max_value1),
			(length2, min_value2, max_value2))
	def op (self, value1, value2):
		Operations.op (self, value1, value2)
		ret = HarmonicDifference.sop (value1, value2)
		self.validateOp (ret)
		return ret