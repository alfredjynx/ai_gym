from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa, BuscaLargura
from aigyminsper.search.Graph import State

class ProblemSpecification(State):

    def __init__(self, op, robot, campo, elev,dir):
        self.operator = op
        self.pos = robot
        self.campo = campo
        self.elevation = elev
        self.dir = dir
        casa = list()
        c = list()
        for i in range(10):
            c.append('LIMPO')
        for i in range(10):
            casa.append(c)
        self.linha_meta = c
        self.meta = casa
    
    def sucessors(self):
        successors = []
        # esq
        # if self.pos>0:
        #     successors.append(ProblemSpecification("esq",self.pos-1,self.campo,self.elevation,self.dir))

        # # direita
        # if self.pos<len(self.campo[self.elevation])-1:
        #     successors.append(ProblemSpecification("dir",self.pos+1,self.campo,self.elevation,self.dir))

        # # cima
        # if self.elevation>0:
        #     successors.append(ProblemSpecification('cima',self.pos,self.campo,self.elevation-1,self.dir))

        # # baixo
        # if self.elevation<len(self.campo)-1:
        #     successors.append(ProblemSpecification('baixo',self.pos,self.campo,self.elevation+1,self.dir))

        #limpar
        if self.campo[self.elevation][self.pos] == 'SUJO':
            l = self.campo
            l[self.elevation][self.pos] = 'LIMPO'
            successors.append(ProblemSpecification('limpar',self.pos,l,self.elevation,self.dir))
        
        elif self.dir!=[0,0]:
            successors.append(ProblemSpecification('andar',self.pos+self.dir[1],self.campo,self.elevation+self.dir[0],[0,0]))

        else:
            poss = [[self.elevation+1,self.pos],[self.elevation,self.pos+1],[self.elevation-1,self.pos],[self.elevation,self.pos-1]]
            estado = list()
            for pos in poss:
                if (pos[0]<0 | pos[0]==len(self.campo)) | (pos[1]<0 | pos[1]==len(self.campo[self.elevation])):
                    estado.append(False)
                else:
                    estado.append(True)

            for i in range(len(poss)):
                if self.campo[poss[i][0]][poss[i][1]] == 'SUJO' and estado[i]:
                    successors.append(ProblemSpecification('limpar',self.pos,self.campo,self.elevation,[pos[0]-self.elevation,pos[1]-self.pos]))
    
        return successors

    
    def is_goal(self): return True if self.campo == self.meta else False
    
    def description(self):
        return f"Operador:{self.operator}|Posição:{self.pos}|\nSujeira:\n- Direita:{self.pos}\n- Esquerda:{self.elevation}"
    
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
    casa = list()
    c = list()
    for i in range(10):
        c.append('SUJO')
    for i in range(10):
        casa.append(c)
    state = ProblemSpecification("Eu mesmo",0,casa,0,[0,0])
    # algorithm = BuscaProfundidadeIterativa()
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()