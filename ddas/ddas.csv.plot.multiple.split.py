import numpy as np
import matplotlib.pyplot as plt
import pylab
import pandas as pd
import Tkinter,tkFileDialog

root = Tkinter.Tk()
filez = tkFileDialog.askopenfilenames(parent=root,title='Choose 2 or more files',filetypes=(("csv files","*csv"),("All files","*.*" )))
t=list(filez)
p=len(filez)
root.destroy()
print(p)
if p==2:
 data0 = pd.read_csv(t[0],sep=u',', header=14, skip_footer=0)
 df0 = pd.DataFrame(data=data0,columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data1 = pd.read_csv(t[1],sep=u',', header=14, skip_footer=0)
 df1 = pd.DataFrame(data=data1, columns=['CH1', 'CH2', 'CH3', 'CH4'])  

 f, ax = plt.subplots(2,2,figsize=(20, 10))
 ax[0,0].plot(df0)
 ax.set_title("Title for second plot")
 ax[0,1].plot(df1)
##################
elif p==3:
 data0 = pd.read_csv(t[0],sep=u',', header=14, skip_footer=0)
 df0 = pd.DataFrame(data=data0,columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data1 = pd.read_csv(t[1],sep=u',', header=14, skip_footer=0)
 df1 = pd.DataFrame(data=data1, columns=['CH1', 'CH2', 'CH3', 'CH4'])  

 data2 = pd.read_csv(t[2],sep=u',', header=14, skip_footer=0)
 df2 = pd.DataFrame(data=data2, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 f, ax = plt.subplots(2,2,figsize=(20, 10))
 ax[0,0].plot(df0)
 ax[0,1].plot(df1)
 ax[1,0].plot(df2)
#################
elif p==4:
 data0 = pd.read_csv(t[0],sep=u',', header=14, skip_footer=0)
 df0 = pd.DataFrame(data=data0,columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data1 = pd.read_csv(t[1],sep=u',', header=14, skip_footer=0)
 df1 = pd.DataFrame(data=data1, columns=['CH1', 'CH2', 'CH3', 'CH4'])  

 data2 = pd.read_csv(t[2],sep=u',', header=14, skip_footer=0)
 df2 = pd.DataFrame(data=data2, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data3 = pd.read_csv(t[3],sep=u',', header=14, skip_footer=0)
 df3 = pd.DataFrame(data=data3, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 f, ax = plt.subplots(2,2,figsize=(20, 10))
 ax[0,0].plot(df0)
 ax[0,1].plot(df1)
 ax[1,0].plot(df2)
 ax[1,1].plot(df3)
##################### 
elif p==5:
 data0 = pd.read_csv(t[0],sep=u',', header=14, skip_footer=0)
 df0 = pd.DataFrame(data=data0,columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data1 = pd.read_csv(t[1],sep=u',', header=14, skip_footer=0)
 df1 = pd.DataFrame(data=data1, columns=['CH1', 'CH2', 'CH3', 'CH4'])  

 data2 = pd.read_csv(t[2],sep=u',', header=14, skip_footer=0)
 df2 = pd.DataFrame(data=data2, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data3 = pd.read_csv(t[3],sep=u',', header=14, skip_footer=0)
 df3 = pd.DataFrame(data=data3, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data4 = pd.read_csv(t[4],sep=u',', header=14, skip_footer=0)
 df4 = pd.DataFrame(data=data3, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 f, ax = plt.subplots(3,2,figsize=(20, 10))
 ax[0,0].plot(df0)
 ax[0,1].plot(df1)
 ax[1,0].plot(df2)
 ax[1,1].plot(df3)
 ax[2,1].plot(df3)
 #####################
elif p==6:
 data0 = pd.read_csv(t[0],sep=u',', header=14, skip_footer=0)
 df0 = pd.DataFrame(data=data0,columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data1 = pd.read_csv(t[1],sep=u',', header=14, skip_footer=0)
 df1 = pd.DataFrame(data=data1, columns=['CH1', 'CH2', 'CH3', 'CH4'])  

 data2 = pd.read_csv(t[2],sep=u',', header=14, skip_footer=0)
 df2 = pd.DataFrame(data=data2, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data3 = pd.read_csv(t[3],sep=u',', header=14, skip_footer=0)
 df3 = pd.DataFrame(data=data3, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data4 = pd.read_csv(t[4],sep=u',', header=14, skip_footer=0)
 df4 = pd.DataFrame(data=data4, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 data5 = pd.read_csv(t[5],sep=u',', header=14, skip_footer=0)
 df5 = pd.DataFrame(data=data5, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 f, ax = plt.subplots(3,2,figsize=(20, 10))
 ax[0,0].plot(df0)
 ax[0,1].plot(df1)
 ax[1,0].plot(df2)
 ax[1,1].plot(df3)
 ax[2,1].plot(df4)
 ax[2,2].plot(df5)
 #####################
elif p==7:
 data0 = pd.read_csv(t[0],sep=u',', header=14, skip_footer=0)
 df0 = pd.DataFrame(data=data0,columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data1 = pd.read_csv(t[1],sep=u',', header=14, skip_footer=0)
 df1 = pd.DataFrame(data=data1, columns=['CH1', 'CH2', 'CH3', 'CH4'])  

 data2 = pd.read_csv(t[2],sep=u',', header=14, skip_footer=0)
 df2 = pd.DataFrame(data=data2, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data3 = pd.read_csv(t[3],sep=u',', header=14, skip_footer=0)
 df3 = pd.DataFrame(data=data3, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data4 = pd.read_csv(t[4],sep=u',', header=14, skip_footer=0)
 df4 = pd.DataFrame(data=data4, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 data5 = pd.read_csv(t[5],sep=u',', header=14, skip_footer=0)
 df5 = pd.DataFrame(data=data5, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 data6 = pd.read_csv(t[6],sep=u',', header=14, skip_footer=0)
 df6 = pd.DataFrame(data=data6, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 f, ax = plt.subplots(4,2,figsize=(20, 10))
 ax[0,0].plot(df0)
 ax[0,1].plot(df1)
 ax[1,0].plot(df2)
 ax[1,1].plot(df3)
 ax[2,1].plot(df4)
 ax[2,2].plot(df5)
 ax[3,1].plot(df6)
 #####################
elif p==8:
 data0 = pd.read_csv(t[0],sep=u',', header=14, skip_footer=0)
 df0 = pd.DataFrame(data=data0,columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data1 = pd.read_csv(t[1],sep=u',', header=14, skip_footer=0)
 df1 = pd.DataFrame(data=data1, columns=['CH1', 'CH2', 'CH3', 'CH4'])  

 data2 = pd.read_csv(t[2],sep=u',', header=14, skip_footer=0)
 df2 = pd.DataFrame(data=data2, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data3 = pd.read_csv(t[3],sep=u',', header=14, skip_footer=0)
 df3 = pd.DataFrame(data=data3, columns=['CH1', 'CH2', 'CH3', 'CH4'])

 data4 = pd.read_csv(t[4],sep=u',', header=14, skip_footer=0)
 df4 = pd.DataFrame(data=data4, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 data5 = pd.read_csv(t[5],sep=u',', header=14, skip_footer=0)
 df5 = pd.DataFrame(data=data5, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 data6 = pd.read_csv(t[6],sep=u',', header=14, skip_footer=0)
 df6 = pd.DataFrame(data=data6, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 data7 = pd.read_csv(t[7],sep=u',', header=14, skip_footer=0)
 df7 = pd.DataFrame(data=data7, columns=['CH1', 'CH2', 'CH3', 'CH4'])
 
 f, ax = plt.subplots(4,2,figsize=(20, 10))
 ax[0,0].plot(df0)
 ax[0,1].plot(df1)
 ax[1,0].plot(df2)
 ax[1,1].plot(df3)
 ax[2,0].plot(df4)
 ax[2,1].plot(df5)
 ax[3,0].plot(df6)
 ax[3,1].plot(df7)
 #####################
plt.show()

