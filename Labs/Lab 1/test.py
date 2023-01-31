import matplotlib.pyplot as plt
import numpy as np

x = np.arange(start=1.920, stop=2.080, step=0.001)
p = lambda x: (x - 2)**9

plt.plot(x, p(x))
plt.title("Plot of P(X) with Expression") 
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
plt.savefig('test2.png', bbox_inches='tight')

