from Util.util import Util

from Operations.operations import Operations

class AbsoluteDifference (Operations):
	@staticmethod
	def sop (value1, value2): return abs (value1 - value2)
	def __init__ (self,
		min_value1, max_value1,
		min_value2, max_value2):
		
		extrema = [
			AbsoluteDifference.sop (min_value1, max_value2),
			AbsoluteDifference.sop (max_value1, min_value2)]
		if Util.rangeIntersection (
			min_value1, max_value1,
			min_value2, max_value2) in [3, 4, 5, 6]:
			extrema.append (0)
		min_value = min (extrema)
		max_value = max (extrema)

		Operations.__init__ (self, min_value, max_value,
			(min_value1, max_value1),
			(min_value2, max_value2))
	def op (self, value1, value2):
		Operations.op (self, value1, value2)
		ret = AbsoluteDifference.sop (value1, value2)
		self.validateOp (ret)
		return ret