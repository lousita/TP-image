import numpy as np
import matplotlib.pyplot as plt

#Defaut figures matplotlib
plt.rcParams["figure.figsize"] = (4, 4)

#Exercice
#1
tableau = np.array([[(255,255,255) for i in range(91)] for k in range(91)])
plt.imshow(tableau)
plt.show
print(tableau.itemsize)

#2
tableau[:]=0
print(tableau.shape)

#3
