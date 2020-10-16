from Vertice import Vertice
from Aresta import Aresta

class Grafo:

    def __init__(self):
        self.__reset()
        self.lerArquivo("arquivos-teste/agm_tiny_aresta.net")

    def __reset(self):
        self.vertices = []
        self.carregado = False

    def mostrarGrafo(self):
        self.__validarSeFoiCarregado()
        for v in self.vertices:
            print(str(v.numero) + ": " + ", ".join(map(lambda r: str(r.obterOutraParte(v).numero), v.arestas.values())))

    def lerArquivo(self, arquivo):
        self.__reset()
        f = open(arquivo, "r", encoding='utf-8')
        linhas = f.readlines()
        f.close()
        self.__lerVertices(linhas)
        self.__lerArestas(linhas)
        self.carregado = True

    def __validarSeFoiCarregado(self):
        if not self.carregado:
            raise Exception("Nenhum arquivo foi carregado! Primeiro carregue um arquivo para poder executar operações no grafo")

    def __lerVertices(self, linhas):
        self.numeroDeVertices = int(linhas[0].split(" ")[1])
        for i in range(1, self.numeroDeVertices + 1):
            linha = linhas[i]
            posicaoEspaco = linha.index(" ")
            numeroVertice = int(linha[0:posicaoEspaco])
            posicaoInicioRotulo = posicaoEspaco + 2
            posicaoFimRotulo = len(linha) - 2
            rotulo = linha[posicaoInicioRotulo:posicaoFimRotulo]
            self.vertices.append(Vertice(numeroVertice, rotulo))


    def __lerArestas(self, linhas):
        self.numeroDeArestas = 0
        for i in range(self.numeroDeVertices + 2, len(linhas)):
            valores = linhas[i].split(" ")

            v1 = self.vertices[int(valores[0]) - 1]
            v2 = self.vertices[int(valores[1]) - 1]
            peso = 1
            if (len(valores) >= 3):
                peso = float(valores[2])

            # visando economizar memória, por ser um grafo não dirigido,
            # criamos uma única vez a representação da relação e adicionamos ela
            # em ambos os vértices
            aresta = Aresta(v1, v2, peso)
            v1.adicionarAresta(aresta)
            v2.adicionarAresta(aresta)

            self.numeroDeArestas = self.numeroDeArestas + 1
