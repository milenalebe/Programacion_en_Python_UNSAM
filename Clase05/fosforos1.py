# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:29:54 2021

@author: meleg
"""
def buscar_p_elemento(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def buscar_u_elemento(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            #break    # y salimos del ciclo
    return pos

def buscar_n_elemento(lista, e):
    '''Cantidad de veces del elemento en la lista.
    '''
    contador = 0  # comenzamos suponiendo que e no está
    for z in lista: # recorremos la lista
        if z == e:   # si encontramos a e
            contador+= 1  # incremento el contador
    return contador

 # buscar_n_elemento([1, 4, 54, 3, 0, 1], 44)
 

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0]# Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e>m:
            m=e
    return m

def invertir_lista(lista):
    invertida = []
    for e in lista[::-1]: # Recorro la lista al reves
        invertida.append(e)  #agrego el elemento e al principio de la lista invertida
    return invertida


            
def propagar(lista):
    lista_propagada=[]
    pos_1=buscar_p_elemento(lista, 1)
    pos_quem=buscar_p_elemento(lista, -1)
    if pos_1<0:
        lista_propagada+=lista
    elif pos_quem<0:
        for i in range (len(lista)):
            lista_propagada.append(1)    
    else: 
        sub_lista=lista[:pos_quem+1]
        # print(sub_lista)
        lista_propagada+=sub_lista
        for i in range(pos_quem+1 , pos_1+1):
            lista_propagada.append(1)
        pos_quem=buscar_p_elemento(lista[pos_1+1 : ] ,-1)
        # print('posc quemado',pos_quem)
        if pos_quem>=0:
            for i in range(pos_quem):
                # print('itero:',i)
                lista_propagada.append(1)
                # print(lista_propagada)
            lista_propagada.append(-1)
            cola_lista=lista[pos_quem+pos_1+2: ]
            # print('cola',cola_lista)
            # print('propago cola:', propagar(cola_lista))
            lista_propagada+=propagar(cola_lista)
        else:   
            for i in range(pos_1,len(lista)-1):
                lista_propagada.append(1)
                # print('itero 2:',i)
  
    return lista_propagada     
        

print(propagar([0,1,-1,0,0,1,-1,0,0]))