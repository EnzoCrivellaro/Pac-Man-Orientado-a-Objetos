#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import floor
from turtle import *
import numpy as np

"""
Dica: carregue a matriz no construtor da classe Labirinto via chamada de método
"""
class Labirinto:
    
    def __init__(self, dimensao_da_matriz, tam_celula):
        self._tam_celula = tam_celula
        self._dimensao_da_matriz = dimensao_da_matriz

    def obter_vizinhos(self, lin, col):
        """ Retorna uma lista com os vizinhos (cima, baixo, esquerda, direita) da célula que são caminho.
            As coordenadas (lin, col) são da matriz. Por exemplo, na matriz a seguir:
            [[ 0  1  0 ]
             [ 1  1  0 ]
             [ 0  0  1 ]]
             Os vizinhos do elemento central (1,1) incluem o de cima (0,1) e o da
             esquerda (1,0). O vizinho de baixo (2,1) e o da direita (1,2) não são
             incluídos porque estão com valor 0. Nem os elementos da diagonal porque
             não entram na definição de vizinhança adotada aqui.
        """
        self._lst = []
        if self._matriz[lin-1][col] == 1:
            self._lst.append((lin-1, col))
        
        if self._matriz[lin][col-1] == 1:
            self._lst.append((lin, col-1))
        
        if self._matriz[lin+1][col] == 1:
            self._lst.append((lin+1, col))
        
        if self._matriz[lin][col+1] == 1:
            self._lst.append((lin, col+1))
        
        return self._lst

    def ler_matriz_fixa(self):
        """ Retorna uma matriz fixa """
        return [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]


    def ler_matriz_aleatoria(self, dim):
        """ Retorna uma matriz quadrada na dimensão especificada com números
            aleatórios (0's e 1's)
            Dica: utilize numpy.random.randint()
        """
        self._dimensao_da_matriz = dim
        return np.random.randint(2,size=(self._dimensao_da_matriz,self._dimensao_da_matriz))


    def criar_labirinto(self, p1=500, p2=500, p3=370, p4=0):
        """ Cria o gráfico do labirinto baseado nos valores da matriz """
        tracer(False)
        hideturtle()
        bgcolor('black')
        setup(p1, p2, p3, p4)
        
        self._matriz = np.random.randint(2,size=(self._dimensao_da_matriz,self._dimensao_da_matriz))

        # Para cada linha da matriz
        for lin in range(self._dimensao_da_matriz):
            # Para cada coluna da matriz
            for col in range(self._dimensao_da_matriz):
                # Testa se a coordenada da matriz (lin, col) é caminho (=1)
                if (self._matriz[lin][col] == 1):
                    # Em caso positivo, transforma em coordenada Turtle.
                    # Atenção: Numa coordenada Turtle (x,y), o eixo x refere-se à coluna e o eixo y à linha
                    # Numa coordenada da matriz (lin, col), o primeiro elemento é a linha e o segundo a coluna
                    self._x, self._y = self.em_coord_turtle(lin, col)
                    # Pinta a celula na posição (x,y) com a cor especificada
                    self.desenhar_celula(self._x, self._y, 'blue')

                    self.desenhar_pastilha(self._x, self._y, 'white')

    def desenhar_celula(self, x, y, cor):
        """ Dada uma coordenada (x, y) do Turtle, desenha um quadrado (célula) na posição """
        self._x = x
        self._y = y
        self._cor = cor
        color(cor)
        up()
        goto(self._x,self._y)
        down()
        begin_fill()
        for _ in range(4):
            forward(self._tam_celula)
            left(90)
        end_fill()
        up()

    def chao_da_celula(self, x, y):
        """ Dadas coordenadas do Turtle (x,y), retorna as coordenadas do início de uma célula.
            Por exemplo, na celula da origem com tamanho 20, a coordenada Turtle (10,10)
            representa o meio da célula. A chamada de função 'chao_da_celula(10, 10)' retorna
            as coordenadas de início dessa célula (0,0)
            Dica: para entender, veja o exemplo da função: 'uso_do_floor()''
        """
        self._x = x
        self._y = y
        
        self._chao_x = int(floor(self._x, self._tam_celula))
        self._chao_y = int(floor(self._y, self._tam_celula))
        return self._chao_x, self._chao_y

    def em_coord_turtle(self, lin, col):
        """ Dados os índices da matriz (lin, col), retorna as coordenadas do Turtle correspondentes.
            Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20,
            a chamada de função 'em_coord_turtle(0,0)' deve retornar (-200,200) e a
            chamada de função 'em_coord_turtle(10,10)' deve retornar (0,0)
        """
        self._lin = lin
        self._col = col
        
        self._meio = self._dimensao_da_matriz // 2
        self._x = (self._col - self._meio) * self._tam_celula
        self._y = (self._meio - self._lin) * self._tam_celula
        return self._x, self._y

    def em_coord_matriz(self, x, y):
        """ Dada uma coordenada do Turtle (x,y), retorna os índices correspondentes da matriz
            Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20,
            a chamada de função 'em_coord_matriz(-200, 200)' deve retornar (0,0) e a
            chamada de função 'em_coord_matriz(0, 0)' deve retornar (10,10).
            Dica: utilize a função 'chao_da_celula(x, y)'
        
        """
        self._x = x
        self._y = y
        
        self._x, self._y = self.chao_da_celula(self._x, self._y)
        self._meio = self._dimensao_da_matriz // 2
        self._lin = int(self._meio - (self._y / self._tam_celula))
        self._col = int(self._meio + (self._x / self._tam_celula))
        return self._lin, self._col

    def cel_aleatoria(self):
        """
        """
        self._i, self._j = np.random.randint(self._dimensao_da_matriz, size=(2))
        while (not self.eh_caminho(self._i, self._j)):
            self._i, self._j = np.random.randint(self._dimensao_da_matriz, size=(2))
        return self._i, self._j

    def eh_caminho(self, lin, col):
        """ Dada uma matriz quadrada, retorna True quando (lin, col) == 1 e
            False caso contrário.
            Por exemplo, na matriz a seguir:
            [[ 1  0  0 ]
             [ 0  1  0 ]
             [ 0  0  1 ]]
            a chamada de função 'eh_caminho(0,0)' retorna True e
            a chamada de função 'eh_caminho(0,1)' retorna False
        """
        return self._matriz[lin][col] == 1

    def desenhar_pastilha(self, x, y, cor):
        """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
            para representar a pastilha
        """
        self._x = x
        self._y = y
        self._cor = cor
        self._c = self._tam_celula // 2
        
        up()
        goto(self._x + self._c,self._y + self._c)
        down()
        dot(3, self._cor)

