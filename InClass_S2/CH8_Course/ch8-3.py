import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-100,100,10)
y = x**2
plt.title("My-Figure")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y,color="c",linestyle="--", marker="o",linewidth="1")
plt.show()