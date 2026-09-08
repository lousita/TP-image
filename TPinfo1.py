import numpy as np
import matplotlib.pyplot as plt

#Defaut figures matplotlib
plt.rcParams["figure.figsize"] = (4, 4)

#Exercice
#1
tableau = np.array([[(255,255,255) for i in range(91)] for k in range(91)])
plt.imshow(tableau)
plt.show()
print(tableau.itemsize)

#2
tableau[:]=255
print(tableau.shape)
plt.imshow(tableau)
plt.show()
#3
tableau[:]=(0,255,0)
plt.imshow(tableau)
plt.show()
#4
print("RGB du 1er pixel",tableau[0][0])
print("RGB du dernier pixel", tableau[-1][-1])
#5
k=0
while k<91:
    for i in range(91):
        tableau[k][i]=(0,0,255)
        tableau[i][k]=(0,0,255)
    k+=10
plt.imshow(tableau)
plt.show()
