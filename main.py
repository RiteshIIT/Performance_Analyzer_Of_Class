import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

sheet=pd.read_excel("marks.xlsx")
marks=sheet["marks"]
mean=marks.mean()
median=marks.median()
mode=marks.mode().iloc[0]
sdeviation=marks.std()
frequency=marks.value_counts().sort_index()

x_new=np.linspace(marks.min(),marks.max(),300)
spl=make_interp_spline(frequency.index,frequency.values,k=3)
y_smooth=spl(x_new)

plt.scatter(frequency.index,frequency.values)
plt.plot(x_new,y_smooth, color='red')
plt.axhline(y=mode, color="yellow",linestyle="--", label="Mode")
# plt.axvline(x=mean, color="pink",linestyle="--", label="Mean")
# plt.axvline(x=sdeviation, color="orange",linestyle="--", label="Standard Deviation")
# plt.axvline(x=median, color="g",linestyle="--", label="Median")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

