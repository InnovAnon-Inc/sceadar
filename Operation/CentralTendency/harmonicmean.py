from Operation.CentralTendency.centraltendency import CentralTendency

class HarmonicMean (CentralTendency):
	def __init__ (self, length, min_value, max_value):
		self.s = 0
		if 0 in xrange (min_value, max_value + 1): raise Exception (
			"0 in [%s, %s]" % (min_value, max_value))
		CentralTendency.__init__ (self, length, min_value, max_value)
	def update (self, elem):
		CentralTendency.update (self, elem)
		tfe = 1.0 / float (elem)
		#CentralTendency.update (self, 1.0 / tfe)
		self.s += tfe
	def finish (self):
		self.value = float (self.length) / self.s
		CentralTendency.finish (self)
	def cupdates (self, elem): return CentralTendency.cupdates (self, elem)