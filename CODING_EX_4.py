#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Estimador:

    def __init__(self,x,y):
        
        import numpy as np
        import math as mt
        
        self.vetor_x = np.array(x)
        self.vetor_y = np.array(y) 

        #Realiza simulação com n=100.000 para achar uma aproximação do sup f(θ)

        self.supf=mt.gamma(sum(x+y))/np.prod([mt.gamma(x+y) for x,y in zip(x,y) ])*max([np.prod(p) 
                     for p in list(map(lambda theta:[pow(theta[i],x[i]+y[i]-1) for i in range(len(x))],[np.random.dirichlet(np.array(x)+np.array(y)-1) 
                                                                                                      for i in range(100000)]))])
        #Define o número de bins
        self.bins=np.arange(start=0,stop=self.supf,step=self.supf/39)
        
        #Simulando n pontos distribuídos pela Dirchlet correspondente
        dirch_pontos=mt.gamma(sum(x+y))/np.prod([mt.gamma(x+y) for x,y in zip(x,y) ])*np.array([np.prod(p) 
                     for p in list(map(lambda theta:[pow(theta[i],x[i]+y[i]-1) for i in range(len(x))],[np.random.dirichlet(np.array(x)+np.array(y)-1) 
                                                                                                      for i in range(22691)]))])
        
        #Calculando a proporção de pontos que cairam nos bins
        self.prop=[sum(np.digitize(dirch_pontos,self.bins)==b)/22691 for b in np.unique(np.digitize(dirch_pontos, self.bins))]
    
    def U(self,v):

        import numpy as np
        
        #Retorna 1 se v maior que sup f(θ)
        if v>self.supf:
            return 1
        #Retorna 0 se v=0
        elif v==0:
            return 0
        else:
            #Obtem o extremo interior do bin
            pos = np.digitize(v,self.bins)-1
            #Calcula a base do retangulo [inf bin_i,v] e multiplica pela proporção de pontos que caíram no bin
            val = (v-self.bins[pos])*self.prop[pos]
        #Retorna a estimativa U(v)
        return sum(self.prop[0:pos])+val
