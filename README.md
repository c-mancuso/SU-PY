# SU-PY
Quickly load Seismic Unix (SU) files in Python from command line

Written by Chris Mancuso
Sept. 19, 2019

Seismic Unix to Python back to Seismic Unix Tool
For automating experimental Seismic Data Processing subroutines in 
tandem with the open source Seismic Unix Program.

Works from command line usually to pipe "|" into and out of SU file
structures (240 byte header > trace). 

Written to implement some operations
for my Masters research, I found this to be the fastest possible implementation
of python with SU (a popular, free and comprehensive seismic data processing
CLI program).

Shown example works for operating on one trace at a time, useful for 
applyin static shifts, some random noise attenuation, moveout,
or any other operations which can be performed independant of sorting.

Code can be easily changed to load many traces at a time (ie. gathers 
etc.) but may overflow memory.

ex: sugain < stdin agc=1 | python supy_example.py | suximage

For more information on Seismic Unix see https://github.com/JohnWStockwellJr/SeisUnix/wiki
