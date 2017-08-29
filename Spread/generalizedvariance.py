from Operation.operation import Operation

from Spread.spread import Spread

# (tm)
class GeneralizedVariance (Spread):
	# no CTargs or Diffargs... make a subtype or no soup for you
	def __init__ (self, length, min_value, max_value,
		CT, Diff, mean):
		#Transform (length, min_value, max_value,
		#lambda x: x - 1, lambda y: y - 1,
		#HarmonicMean)
		diff = Diff (
			min_value, max_value,
			mean,      mean)
		ct = CT (length, diff.min_value, diff.max_value)
		self.diff = diff
		self.ct = ct
		self.mean = mean
		Spread.__init__ (self, ct.length, ct.min_value, ct.max_value)
	def update (self, value):
		Spread.update (self, value)
		self.ct.update (self.diff.op (value, self.mean))
	def finish (self):
		self.ct.finish ()
		self.value = self.ct.value
		Spread.finish (self)
	def validate (self):
		Spread.validate (self)
		self.ct.validate ()
	def cupdates (self, elem): return Spread.cupdates (self,
		self.ct.cupdates (elem))