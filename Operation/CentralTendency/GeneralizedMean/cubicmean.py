from Operation.CentralTendency.GeneralizedMean.generalizedmean \
import GeneralizedMean

class CubicMean (GeneralizedMean):
	def __init__ (self, length, min_value, max_value):
		GeneralizedMean.__init__ (self, length, min_value, max_value, 3)