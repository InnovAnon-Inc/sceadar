from math import sqrt

from Operation.sumop  import SumOp
from Operation.cntop  import CntOp
from Operation.prodop import ProdOp

from Operation.CentralTendency.arithmeticmean import ArithmeticMean
from Operation.CentralTendency.geometricmean  import GeometricMean
from Operation.CentralTendency.harmonicmean   import HarmonicMean
from Operation.CentralTendency.trimean        import TriMean

from Operations.difference          import Difference
from Operations.sum                 import Sum
from Operations.absolutedifference  import AbsoluteDifference
from Operations.powerdifference     import PowerDifference
from Operations.geometricdifference import GeometricDifference
from Operations.harmonicdifference  import HarmonicDifference
from Operations.differencepower     import DifferencePower

from Operation.transform import Transform

from Spread.generalizedvariance import GeneralizedVariance
from Spread.stddevct import StdDevCT
from Spread.standarddeviation import StandardDeviation

from Operations.popcount import PopCount

if __name__ == '__main__':
	l1 = list (xrange (10))
	print len (l1)
	print min (l1)
	print max (l1)
	
	l2 = list (xrange (1, 11))
	print len (l2)
	print min (l2)
	print max (l2)
	
	diffops = Difference (
		min (l1), max (l1),
		min (l2), max (l2))
	print map (lambda (x, y): diffops.op (x, y), zip (l1, l2))
	
	
	sumop = SumOp (len (l1), min (l1), max (l1))
	cntop = CntOp (len (l1), min (l1), max (l1))
	am = ArithmeticMean (len (l1), min (l1), max (l1))
	
	"""
	tp = Transform (len (l1), min (l1), max (l1),
		lambda x: x + 1, lambda y: y - 1,
		ProdOp)
	tc = Transform (len (l1), min (l1), max (l1),
		lambda x: x + 1, lambda y: y - 1,
		CntOp)
	"""
	gm = Transform (len (l1), min (l1), max (l1),
		lambda x: x + 1, lambda y: y - 1,
		GeometricMean)
	#add1 = Sum (
	#	len (l1), min (l1), max (l1),
	#	len (l1), 1, 1)
	#l2 = map (lambda (x, y): add1.op (x, y), zip (l1, [1] * len (l1)))
	#prodop = ProdOp (len (l2), min (l2), max (l2))
	#cntop = CntOp (len (l2), min (l2), max (l2))
	#gm = GeometricMean (len (l2), min (l2), max (l2), prodop, cntop)
	#map (gm.update, l2)
	#map (gm.update, l1)
	#gm.finish ()
	#gm.validate ()
	#print gm.value
	"""
	add1 = Sum (
		len (l1), min (l1), max (l1),
		len (l1), 1, 1)
	l3 = map (lambda (x, y): add1.op (x, y), zip (l1, [1] * len (l1)))
	hm = HarmonicMean (len (l3), min (l3), max (l3))
	
	tm = TriMean (am, gm, hm)
	"""
	hm = Transform (len (l1), min (l1), max (l1),
		lambda x: x + 1, lambda y: y - 1,
		HarmonicMean)
	
	tm = TriMean (am, gm, hm)
	map (tm.update, l1)
	tm.finish ()
	tm.validate ()
	print tm.value
	
	ad = AbsoluteDifference (
		min (l1), max (l1),
		min (l2), max (l2))
	print map (lambda (x, y): ad.op (x, y), zip (l1, l2))
	
	ad = AbsoluteDifference (
		min (l2), max (l2),
		min (l1), max (l1))
	print map (lambda (x, y): ad.op (x, y), zip (l2, l1))
	
	l3 = list (xrange (12, 20))
	l4 = list (xrange (2, 10))
	ad = AbsoluteDifference (
		min (l3), max (l3),
		min (l4), max (l4))
	print map (lambda (x, y): ad.op (x, y), zip (l3, l4))
	
	l5 = list (xrange (22, 30))
	ad = AbsoluteDifference (
		min (l3), max (l3),
		min (l5), max (l5))
	print map (lambda (x, y): ad.op (x, y), zip (l3, l5))
	
	l6 = list (xrange (12 - 4, 12 + 4))
	ad = AbsoluteDifference (
		min (l3), max (l3),
		min (l6), max (l6))
	print map (lambda (x, y): ad.op (x, y), zip (l3, l6))
	
	l7 = list (xrange (20 - 4, 20 + 4))
	ad = AbsoluteDifference (
		min (l3), max (l3),
		min (l7), max (l7))
	print map (lambda (x, y): ad.op (x, y), zip (l3, l7))
	
	l8 = list (xrange (12 - 4, 20 + 4, 2))
	ad = AbsoluteDifference (
		min (l3), max (l3),
		min (l8), max (l8))
	print map (lambda (x, y): ad.op (x, y), zip (l3, l8))
	
	ad = AbsoluteDifference (
		min (l8), max (l8),
		min (l3), max (l3))
	print map (lambda (x, y): ad.op (x, y), zip (l8, l3))
	
	pd = PowerDifference (
		min (l1), max (l1),
		min (l2), max (l2))
	print map (lambda (x, y): pd.op (x, y), zip (l1, l2))
	
	pd = PowerDifference (
		min (l1), max (l1),
		min (l2), max (l2), 3)
	print map (lambda (x, y): pd.op (x, y), zip (l1, l2))
	
	pd = PowerDifference (
		min (l1), max (l1),
		min (l2), max (l2), .5)
	print map (lambda (x, y): pd.op (x, y), zip (l1, l2))
	
	dp = DifferencePower (
		min (l1), max (l1),
		min (l2), max (l2))
	print map (lambda (x, y): dp.op (x, y), zip (l1, l2))
	
	dp = DifferencePower (
		min (l1), max (l1),
		min (l2), max (l2), 3)
	print map (lambda (x, y): dp.op (x, y), zip (l1, l2))
	
	dp = DifferencePower (
		min (l1), max (l1),
		min (l2), max (l2), .5)
	print map (lambda (x, y): dp.op (x, y), zip (l1, l2))
	
	add2 = Sum (
		min (l1), max (l1),
		2, 2)
	l9 = map (lambda (x, y): add2.op (x, y), zip (l1, [2] * len (l1)))
	gd = GeometricDifference (
		min (l9), max (l9),
		min (l2), max (l2))
	print map (lambda (x, y): gd.op (x, y), zip (l9, l2))
	
	hd = HarmonicDifference (
		min (l9), max (l9),
		min (l2), max (l2))
	print map (lambda (x, y): hd.op (x, y), zip (l9, l2))
	
	v = GeneralizedVariance (len (l1), min (l1), max (l1),
		StdDevCT, DifferencePower, am.value)
	map (v.update, l1)
	v.finish ()
	#print sqrt (v.value)
	print v.value
	# TODO std dev isn't exactly the arithmetic mean
	#print sqrt (v.value * len (l1) / (len (l1) - 1))
	
	v = StandardDeviation (len (l1), min (l1), max (l1), am.value)
	map (v.update, l1)
	v.finish ()
	print v.value
	
	p = PopCount (min (l1), max (l1))
	print map (p.op, l1)