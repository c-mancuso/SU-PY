# SU-PY
Quickly load Seismic Unix (SU) files in Python 2.7 from command line

Written by Chris Mancuso
Sept. 19, 2019

Seismic Unix to Python back to Seismic Unix Tool
For automating experimental Seismic Data Processing subroutines in tandem with the open source Seismic Unix Program.

Works from command line usually to pipe "|" into and out of SU file structures (240 byte header > trace). 

Written to implement some operations for my Masters research, I found this to be the fastest possible implementation
of Python with SU (a popular, free and comprehensive seismic data processing CLI program).

Shown example works for operating on one trace at a time, useful for applying static shifts, some random noise attenuation, moveout, or any other operations which can be performed independant of sorting.

Have not codified the trace header byte lookup numbers yet, simply implement them from exploring the contents of the 2 and 4
byte header arrays grabbed. (Example, 'ns' is in position [57] of 2 byte array).  Values needed are easily obtained by passing
some test values through and printing out. If there in interest in the future I can make a subroutine to return values by
using a keyword, but I wanted to lay it out as simply as possible for the time being.

Code can be easily changed to load many traces at a time (ie. gathers etc.) but may overflow memory.

ex: sugain < stdin agc=1 | python supy_example.py | suximage

ex: file_in.su < python supy_example.py > file_out.su 

For more information on Seismic Unix see https://github.com/JohnWStockwellJr/SeisUnix/wiki
