import matplotlib.pyplot as plt
import numpy as np

x =np.arange(1,10)



y1 = x+106
y2 = x+103
y3 = x+104


plt.plot(x,y1,color='red',label='1-2')
plt.plot(x,y2,color='blue',label='2-3')
plt.plot(x,y3,color='orange',label='4-5')

plt.xlabel('hours studied')
plt.ylabel('Average mark Achieved')
plt.title('Relationship between  Hours spend studying and Average Mark')
plt.grid(True)
plt.legend()
plt.show()

