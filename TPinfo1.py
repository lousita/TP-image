""""
Eléonore Veyron
"""
import numpy as np
import matplotlib.pyplot as plt

#Defaut figures matplotlib
plt.rcParams["figure.figsize"] = (4, 4)

"""     Exercice       """

#1 Création tableau
tableau = np.array([[(255,255,255) for i in range(91)] for k in range(91)])
plt.imshow(tableau)
plt.show()
print(tableau.itemsize)

#2 Changement de couleur (blanc)
tableau[:]=255
print(tableau.shape)
plt.imshow(tableau)
plt.show()
#3 idem en vert
tableau[:]=(0,255,0)
plt.imshow(tableau)
plt.show()
#4
print("RGB du 1er pixel",tableau[0][0])
print("RGB du dernier pixel", tableau[-1][-1])
#5
k=0 #compteur
while k<91: 
    for i in range(91):
        tableau[k][i]=(0,0,255)
        tableau[i][k]=(0,0,255)
    k+=10
plt.imshow(tableau)
plt.show()

"""     Lecture d'une image en couleur     """
#1
im = plt.imread("data/les-mines.jpg")
#2
if not im.flags.writeable:
    im=im.copy()
#3
plt.imshow(im)
plt.show()
#4
print("type de l'objet", type(im))
#5
print("Dimension", im.ndim)
#6
print("Taille", im.shape[:2]) #hauteur, largeur
#7
print("Nb octet", im.itemsize) #octet par valeur
#8
print("Type pixel", im.dtype)
#9
print(im.max(), im.min()) #valeur max, min pixels
#10
im2=im[:10,:10]
plt.imshow(im2)
plt.show()

""" Accès à des parties d'image """
#1
im = plt.imread("data/les-mines.jpg")
#2
liste=[2,5,10,20]
for k in liste:
    im3=im[::k,::k]
    plt.imshow(im3)
    plt.show()
#3
x0= 533//2
y0=800//2
for (l,c) in ((10,20),(100,200)):
    x1=x0 - l//2
    x2=x0 + l//2 +1
    y1=y0 - c//2
    y2= y0 + c//2 +1
    im4=im[x1:x2,y1:y2]
    plt.imshow(im4)
    plt.show()

""" Canaux RGB de l'image   """
#1
im = plt.imread("data/les-mines.jpg")
#2 et 3 Création de 3 images issus des couleurs 
rouge=im[::,::,0]
vert=im[::,::,1]
bleu=im[::,::,2]
plt.imshow(rouge,cmap ='Reds')
plt.show()
plt.imshow(vert, cmap='Greens')
plt.show()
plt.imshow(bleu, cmap='Blues')
plt.show()
#5
#Carré rose en bas à droite
copie=im.copy()
copie[-200:,-200:]= (219, 112, 147)
plt.imshow(copie)
plt.show()
#Carré rayé rouge en bas à droite
copie2=im.copy()
copie2[-200:,-200]=(255,255,255)
copie2[-200::2,-200:,0]=255
copie2[-200::2,-200:,1]=0
copie2[-200::2,-200:,2]=0
plt.imshow(copie2)
plt.show()
#6
plt.imshow(copie2[-200:,-200:])
plt.show()

"""     Transparence des images     """

#1
im = plt.imread("data/les-mines.jpg")
#2 Création du 4e cannal
im4=np.empty((533,800,4), dtype=im.dtype)
im4[:,:,:3]=im
im4[:,:,3]=128
plt.imshow(im4)
plt.show()

""" Image en niveaux de gris en float   """
#1
im=plt.imread("data/les-mines.jpg")
#2
im_float=im/255
plt.imshow(im_float)
plt.show()
#3
gris_moyenne=im_float.mean(axis=2)
plt.imshow(gris_moyenne,cmap='gray')
plt.show()

gris2= 0.299*im_float[:,:,0] + 0.587*im_float[:,:,1]+ 0.144*im_float[:,:,2]
plt.imshow(gris2, cmap='gray')
plt.show()
#4
gris3=gris_moyenne**2
plt.imshow(gris3,cmap="gray")
plt.show()
