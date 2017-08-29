from Util.util import Util

from Operations.operations import Operations

class PopCount (Operations):
	@staticmethod
	def sop (value): return bin (value).count ("1")
	def __init__ (self, min_value1, max_value1):
		# TODO there's gotta be a more efficient way to do this
		l = map (PopCount.sop, xrange (min_value1, max_value1 + 1))
		min_value = min (l)
		max_value = max (l)

		Operations.__init__ (self, min_value, max_value,
			(min_value1, max_value1))
	def op (self, value1):
		Operations.op (self, value1)
		ret = PopCount.sop (value1)
		self.validateOp (ret)
		return ret