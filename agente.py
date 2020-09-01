#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *

class Agente:

    def __init__(self, tam_agente, tam_celula):
        
        self._tam_celula = tam_celula
        self._tam_agente = tam_agente
    
    def desenhar_agente(self, x, y, cor):
        """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
            para representar o agente (i.e., pacman, fantasmas)
        """
        self._c = self._tam_celula // 2
        self._x = x
        self._y = y
        self._cor = cor
        
        up()
        goto(self._x + self._c,self._y + self._c)
        down()
        dot(self._tam_agente, self._cor)


# In[ ]:




