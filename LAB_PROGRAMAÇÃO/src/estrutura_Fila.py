'''
Created on 30/11/2017

@author: Rodrigo
'''
from objeto_lista_encadeada import lista
class fila(lista):
    def empilha_fim(self,dado):
        self.inserir_fim(dado)
        
    def desempilha_inicio(self):
        return self.remover_inicio()