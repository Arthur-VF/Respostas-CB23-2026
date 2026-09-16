from P06_3462_pilha_encadeada import PilhaEncadeada

class FilaEncadeada:
    def __init__(self):
        self.pilha_entrada = PilhaEncadeada()
        self.pilha_saida = PilhaEncadeada()

    def enfileirar(self, item):
        self.pilha_entrada.push(item)

    def desenfileirar(self):
        if self.pilha_saida.esta_vazia() == True:
            while self.pilha_entrada.esta_vazia() == False:
                item = self.pilha_entrada.pop()
                self.pilha_saida.push(item)

        if self.pilha_saida.esta_vazia() == True:
            raise IndexError("A fila está vazia")
        else:
            return self.pilha_saida.pop()

    def frente(self):
        if self.pilha_saida.esta_vazia() == True:
            while self.pilha_entrada.esta_vazia() == False:
                item = self.pilha_entrada.pop()
                self.pilha_saida.push(item)
        if self.pilha_saida.esta_vazia() == True:
            raise IndexError("A fila está vazia")     
        else:
            return self.pilha_saida.topo()

    def esta_vazia(self):
        if self.pilha_saida.esta_vazia() == True and self.pilha_entrada.esta_vazia() == True:
            return True
        else:
            return False

    def __len__(self):
        return len(self.pilha_entrada) + len(self.pilha_saida)

    def __repr__(self):
        if len(self) == 0:
            return "[]"
        else:
            string1 = "["
            pilha_aux1 = PilhaEncadeada()
            while len(self.pilha_saida) != 0:
                item = self.pilha_saida.pop()
                pilha_aux1.push(item)

            while len(self.pilha_entrada) != 0:
                item = self.pilha_entrada.pop()
                self.pilha_saida.push(item)

            while len(pilha_aux1) != 0:
                item = pilha_aux1.pop()
                self.pilha_saida.push(item)

            pilha_aux2 = PilhaEncadeada() 

            while len(self.pilha_saida) != 0:
                item = self.pilha_saida.pop()
                pilha_aux2.push(item)  
                string1 += str(item) + ", "
               
            while len(pilha_aux2) != 0:
                item = pilha_aux2.pop()
                self.pilha_saida.push(item)

            string1 = string1[:-2]    

            return string1 + "]"            
