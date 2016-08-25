from pyflann import *
from numpy import *
from numpy.random import *
import time

time.clock()
dataset = rand(10000, 128)
testset = rand(1000,128)
print "Generate Dataset using:" ,time.clock()
flann = FLANN()
print "dim=128,trainset size=1M using time", (time.clock())

result, dists = flann.nn(dataset, testset, 5, algorithm="kmeans", branching=32, iterations=7, checks=6)
print "FLANN nn using time:" , time.clock()
#print result[1:5]
