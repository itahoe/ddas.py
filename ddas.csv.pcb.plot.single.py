import numpy as np
import matplotlib.pyplot as plt
import pylab
import pandas as pd
import Tkinter,tkFileDialog

root = Tkinter.Tk() 


root.fileName=tkFileDialog.askopenfilename(filetypes=(("csv files","*csv"),("All files","*.*" )))
fn=root.fileName
#df = pd.read_csv(fn, skipinitialspace=True)
root.destroy()
#plot_df(df, out_plot_fn=r'd:/bad.png')

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

# пропускаем 7-ю колонку (Python/Pandas считают с нуля, поэтому - 6-ю)
# иначе по Y-axis будет неправильное масштабирование
# и все графики будут выглядеть слишком сглаженными 
usecols = [0,1,2,3,4,5,7]

df = pd.read_csv(fn, usecols=usecols, skipinitialspace=True)

#plot_df(df, out_plot_fn=r'd:/a.png')

# переименуем названия датчиков
cols = ['ch1','ch2','ch3','ch4','ch5','ch6','ch8']
plot_df(df, cols=cols, out_plot_fn=r'd:/b.png',figsize=(17, 14))
plt.show()

# только первые 50 строк
#plot_df(df.head(50), out_plot_fn=r'd:/c.png')
plt.show()
input()
