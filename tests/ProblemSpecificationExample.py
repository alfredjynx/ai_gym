from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State

class ProblemSpecification(State):

    def __init__(self, op, robot, dire, esq):
        self.operator = op
        self.pos = robot
        self.direita = dire
        self.esquerda = esq
    
    def sucessors(self):
        successors = []
        # esq
        successors.append(ProblemSpecification("esq","ESQ",self.direita,self.esquerda))

        # direita
        successors.append(ProblemSpecification("dir","DIR",self.direita,self.esquerda))

        #limpar
        if self.pos == "ESQ":
            successors.append(ProblemSpecification('limpar',self.pos,self.direita,"LIMPO"))
        else:
            successors.append(ProblemSpecification('limpar',self.pos,"LIMPO",self.esquerda))
        return successors

    
    def is_goal(self): return True if self.direita == self.esquerda == "LIMPO" and self.pos == "ESQ" else False
    
    def description(self):
        return f"Operador:{self.operator}|Posição:{self.pos}|\nSujeira:\n- Direita:{self.direita}\n- Esquerda:{self.esquerda}"
    
    def cost(self):
        return 1
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        return self.operator


def main():
    print('Busca em profundidade iterativa')
    state = ProblemSpecification("","ESQ","SUJO","SUJO")
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()