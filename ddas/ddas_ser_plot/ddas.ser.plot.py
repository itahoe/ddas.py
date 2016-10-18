import sys
import serial


def synchronize( data ):
    sync            =   False
    frame_size      =   1
    return sync, frame_size


""" start """
print "\nplot DDAS stream data\n"


""" get settings """
try:
    serial_port     =   sys.argv[1]
    serial_baud     =   sys.argv[2]
except:
    print "usage:       ", sys.argv[0], "<serial port>"
    sys.exit( 1 )

""" get input data """
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


out_file        =   open( "output.dat", 'wb'  )  


""" main loop """
sync            =   False

"""
while True:
    if sync:
        data        =   stream.read( frame_size )
    else:
        sync,
        frame_size  =   synchronize( stream.read(1) )
        print sync,
"""
counter         =   0
while True:
        data        =   stream.read( 1024 )
        out_file.write( data )
        counter     +=  1
        if( counter > 1000 ):
            break

print "done"
                    
stream.close()
out_file.close()
