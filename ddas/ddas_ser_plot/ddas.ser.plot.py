import numpy as np
import pygame
import serial as ser
import struct
import sys
import threading
import matplotlib.pyplot as plt
import scipy.fftpack


pygame.init()

global lock
global serial_port


lock            =   threading.Lock()
out_file        =   open( "output.dat", 'wb'  )  

data_raw_len    =   2048
smpl_sizeof     =   2
data_chnl_max   =   8
smpl_range_max  =   4096

chnl_current    =   7


class ReadStream(threading.Thread):
        
    #thread event, stops the thread if it is set.
    stopthread = threading.Event()

    def __init__( self ):
        threading.Thread.__init__( self )                               #call constructor of parent
        self.ser            =   ser.Serial( serial_port, serial_baud )  #Initialize serial port
        self.data_smpl_size =   data_raw_len / (data_chnl_max * smpl_sizeof)
        self.data_smpl      =   np.empty( self.data_smpl_size, dtype=np.uint16 )
        #self.data_smpl      =   np.empty( [self.data_smpl_size, data_chnl_max], dtype=np.uint16 )
        self.start()

    def run( self ):                                                    #runs while thread is alive.
        while not self.stopthread.isSet() :
            sync_tocken     =   self.ser.read(1)

            if(sync_tocken == '\x7E'):
                reserved        =   self.ser.read(3)
                data_raw        =   self.ser.read( data_raw_len )

                sample          =   struct.Struct(  'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH'   )

                data_block      =   sample.unpack( data_raw )

                for i in range( self.data_smpl_size ):
                    lock.acquire()
                    self.data_smpl      = np.roll(self.data_smpl,-1)
                    self.data_smpl[0]   = data_block[i * 8 + chnl_current]
                    lock.release()

                #out_file.write( self.data_smpl )
                #print self.data_smpl
                #print data_raw,
                #print data_block
                #print self.data_smpl

        self.ser.close()


    def stop(self):
        self.stopthread.set()


class Display():
    

    def __init__(self):
        self.screen         = pygame.display.set_mode( (640, 480) )
        pygame.display.set_caption( "DDAS plot" )
        self.clock          = pygame.time.Clock()
        self.dataflow       = ReadStream()
        self.run()
        

    def plot(self, x, y, xmin, xmax, ymin, ymax):
        w, h                = self.screen.get_size()
        x                   = np.array(x)
        y                   = np.array(y)
        grid_color          =   0,   0,   0
        grid_width          =   1
        line_color          = 255, 255,   0
        line_width          =   2

        #scale data
        xspan               = abs(xmax - xmin)
        yspan               = abs(ymax - ymin)
        xsc                 = 1.0 * (w + 1) / xspan
        ysc                 = 1.0 * h / yspan
        xp                  = (x - xmin) * xsc
        yp                  = h - (y-ymin) * ysc

        #grid
        for i in range(10):
            pygame.draw.line(   self.screen,
                                grid_color,
                                ( 0, int(h * 0.1 * i) ),
                                ( w-1, int(h * 0.1 * i) ),
                                grid_width )

            pygame.draw.line(   self.screen,
                                grid_color,
                                ( int(w * 0.1 * i), 0 ),
                                ( int(w * 0.1 * i), h-1 ),
                                grid_width )

        pygame.draw.line(   self.screen,
                            grid_color,
                            ( 0, int(h * 0.5) ),
                            ( w-1, int(h * 0.5) ),
                            grid_width * 2 )

        #data
        for i in range( len(xp)-1 ):
            pygame.draw.line(   self.screen,
                                line_color,
                                ( int(xp[  i]), int(yp[  i]) ),
                                ( int(xp[i+1]), int(yp[i+1]) ),
                                line_width )


    def run(self):
        fill_color          = 127, 127, 127
        
        #main loop supply
        font            = pygame.font.Font(pygame.font.match_font(u'mono'), 20)
        data_smpl_size  = self.dataflow.data_smpl_size
        hold            = False

        while True:
            #process events
            event           = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                self.dataflow.stop()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_h:
                    hold        = not hold

            self.screen.fill( fill_color )     

            #plot current buffer
            if not hold:
                lock.acquire()
                x           = np.arange( data_smpl_size, dtype=np.uint16 )
                y           = self.dataflow.data_smpl
                lock.release()

            self.plot( x, y, 0, data_smpl_size, 0, smpl_range_max)

            #show FPS
            text = font.render("%3d fps"%self.clock.get_fps(), 1, (0, 10, 10))
            self.screen.blit(text, (10, 10))
            pygame.display.flip()
            self.clock.tick(0)

try:
    serial_port     =   sys.argv[1]
    serial_baud     =   sys.argv[2]
except:
    print "usage:       ", sys.argv[0], "<serial port>, <serial baud>"
    sys.exit( 1 )

display     = Display()
out_file.close()
