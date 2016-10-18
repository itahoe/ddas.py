#!/usr/bin/env python


import sys
import math
import struct


def ddas_header( header ):
    inp_file.seek( 1024 )   # skip file header
    timebase_sec    = 1.0
    return timebase_sec

   
DDAS_HEADER_SIZE_OCT    = 1024
DDAS_FRAME_SIZE_OCT     = 4096
blocks_per_frame        = 255

header_format           =   'IIII'

frame_format            =   'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                                                                                    \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                                                                                    \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                                                                                    \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                                                                                    \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                                                                                    \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                                                                                    \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                                                                                    \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                            'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH'

print "\nconvert DDAS binary data to CSV format\n"

#
# get input data 
#
try:
    inp_file_name   =   sys.argv[1]
    out_file_name   =   inp_file_name + ".csv"
except:
    print "usage:       ", sys.argv[0], "input_file"
    sys.exit( 1 )

inp_file        =   open( inp_file_name, 'rb' )
out_file        =   open( out_file_name, 'w'  )  

print "output file:     ", out_file_name
print "converting...    ",

line_num        = 0
header          = inp_file.read( DDAS_HEADER_SIZE_OCT )
timebase_sec    = ddas_header( header )
block_num       = 0
blocks_total    = 0

while True:
    frame           = inp_file.read( DDAS_FRAME_SIZE_OCT )

    if len( frame ) == 0:
        break

    block_num       += 1
    print "\rconverting block  %i of %i" % (block_num, blocks_total),

    header          = struct.Struct( header_format )
    sample          = struct.Struct( frame_format  )
    h               = header.unpack( frame[  0:  16] )
    s               = sample.unpack( frame[ 16:4096] )
#    timestamp       = hdr[ 1 ]
    timestamp       = h[ 1 ] * blocks_per_frame

    i               = 0
    while i < blocks_per_frame:
        j               = i*8
        out_file.write( '%i,%i,%i,%i,%i,%i,%i,%i,%i,\n' %
                        (timestamp, s[j+0], s[j+1], s[j+2], s[j+3], s[j+4], s[j+5], s[j+6], s[j+7]) )
        i               += 1
        timestamp       *= timebase_sec
        line_num        += 1



print "\r\ndone"
print "lines, total:    ", line_num
                    
inp_file.close()
out_file.close()
