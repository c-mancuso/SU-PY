#!/usr/bin/env python
""" 
Written by Chris Mancuso
Sept. 19 2019

Seismic Unix to Python back to Seismic Unix Tool
For automating experimental Seismic Data Processing subroutines in 
tandem with the open source Seismic Unix Program.

Works from command line usually to pipe "|" into and out of SU file
structures (240 byte header > trace)

Shown example works for operating on one trace at a time, useful for 
applyin static shifts, some random noise attenuation, moveout,
or any other operations which can be performed independant of sorting.

Code can be easily changed to load many traces at a time (ie. gathers 
etc.) but may overflow memory.

ex: sugain < stdin agc=1 | python supy_example.py | suximage

See README for more information
"""
import sys
import numpy as np

while True: #open and write out one trace at a time

	""" IMPORT TRACE HEADER """
	header_data=sys.stdin.read(240)
	if len(header_data)==0: break

	#open all two and four byte headers
	four_byte = np.fromstring(header_data, dtype='>i4') 
	two_byte=np.fromstring(header_data, dtype='>i2')

	ns=two_byte[57] # ns is necessary to parse in trace data
	dt=two_byte[58]*1e-6 #example 2-byte header from byte 58
	
	""" IMPORT SEISMIC TRACE DATA """
	seismic_data=np.fromstring(sys.stdin.read(4*ns), dtype='>f4') #4 bytes per sample
	
	""" INSERT CODE HERE """
	#example operation on trace given (multiply by one in this case)
	seismic_data_out = seismic_data * 1
		
	""" WRITE OUT """
	sys.stdout.write(header_data)
	sys.stdout.write(seismic_data_out)
sys.stdout.close()
#END
