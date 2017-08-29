from Util.util import Util

from Operation.CentralTendency.centraltendency import CentralTendency

class GeneralizedMean (CentralTendency):
	@staticmethod
	def doop (elem, length, p=4):
		return (abs (elem) ** p) ** (1.0 / p)
	def __init__ (self, length, min_value, max_value, p=4):
		if p is 0: raise Exception ("p is 0")
		self.p = p
		self.s = 0
		self.s2 = 0
		
		#minp = (min_value ** p * length / length) ** (1.0 / p)
		#maxp = (max_value ** p * length / length) ** (1.0 / p)
		minp = GeneralizedMean.doop (min_value, length, p)
		maxp = GeneralizedMean.doop (max_value, length, p)
		lp = [minp, maxp]
		
		CentralTendency.__init__ (self, length,
			#length * min_value, length * max_value)
			min (lp), max (lp))
	def update (self, elem):
		CentralTendency.update (self, elem)
		tfe = abs (elem) ** self.p
		#CentralTendency.update (self, (tfe / float (self.length)) ** (1.0 / self.p))
		self.s += tfe # TODO verify correctness
		self.s2 += abs (elem) ** self.p / float (self.length)
	def finish (self):
		self.value = (self.s / float (self.length)) ** (1.0 / float (self.p))
		self.v2 = self.s2 ** (1.0 / float (self.p))
		CentralTendency.finish (self)
	def validate (self):
		CentralTendency.validate (self)
		if not Util.approxEqual (self.value, self.v2): raise Exception (
			"value:%s is not v2:%s" % (self.value, self.v2))
	def cupdates (self, elem): #return CentralTendency.cupdates (self,
		#(abs (elem) ** self.p / float (self.length)) ** (1.0 / self.p))
		return CentralTendency.cupdates (self,
			GeneralizedMean.doop (elem, self.length, self.p))