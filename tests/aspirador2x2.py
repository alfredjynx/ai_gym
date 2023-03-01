from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa, BuscaProfundidade, BuscaLargura
from aigyminsper.search.Graph import State

class ProblemSpecification(State):

    def __init__(self, op, robot, dire, esq, elev):
        self.operator = op
        self.pos = robot
        self.direita = dire
        self.esquerda = esq
        self.elevation = elev
    
    def sucessors(self):
        successors = []
        # esq
        successors.append(ProblemSpecification("esq","ESQ",self.direita,self.esquerda,self.elevation))

        # direita
        successors.append(ProblemSpecification("dir","DIR",self.direita,self.esquerda,self.elevation))

        # cima
        successors.append(ProblemSpecification('cima',self.pos,self.direita,self.esquerda,0))

        # baixo
        successors.append(ProblemSpecification('baixo',self.pos,self.direita,self.esquerda,1))

        #limpar
        if self.elevation:
            if self.esquerda[1] == self.direita[1] == 'LIMPO':
                successors.append(ProblemSpecification('cima',self.pos,self.direita,self.esquerda,0))
            else:
                if self.pos == "ESQ":
                    successors.append(ProblemSpecification('limpar',self.pos,self.direita,[self.esquerda[0],'LIMPO'],self.elevation))
                elif self.pos == "DIR":
                    successors.append(ProblemSpecification('limpar',self.pos,[self.direita[0],'LIMPO'],self.esquerda,self.elevation))
        else:
            if self.esquerda[0] == self.direita[0] == 'LIMPO':
                successors.append(ProblemSpecification('baixo',self.pos,self.direita,self.esquerda,1))
            else:
                if self.pos == "ESQ":
                    successors.append(ProblemSpecification('limpar',self.pos,self.direita,['LIMPO',self.esquerda[1]],self.elevation))
                else:
                    successors.append(ProblemSpecification('limpar',self.pos,['LIMPO',self.direita[1]],self.esquerda,self.elevation))
        return successors

    
    def is_goal(self): return True if self.direita == self.esquerda == ["LIMPO","LIMPO"] else False
    
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
    state = ProblemSpecification("","ESQ",["SUJO","SUJO"],["SUJO","SUJO"],0)
    algorithm = BuscaProfundidadeIterativa()
    algorithm = BuscaProfundidade()
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()