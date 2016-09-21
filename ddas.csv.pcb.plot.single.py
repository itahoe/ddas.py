
import csv
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
fn=root.fileName
def plot_df(df, out_plot_fn=None, mult_factor=0.8,
            cols=None, x_axis=None, figsize=(12,10)):
    if x_axis:
        df = df.set_index(x_axis)

    if cols:
        df.columns = cols

    if mult_factor and mult_factor != 1:
        df *= mult_factor

    ax = df.plot.line(figsize=figsize)

    if out_plot_fn:
        plt.savefig(out_plot_fn)
    else:
        plt.show()



usecols = [0,1,2,3,4,5,7]

df = pd.read_csv(fn, usecols=usecols, skipinitialspace=True)
# переименуем названия колонок в DF
cols = ['ch1','ch2','ch3','ch4','ch5','ch6','ch8']
plot_df(df, cols=cols, out_plot_fn=r'd:/b.png')
root.destroy()
plt.show()