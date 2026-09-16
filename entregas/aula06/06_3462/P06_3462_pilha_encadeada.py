class No:
    def __init__(self, dado):
            self.dado = dado
            self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def push(self, item):
        novo_no = No(item)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self.tamanho += 1

    def pop(self):
         try:
              item_removido = self.cabeca.dado
              self.cabeca = self.cabeca.proximo
              self.tamanho -= 1
              return item_removido

         except AttributeError:
              raise IndexError("A pilha está vazia")
             

    def topo(self):
         try:
            return self.cabeca.dado
         except AttributeError:
            raise IndexError("A pilha está vazia")
 

    def esta_vazia(self):
         if self.tamanho == 0:
              return True
         else:
              return False

    def __len__(self):
         return self.tamanho

    def __repr__(self):
        if self.cabeca == None:
            return "[]"
        else: 
            string1 = "["
            elemento_atual = self.cabeca
            while elemento_atual is not None:
                string1 += str(elemento_atual.dado)
                if elemento_atual.proximo != None:
                    string1 += ", "     
                elemento_atual = elemento_atual.proximo
            string1 += "]"
            return string1     