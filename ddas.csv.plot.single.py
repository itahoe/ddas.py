import numpy as np
import matplotlib.pyplot as plt
import pylab
import pandas as pd
from Tkinter import*
import tkFileDialog as filedialog
def hide_me(event):
    event.widget.pack_forget()
root=Tk()
root.fileName=filedialog.askopenfilename(filetypes=(("csv files","*csv"),("All files","*.*" )))
k=root.fileName
print(k)
root.destroy()
import pandas as pd
data = pd.read_csv(k,sep=u',', header=14, skip_footer=0)
data.plot(x='TIME',y=['CH1','CH2','CH3','CH4'],figsize=(14, 10))
data.plot(x='TIME',y=['CH1 Peak Detect','CH2 Peak Detect','CH3 Peak Detect','CH4 Peak Detect'],figsize=(14, 10))

pylab.show()
