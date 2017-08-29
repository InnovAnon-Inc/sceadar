from Operation.CentralTendency.centraltendency import CentralTendency

from Operation.minop import MinOp
from Operation.maxop import MaxOp

class MidRange (CentralTendency):
	def __init__ (self, length, min_value, max_value):
		self.minOp = MinOp (length, min_value, max_value)
		self.maxOp = MaxOp (length, min_value, max_value)
		self.mn = max_value
		self.mx = min_value
		CentralTendency.__init__ (self, length, min_value, max_value)
	def update (self, elem):
		CentralTendency.update (self, elem)
		if elem < self.mn: self.mn = elem
		if elem > self.mx: self.mx = elem
		self.minOp.update (elem)
		self.maxOp.update (elem)
	def finish (self):
		#self.value = self.mn + (self.mx - self.mn) / 2
		s = self.mx + self.mn
		if s % 2 is 0: self.value = s / 2
		else: self.value = float (s) / 2.0
		self.minOp.finish ()
		self.maxOp.finish ()
		CentralTendency.finish (self)
	def validate (self):
		CentralTendency.validate (self)
		self.minOp.validate ()
		self.maxOp.validate ()
		if self.mn is not self.minOp.value: raise Exception (
			"min:%s is not minOp:%s" % (self.mn, self.minOp.value))
		if self.mx is not self.maxOp.value: raise Exception (
			"max:%s is not maxOp:%s" % (self.mx, self.maxOp.value))
		if self.mn > self.mx: raise Exception (
			"min:%s > max:%s" % (self.mn, self.mx))
	def cupdates (self, elem): return CentralTendency.cupdates (self, elem)