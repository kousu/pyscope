import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.widgets import Slider, Button, RadioButtons

import time

from pysoundcard import *
from pysoundfile import *

from scipy import *

#plt.ion() #key? does this show up???
fig, ax = plt.subplots()

#plt.subplots_adjust(left=0.25, bottom=0.25)
l, = plt.plot(arange(44100), lw=2, color='red')
print(l)
print(l.get_data())
#time.sleep(1)

MAXPT = 0

def pysoundcard_callback(in_data, frame_count, time_info, status):
	# pysoundcard is giving 32 channels on my machine??
	# but the upper channels are empty and the lower ones are dupes?
	signal = in_data[:,1]
	period = time_info['input_adc_time']
	#print(signal)
	
	#print("energy:", abs(signal).sum(), "/%.2fms" % (period*1e3,))
	
	t = arange(0, len(signal))/len(signal) * period
	a = signal;
	l.set_data((t, a))
	
	#global MAXPT
	MAXPT = .005
	#if max(t) > MAXPT:
	#	MAXPT = max(t)
	
	ax.set_xlim((0, period)) #..huh?
	ax.set_ylim((-1, 1))
	#ax.set_ylim((min(a), max(a)))
	
	fig.canvas.draw()
	
	return (zeros_like(in_data), continue_flag)

# how do i get plt to display
# fuck, why does matplotlib make making interaction so difficult?
# I just want you to MAKE ME A PLOT GODDAMMIT


fs = 44100
block_length = 100 #does this actually do anything?
s = Stream(sample_rate=fs, block_length=block_length, callback=pysoundcard_callback)
print("starting soundcard")
s.start()
plt.show() #block
