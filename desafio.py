#@author: Allana Capistrano de Oliveira

#leitura de arquivo csv com o pandas
import pandas as pd

#A leitura se dá em um DataFrame
doc = pd.read_csv('notas.csv')

#Tamanho Total do Documento
tamTotal = int(doc.size/doc.columns.size)

class cria:
    #Criação do DataFrame para o documento
    def criarDataFrame():
        COLUNAS = ['MATRICULA','COD_DISCIPLINA','COD_CURSO','NOTA','CARGA_HORARIA','ANO_SEMESTRE']
        data = pd.DataFrame(columns=COLUNAS)
        return data

#Classe Aluno
class Aluno:
    #Inicialização dos objetos necessários para um Aluno
    def __init__(self):
        self.mat = None
        self.cr = None
        self.documento = cria.criarDataFrame()

    #Gets e sets da classe Aluno
    def setMatricula(self,matricula):
        self.mat = matricula

    def getMatricula(self):
        return self.mat

    def setCR(self,cr):
         self.cr = cr

    def getCR(self):
        return self.cr

    def setDocumento(self,doc):
         self.documento = doc

    def getDocumento(self):
        return self.documento

    #Função que calcula CR do aluno
    def calculaCR(self,nota,totalCargaHoraria):
        cr = 0
        cr = nota/totalCargaHoraria
        return cr

    #Insere novo dado do aluno
    def inserirNovo(self, i):
        self.setDocumento(self.getDocumento().append(doc.loc[i]))

    #Insere informações do Aluno da classe Aluno e logo após insere este no conjunto de Alunos
    def insereAluno(self,aluno, alunos, mat, nota, totalCargaHoraria):
        aluno.setMatricula(mat)
        cr = aluno.calculaCR(nota,totalCargaHoraria)
        aluno.setCR(cr)
        alunos.append(aluno)
        return alunos

#Menu responsável por calcular o CR de cada aluno criando uma lista de alunos
class menuCR:
    #Cria o conjunto de alunos
    def conjuntoAluno(self,alunos,mat,ini,qtde):
        totalCargaHoraria = 0
        nota = 0
        aluno = Aluno()
        for i in range(ini,tamTotal):
            matricula = doc['MATRICULA'][i]
            if(mat == 0):
                mat = matricula
            if(matricula == mat):
                carga = doc['CARGA_HORARIA'][i]
                nota += (doc['NOTA'][i]*carga)
                totalCargaHoraria += carga
                aluno.inserirNovo(i)
            elif(matricula!=mat or i==tamTotal):
                alunos = aluno.insereAluno(aluno,alunos, mat, nota, totalCargaHoraria)
                qtde+=1
                return self.conjuntoAluno(alunos, matricula,i,qtde)
        qtde+=1
        alunos = aluno.insereAluno(aluno,alunos, mat, nota, totalCargaHoraria)
        return [qtde,alunos]

    #Responsável pela função principal de chamada
    def meuCR(self):
        alunos = []
        valor = self.conjuntoAluno(alunos,0,0,0)
        qtde = valor[0]
        alunosTotal = valor[1]
        #print("Qtde: %d" % qtde)

        print("------- O CR dos alunos é: --------")
        for aluno in alunosTotal:
            print("Matricula: %d - CR: %.2f"% (aluno.getMatricula(),aluno.getCR()))


#Classe curso responsável pelas configurações que um curso precisa
class Curso:
    #Inicialização de cada curso
    def __init__(self):
        #Cada curso precisa do seu código e do seu documento tipo DataFrame para identificação
        self.cod = None
        self.documento = cria.criarDataFrame()

    #Os gets e sets da classe Curso
    def setCodCurso(self, codCurso):
        self.cod = codCurso

    def getCodCurso(self):
        return self.cod

    def getDocumento(self):
        return self.documento

    def setDocumento(self,doc):
        self.documento = doc

    def getTamanho(self,document):
        #Tamanho Total do Documento
        return int(document.size/document.columns.size)

    #Verificar Média do curso estudado
    def verificarMedia(self):
        document = self.getDocumento()
        nota = 0
        totalCargaHoraria = 0
        tamTotal = self.getTamanho(document)
        for i in range(tamTotal):
            carga = document['CARGA_HORARIA'][i]
            nota += (document['NOTA'][i]*carga)
            totalCargaHoraria += carga

        media = nota/totalCargaHoraria
        return media

#Classe Menu responsável pelas funções que chamam o conjunto necessário
class menuCurso:
    #Verifica se o curso já está no conjunto Cursos
    def verificaCodCurso(self,cursos, codigo):
        for i in cursos:
            if(i.getCodCurso()==codigo):
                return True
        return False

    #Insere Documento ao curso que o contem
    def insereDocumento(self,cursos,codigo, num):
        for i in cursos:
            if(i.getCodCurso()==codigo):
                i.setDocumento(i.getDocumento().append(doc.loc[num]))
                return

    #Faz uma lista de Cursos para melhor contabilidade
    def arrumaACasa(self,cursos):
        qtde = 0
        for i in range(tamTotal):
            codCurso = doc['COD_CURSO'][i]
            valida = self.verificaCodCurso(cursos,codCurso)
            if(valida==False):
                curso = Curso()
                curso.setCodCurso(codCurso)
                curso.setDocumento(curso.getDocumento().append(doc.loc[i]))
                qtde += 1
                cursos.append(curso)
            else:
                self.insereDocumento(cursos,codCurso,i)

        return [qtde,cursos]

    #Chama as funções para realizar objetivos
    def meuCurso(self):
        cursar = []
        valor = self.arrumaACasa(cursar)
        qtde  = valor[0]
        cursos = valor[1]
        #print("Qtde: %d" % qtde)

        print("-----------------------------------")
        print("----- Média de CR dos cursos ------")
        print("-----------------------------------")

        for i in cursos:
            indicesNovos = i.getDocumento().reset_index(drop=True)
            i.setDocumento(indicesNovos)
            media  = i.verificarMedia()

            print("Código do curso: %d - Média de Cr: %.2f "% (i.getCodCurso(),media))

#Main do nosso programa
def main():
    meu_CR = menuCR()
    meu_CR.meuCR()

    meu_Curso = menuCurso()
    meu_Curso.meuCurso()

main()
