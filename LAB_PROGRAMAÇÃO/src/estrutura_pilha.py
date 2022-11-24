'''
Created on 30/11/2017

@author: Rodrigo
'''
from objeto_lista_encadeada import lista

class Pilha(lista):
    def empilha(self,dado):
        self.inserir_inicio(dado)
        
    def desempilha(self):
        return self.remover_inicio()