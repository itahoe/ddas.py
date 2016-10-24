import numpy as np
import pygame
import serial as ser
import struct
import sys
import threading


pygame.init()

global lock
global serial_port
lock = threading.Lock()


class ReadStream(threading.Thread):
        
    #Thread event, stops the thread if it is set.
    stopthread = threading.Event()

    def __init__( self ):
        threading.Thread.__init__( self )                       #Call constructor of parent
        self.ser            =   ser.Serial( serial_port, 115200 )     #Initialize serial port
        self.data_smpl_size =   1024 / (8 * 2)
        self.data_smpl      =   np.zeros( self.data_smpl_size )
        #self.data_smpl      =   np.arange( self.data_smpl_size )
        #self.data_smpl      =   np.empty( self.data_smpl_size )
        self.start()

    def run( self ):                                            #runs while thread is alive.
        #num_bytes           = 400                               #Number of bytes to read at once
        #num_smpls           = num_bytes / 2
        data_chnl_max       =   8
        data_raw_len        =   1024
        data_len            =   data_raw_len / 2
        val                 = 0                                 #Read value
        
        def frame_read( length ):
            #global stream
            sync_tocken     =   self.ser.read(1)

            if(sync_tocken != '\x7E'):
                sync            =   False
            else:
                sync            =   True
                #spare           =   self.ser.read(3)
                #frame           =   self.ser.read( length )

            return sync

        while not self.stopthread.isSet() :
            sync            =   frame_read(1)
            if( sync ):
                spare           =   self.ser.read(3)
                data_raw        =   self.ser.read( data_raw_len )

                #sample          =   struct.Struct( 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'  )
                #data_smpl       =   sample.unpack( data_raw[:data_raw_len:data_chnl_max] )

                sample          =   struct.Struct(  'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' \
                                                    'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH' 'HHHHHHHH'   )

                data_block      =   sample.unpack( data_raw )

                #data            =   self.ser.read( data_raw_len )
                #data_raw            = self.ser.read( num_bytes )        #Read serial data
                #byte_array          = unpack( '%dH' % num_smpls, rslt ) #Convert serial data to array of numbers
                #data_smpl       =   struct.unpack( 'H' % data_raw_len, data_raw ) #Convert serial data to array of numbers


                """
                for smpl in data_smpl[0::8]:
                    lock.acquire()
                    #self.data           = np.roll(self.data,-1)
                    #self.data[-1]       = byte + 2000
                    self.data[-1]       = smpl + 2000
                    lock.release()
                """

                """
                for smpl in data_smpl:
                    lock.acquire()
                    #self.data           = np.roll(self.data,-1)
                    #self.data[-1]       = byte + 2000
                    self.data_smpl      = np.roll(self.data_smpl, -1)
                    #self.data_smpl      = smpl
                    lock.release()
                """

                """
                for smpl in data_block[::8]:
                    lock.acquire()
                    #self.data_smpl      = np.roll(self.data_smpl, -1)
                    np.append( self.data_smpl, smpl )
                    lock.release()
                """
                for i in range( 64 ):
                    self.data_smpl[i]   = data_block[i*8+0]

                #print self.data_smpl
                #print data_raw,
                #print data_block
                #print self.data_smpl


                #for i in range( data_raw_len ):
                    #lock.acquire()
                    #byte0               = self.ser.read()
                    #byte1               = self.ser.read()
                    #self.data           = np.roll(byte0, -1)
                    #self.data[-1]       = byte1
                    #lock.release()


            #sample      =   frame_parse( frame, frame_len )
            #data        =   frame_parse( data_raw, data_raw_len )
            #out_file.write( data[0] )
            #x           =   arange( data_raw_len )
            #y           =   data.copy()
            #plot( x, y, 0, data_buff_size, 0, 1024, screen )
                    


        self.ser.close()


    def stop(self):
        self.stopthread.set()


class Display():
    

    def __init__(self):
        self.screen         = pygame.display.set_mode((640, 480))
        self.clock          = pygame.time.Clock()
        self.data_reader    = ReadStream()
        self.run()
        

    def plot(self, x, y, xmin, xmax, ymin, ymax):
        w, h                = self.screen.get_size()
        x                   = np.array(x)
        y                   = np.array(y)
        grid_color          =   0,   0,   0
        grid_width          =   1
        line_color          = 255, 255,   0
        line_width          =   1

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
        data_smpl_size  = self.data_reader.data_smpl_size
        hold            = False

        while True:
            #process events
            event           = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                self.data_reader.stop()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_h:
                    hold        = not hold

            self.screen.fill( fill_color )     

            #plot current buffer
            if not hold:
                lock.acquire()
                x           = np.arange( data_smpl_size, dtype=np.uint16 )
                y           = self.data_reader.data_smpl
                lock.release()
            #self.plot( x, y, 0, data_smpl_size, 0, 1024 )
            self.plot( x, y, 0, data_smpl_size, 0, 4096)

            #show FPS
            text = font.render("%3d fps"%self.clock.get_fps(), 1, (0, 10, 10))
            self.screen.blit(text, (10, 10))
            pygame.display.flip()
            self.clock.tick(0)

try:
    serial_port     =   sys.argv[1]
    serial_baud     =   sys.argv[2]
except:
    print "usage:       ", sys.argv[0], "<serial port>"
    sys.exit( 1 )

display     = Display()
