import sys
import serial
import numpy as np


CHNL_MAX        =   8
SIZEOF_SMPL     =   2
SMPLS_PER_FRAME =   (2048 / CHNL_MAX) / SIZEOF_SMPL


def frame_read( frame, length ):
    global stream
    sync_tocken     =   stream.read(1)

    if(sync_tocken != '\x7E'):
        sync            =   False
    else:
        sync            =   True
        spare           =   stream.read(3)
        frame           =   stream.read( length )

    return sync


def frame_parse( frame, length ):
    print ".",
"""
    for i in length:
        ch[0],
        ch[1],
        ch[2],
        ch[3],
        ch[4],
        ch[5],
        ch[6],
        ch[7]           =   struct.unpack( fmt, frame )
"""


def plot(x, y, xmin, xmax, ymin, ymax, pygame_screen):
    w, h = pygame_screen.get_size()
    x = array(x)
    y = array(y)
    
    #Scale data
    xspan = abs(xmax-xmin)
    yspan = abs(ymax-ymin)
    xsc = 1.0*w/xspan
    ysc = 1.0*h/yspan
    xp = (x-xmin)*xsc
    yp = h-(y-ymin)*ysc
        
    #Plot data
    pygame_screen.fill((255,255,255))
    for i in range(len(xp)-1):
        pygame.draw.line(pygame_screen, (0, 0, 255), (int(xp[i]),
                                                      int(yp[i])), 
                                                     (int(xp[i+1]),
                                                      int(yp[i+1])), 1)

""" start """
print "\nplot DDAS stream data\n"

out_file        =   open( "output.dat", 'wb'  )  

""" get settings """
try:
    serial_port     =   sys.argv[1]
    serial_baud     =   sys.argv[2]
except:
    print "usage:       ", sys.argv[0], "<serial port>"
    sys.exit( 1 )

""" get input stream """
print "open", serial_port, "...",

try:
    stream          =   serial.Serial()
    stream.port     =   serial_port
    stream.baudrate =   serial_baud
    stream.open()
    #print "success"
    print "success"
except:
    print "error"
    sys.exit( 2 )


""" main loop """
sync            =   False

data_raw        =   []
data_raw_len    =   1024

#rows, cols      =   768, 1024
#image           =   np.random.randint( 100, 14000, size = (1, rows, cols) ).astype(np.uint16)
#data            =   np.zeros( (CHNL_MAX, SMPL_PER_FRAME) )
data            =   np.empty( [CHNL_MAX, SMPLS_PER_FRAME], dtype = np.uint16 )

while True:
    sync            =   frame_read( data_raw, data_raw_len )

    if( sync ):
        #sample      =   frame_parse( frame, frame_len )
        data        =   frame_parse( data_raw, data_raw_len )
        #out_file.write( data[0] )

        x           =   arange( data_raw_len )
        y           =   data.copy()
        plot( x, y, 0, data_buff_size, 0, 1024, screen )

"""
    try:
        sync        =   stream.read(1)

        if sync == 0x7E:
            print "\r"
        else:
            print sync,
    except:
        print "serial error"
        stream.close()
        sys.exit( 3 )
"""

stream.close()
