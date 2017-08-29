from Util.util import Util

from Operations.operations import Operations

class DifferencePower (Operations):
	@staticmethod
	def sop (value1, value2, p=2):
		diff = value1 - value2
		if p % 2 is not 0: diff = abs (diff)
		return diff ** p
	def __init__ (self,
		min_value1, max_value1,
		min_value2, max_value2, p=2):
		if p is 0: raise Exception (
			"p:%s is 0" % p)
		
		extrema = [
			DifferencePower.sop (min_value1, max_value2, p),
			DifferencePower.sop (max_value1, min_value2, p)]
		if Util.rangeIntersection (
			min_value1, max_value1,
			min_value2, max_value2) in [3, 4, 5, 6]:
			extrema.append (0)
		min_value = min (extrema)
		max_value = max (extrema)
		
		self.p = p

		Operations.__init__ (self, min_value, max_value,
			(min_value1, max_value1),
			(min_value2, max_value2))
	def op (self, value1, value2):
		Operations.op (self, value1, value2)
		ret = DifferencePower.sop (value1, value2, self.p)
		self.validateOp (ret)
		return ret