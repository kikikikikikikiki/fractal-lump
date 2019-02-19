import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fftp



t = np.linspace(0, 2*np.pi, 1000, endpoint=True)
f = 1.0 # Frequency in Hz
A = 100.0 # Amplitude in Unit
s = A * (np.sin(2*np.pi*f*t)+ np.sin(3*(2*np.pi*f*t))/3+np.sin(5*(2*np.pi*f*t))/5) # Signal

plt.plot(t,s)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.show()
