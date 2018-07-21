import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['DejaVu Sans']

keys = mpl.rcParams.keys()
for key in keys:
    if key == 
    print(key)
x = np.linspace(-1, 1, 50)
print(x)
y1 = 2 * x + 1
y2 = 2 ** x + 1
#plt.figure()
plt.plot(x, y1)
#plt.figure()
plt.plot(x, y2)
# plt.xlabel("x轴")
# plt.ylabel("y轴")
plt.show()
