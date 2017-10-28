#!/usr/bin/env python
#Author: Maria Clara Moraes
from math import sqrt

#lx = [16 31 38 39 37 36 36 22 10]
#ly = [290 374 393 425 406 370 365 320 269]

def getRol(lx):
	sortedLx = sorted(lx)
	return sortedLx

def median(lx):
	lx.sort()
	n = len(lx)
	medianX = -1

	if n % 2 == 0:
		medianX = (lx[(n-1) / 2]  + lx[(n-1) / 2 + 1]) / 2.0

	else:
		medianX = lx[(n - 1) / 2]

	return medianX


def mode(lx):
	frequencies = [0 for i in range(max(lx) + 1)]
	n = len(lx)

	for i in range(n):
		frequencies[lx[i]] += 1

	mode = max(frequencies)
	modes = [mode]

	timesMode = 0
	for i in range(len(frequencies)):
		if frequencies[i] == mode:
			modes.append(i)
			timesMode += 1

	out = [] #number of modes, modes
	if timesMode < n:
		out.append(timesMode)
		out.append(modes)

	return out


def average(lx):
	return sum(lx) / len(lx)

def variance(lx):
	sumX = 0
	n = len(lx)
	mx = average(lx)

	for i in range(n):
		aux = (lx[i] - mx)**2
		sumX += aux

	return sumX / float(n)

def standardDeviation(lx):
	varX = variance(lx)

	return (sqrt(varX))

def averageDeviation(lx):
	mx = average(lx)
	sumX = 0
	n = len(lx)

	for i in range(n):
		sumX += abs(lx[i] - mx)

	return sumX / float(n)

def correlation(lx, ly):
	xy = 0
	sumX = 0
	sumY = 0
	sqrtX = 0
	sqrtY = 0

	for i in range(len(lx)):
		xy += lx[i] * ly[i]
		sumX += lx[i]
		sumY += ly[i]
		sqrtX += lx[i]**2
		sqrtY += ly[i]**2

	numerator = xy - (1.0 / len(lx)) * sumX * sumY
	denominator = sqrt((sqrtX - (1.0 / len(lx)) * sumX**2) * (sqrtY - (1.0 / len(lx) * sumY**2)))

	return numerator / denominator

while True:
	print "Options:"
	print "Press 1 for median"

lx = map(float, raw_input("Digite os valores da variavel X separados por espaco: \n").split())
print
ly = map(float, raw_input("Digite os valores da variavel Y separados por espaco: \n").split())

print ""
print "O valor da correlacao linear entre as variaveis eh: %.3f" %correlacao(lx, ly)
