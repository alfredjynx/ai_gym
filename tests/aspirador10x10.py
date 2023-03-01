from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa, BuscaLargura, BuscaProfundidade
from aigyminsper.search.Graph import State
import copy

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

        if self.campo[self.elevation][self.pos] == 'SUJO':
            l = copy.deepcopy(self.campo)
            l[self.elevation][self.pos] = 'LIMPO'
            successors.append(ProblemSpecification('limpar',self.pos,l,self.elevation,self.dir))
        
        else:
            # esq
            if self.pos>0:
                successors.append(ProblemSpecification("esq",self.pos-1,self.campo,self.elevation,self.dir))

            # direita
            if self.pos<len(self.campo[self.elevation])-1:
                successors.append(ProblemSpecification("dir",self.pos+1,self.campo,self.elevation,self.dir))

            # cima
            if self.elevation>0:
                successors.append(ProblemSpecification('cima',self.pos,self.campo,self.elevation-1,self.dir))

            # baixo
            if self.elevation<len(self.campo)-1:
                successors.append(ProblemSpecification('baixo',self.pos,self.campo,self.elevation+1,self.dir))

        
        
        return successors
    
    # def sucessors(self):
    #     successors = []
    #     # # esq
    #     # if self.pos>0:
    #     #     successors.append(ProblemSpecification("esq",self.pos-1,self.campo,self.elevation,self.dir))

    #     # # # direita
    #     # if self.pos<len(self.campo[self.elevation])-1:
    #     #     successors.append(ProblemSpecification("dir",self.pos+1,self.campo,self.elevation,self.dir))

    #     # # # cima
    #     # if self.elevation>0:
    #     #     successors.append(ProblemSpecification('cima',self.pos,self.campo,self.elevation-1,self.dir))

    #     # # # baixo
    #     # if self.elevation<len(self.campo)-1:
    #     #     successors.append(ProblemSpecification('baixo',self.pos,self.campo,self.elevation+1,self.dir))

    #     #limpar
    #     if self.campo[self.elevation][self.pos] == 'SUJO':
    #         l = copy.deepcopy(self.campo)
    #         l[self.elevation][self.pos] = 'LIMPO'
    #         successors.append(ProblemSpecification('limpar',self.pos,l,self.elevation,self.dir))
    #         # print('LIMPAR')
        
    #     elif self.dir!=[0,0]:
    #         successors.append(ProblemSpecification('andar',self.pos+self.dir[1],self.campo,self.elevation+self.dir[0],[0,0]))
    #         # print('ANDAR')

    #     else:
    #         val = self.pontos_sujos(self.elevation,self.pos)

    #         if val!=False:
    #             successors.append(val)
    #             # print('SUJO AO LADO')
    #         else:
    #             poss = [[self.elevation+1,self.pos],[self.elevation,self.pos+1],[self.elevation-1,self.pos],[self.elevation,self.pos-1]]
    #             for d in poss:
    #                 if self.pontos_sujos(d[0],d[1])!=False:
    #                     successors.append(self.pontos_sujos(d[0],d[1]))
    #                     break
    #             # print('DIRECIONAR PRO MAIS PRÓXIMO')
        
    #     # print(self.campo)
    
    #     return successors

    # def pontos_sujos(self,elevation,pos):
    #     poss = [[elevation+1,pos],[elevation,pos+1],[elevation-1,pos],[elevation,pos-1]]
    #     estado = list()
    #     for p in poss:
    #         if (p[0]<0 | p[0]>=len(self.campo)) | (p[1]<0 | p[1]>=len(self.campo[elevation])):
    #             estado.append(False)
    #         else:
    #             estado.append(True)
    #     direcao = ['cima','direita','baixo','esquerda']
    #     for i in range(len(poss)):
    #         if self.campo[poss[i][0]][poss[i][1]] == 'SUJO' and estado[i]:
    #             return (ProblemSpecification(direcao[i],self.pos,self.campo,elevation,[poss[i][0]-elevation,poss[i][1]-pos]))
        
    #     return False

    
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
    print('Busca em profundidade')
    casa = list()
    c = list()
    for i in range(10):
        c.append('SUJO')
    for i in range(10):
        casa.append(c)
    state = ProblemSpecification("Eu mesmo",0,casa,0,[0,0])
    algorithm = BuscaProfundidade()
    # algorithm = BuscaLargura()
    result = algorithm.search(state,20)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()