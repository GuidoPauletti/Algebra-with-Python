# -*- coding: utf-8 -*-
"""
Created on Mon May  2 22:39:35 2022

@author: guido
"""

import numpy as np

#Datos:
    
M_f = np.array([[1, 1, 0],
                 [2, 1, -1],
                 [0, -2, -1]])

Cbe_f = np.array([[1, 0, 2],
                 [0, 1, 1],
                 [2, 1, 0]])

#primero busco la matriz de f en base BE, que va a ser igual
#al producto de la matriz de F en base EE (M_f) con la matriz de cambio
#de base C en base BE (Cbe_f). La llamamos Mbe_f 

Mbe_f= np.dot(M_f, Cbe_f)

#luego me piden obtener la matriz de f en base BB (Mbb_f), que se la puede calcular
#con el producto de la matriz de cambio "Ceb" * M_f * Cbe_f que seria igual
# a Ceb * Mbe_f

#Ceb es igual a la inversa de Cbe_f 
Mbb_f = np.dot(np.linalg.inv(Cbe_f), Mbe_f)

#por ultimo se pide calcular la matriz en base BE de la transformacion
#lineal inversa a f, que seria igual a la matriz de f en base EB y la 
#puedo calcular con el producto de Mbb_f * (inv)Ceb_f

inv_Mbe_f = np.dot(Mbb_f, np.linalg.inv(Cbe_f))

print("la matriz de f en base BE es:\n", Mbe_f,"\n",
      "la matriz de f en base B  es: \n", Mbb_f, "\n",
      "la matriz de la inversa de f en base BE es: \n", inv_Mbe_f
      )
                   

                   
                   
