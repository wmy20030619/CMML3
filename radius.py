import matplotlib.pyplot as plt
import numpy as np

time, rg = np.loadtxt('C:/Users/31937/Downloads/radius_of_gyration.xvg', comments=['#', '@'], usecols=(0, 1), unpack=True)

plt.plot(time, rg, lw=2, label='Radius of Gyration')
plt.xlabel('Time (ps)')
plt.ylabel('Rg (nm)')
plt.title('Protein Conformational Stability')
plt.legend()
plt.show()