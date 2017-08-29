class Operations:
	def __init__ (self, min_value, max_value,
		*params):
		#length1, min_value1, max_value1,
		#length2, min_value2, max_value2):
		#lengths, min_values, max_values = map (list, zip (*params))
		min_values, max_values = map (list, zip (*params))
		#lengths, min_values, max_values = zip (*params)
		#assert isinstance (lengths, list)
		assert isinstance (min_values, list)
		assert isinstance (max_values, list)
		if min_value  > max_value:  raise Exception (
			"min:%s > max:%s" % (min_value, max_value))
		#if min_value1 > max_value1: raise Exception (
		#	"min1:%s > max1: %s" % (min_value1, max_value1))
		#if min_value2 > max_value2: raise Exception (
		#	"min2: %s > max2: %s" % (min_value2, max_value2))
		for mn, mx in zip (min_values, max_values):
			if mn > mx: raise Exception (
				"min:%s > max: %s" % (mn, mx))
		#if length1 is not length2: raise Exception (
		#	"length1:%s is not length2:%s" % (length1, length2))
		#length0 = lengths[0]
		#if filter (lambda l: length0 is not l, lengths[1:]):
		#	raise Exception (
		#		"length0:%s is not l:%s" % (length0, l))
		self.min_value  = min_value
		self.max_value  = max_value
		#self.min_value1 = min_value1
		#self.max_value1 = max_value1
		#self.min_value2 = min_value2
		#self.max_value2 = max_value2
		#self.length = length1
		#self.length = length0
		self.min_values = min_values
		self.max_values = max_values
		#self.cnt = 0
	#def op (self, value1, value2):
	def op (self, *values):
		for value, mn, mx in zip (values, self.min_values, self.max_values):
		#for value in values:
			#if filter (lambda mn: value < mn, self.min_values):
			#for mn in self.min_values:
			if value < mn:
				raise Exception (
					"value:%s < mins:%s" % (
						value, mn))
			#if filter (lambda mx: value > mx, self.max_values):
			#for mx in self.max_values:
			if value > mx:
				raise Exception (
					"value:%s < maxes:%s" % (value, mx))
		#if value1 < self.min_value1: raise Exception (
		#	"value1:%s < min1:%s" % (value1, self.min_value1))
		#if value1 > self.max_value1: raise Exception (
		#	"value1:%s > max1:%s" % (value1, self.max_value1))
		#if value2 < self.min_value2: raise Exception (
		#	"value2:%s < min2:%s" % (value2, self.min_value2))
		#if value2 > self.max_value2: raise Exception (
		#	"value2:%s > max2:%s" % (value2, self.max_value2))
		#if self.cnt is self.length: raise Exception (
		#	"cnt:%s is length" % self.cnt)
		#self.cnt += 1
	def validateOp (self, value):
		if value < self.min_value: raise Exception (
			"value:%s < min:%s" % (value, self.min_value))
		if value > self.max_value: raise Exception (
			"value:%s > max:%s" % (value, self.max_value))