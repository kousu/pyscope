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
l, = plt.plot(arange(44100), lw=.5, color='green')
plt.xlabel("time (s)")
plt.ylabel("amplitude")
print(l)
print(l.get_data())
#time.sleep(1)

MAXPT = 0
LAST = 0

def pysoundcard_callback(in_data, frame_count, time_info, status):
	global LAST
	NOW = time.time()
	# pysoundcard is giving 32 channels on my machine??
	# but the upper channels are empty and the lower ones are dupes?
	signal = (in_data[:,1] + in_data[:,0])/2
	
	#period = time_info['input_adc_time']
	#if period < 0:
	
	period = NOW - LAST
	LAST = time.time()
	if period > 1: #coerce overly long periods (probably due to hangs) to noops
		return (zeros_like(in_data), continue_flag)

	
	#print(period, MAXPT)
	#print("energy:", abs(signal).sum(), "/%.2fms" % (period*1e3,))
	
	t = arange(0, len(signal))/len(signal) * period
	a = signal;
	l.set_data((t, a))
	
	global MAXPT
	#MAXPT = .005
	if period > MAXPT:
		MAXPT = period
	#print(max(a))
	
	#max.set_xlim((0, period*.6)) #..huh?
	ax.set_xlim((0, MAXPT*.2)) #..huh?
	ax.set_ylim((-1, 1))
	#ax.set_ylim((min(a), max(a)))
	
	fig.canvas.draw()
	#if period > 0: time.sleep(period)
	return (zeros_like(in_data), continue_flag)

# how do i get plt to display
# fuck, why does matplotlib make making interaction so difficult?
# I just want you to MAKE ME A PLOT GODDAMMIT


fs = 44100                  #sample rate to open the card at
block_length = 44100//(24) #given a known sample rate, defines how long a single window is (
s = Stream(sample_rate=fs, block_length=block_length, callback=pysoundcard_callback)
print("starting soundcard")
s.start()

#plt.ion()
#plt.show(block=False) #block
# fuck ..there's no way to both block
from threading import Thread
# of course ,putting shit on another thread doesn't hardly help...

def fix_it():
	"Work around some kind of overdriving bug in alsa"
	while True:
		if not s.is_active():
			print("Soundcard crashed. resetting:")
			#time.sleep(22)
			s.stop()
			s.start()
		time.sleep(2)
FIXIT = Thread(target=fix_it)
FIXIT.start()


plt.show()
