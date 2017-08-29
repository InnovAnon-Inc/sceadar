# a self-validating operation over a non-decreasing range of values
# with specified number of samples in a client-specified order
class Operation:
	# length: number of samples
	# min: inclusive min of sample range
	# max: inclusive max of sample range
	def __init__ (self, length, min_value, max_value):
		if min_value > max_value: raise Exception (
			"min:%s > max:%s" % (min_value, max_value))
		if length < 0: raise Exception (
			"length:%s < 0" % length)
		self.length = length
		self.min_value = min_value
		self.max_value = max_value
		self.cnt = 0
		self.isFinished = False
	# abstract algorithm to perform an incremental operation
	# there are no guarantees about internal state or whatever:
	# self.value is un-init'd
	def update (self, elem):
		if self.isFinished: raise Exception (
			"isFinished:%s" % self.isFinished)
		elem = self.cupdates (elem)
		self.validate2 (elem)
		if self.cnt is self.length: raise Exception (
			"cnt:%s is length" % self.cnt)
		self.cnt += 1
	# abstract algorithm to finish computation
	# TODO joke about how the `nice -n +20` guy finishes last
	def finish (self):
		if self.isFinished: raise Exception (
			"isFinished:%s" % self.isFinished)
		self.isFinished = True
		self.validate ()
	# abstract algorithm to validate final result
	def validate (self):
		if not self.isFinished: raise Exception (
			"isFinished:%s" % self.isFinished)
		if self.cnt is not self.length: raise Exception (
			"cnt:%s is not length:%s" % (self.cnt, self.length))
		self.validate2 (self.value)
	# abstract algorithm to validate a result
	def validate2 (self, elem):
		if elem < self.min_value: raise Exception (
			"elem:%s < min:%s" % (elem, self.min_value))
		if elem > self.max_value: raise Exception (
			"elem:%s > max:%s" % (elem, self.max_value))
	# abstract algorithm to perform computation on a constant vector
	def cupdates (self, elem):
		self.validate2 (elem)
		return elem