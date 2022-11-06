#!python
class Termco:
    erro = '\033[91m'  # vermelho
    certo = '\033[0m'
    verde = '\033[1;32m'
    azul = '\033[1;34m'


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        tarefaspendentes = []

        for tarefa in self.tarefas:
            if tarefa.feito:
                pass

            else:
                tarefaspendentes.append(tarefa)

        return len(tarefaspendentes), tarefaspendentes

    def procurar(self, descricao):
        for tarefa in self.tarefas:
            if tarefa.descricao == descricao:
                return tarefa

    def __str__(self):
        return f'projeto {self.nome}, tarefas pendentes -> {self.pendentes()}'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []

        if self.feito:
            status.append('Tarefa Concluida')
            return f'{Termco.verde}{self.descricao} -> {status}{Termco.certo}'

        else:
            status.append('Tarefa Pendente')
            return f'{Termco.erro}{self.descricao} -> {status}{Termco.certo}'
        


listasegunda = ['CASTRO-FISICA', 'DALTRO-BIOLOGIA', 'PIMENTA-MATEMATICA',
                'BORIS-GEOGRAFIA', 'JAPA-QUIMICA', 'BORELLA-BIOLOGIA',
                'LG-MATEMATICA', 'THIAGO-HISTORIA', 'ALFREDO-GEOGRAFIA', 'JERUSA-QUIMICA',
                'BRANCALHAO-FISICA', 'PAULO-BIOLOGIA']

listaterca = ['MARCIO-MATEMATICA', 'NORONHA-PORTUGUES', 'ZELUCIO-BIOLOGIA',
              'ALAOR-GEOGRAFIA', 'GABRIEL-LITERATURA', 'LG-MATEMATICA']

listaquarta = ['RENATO-QUIMICA', 'THIAGO-HISTORIA', 'KLEBER-MATEMATICA',
               'TARCILIO-HISTORIA', 'MALUF-FISICA', 'PHILIPPE-FISICA']

listaquinta = ['BETO-HISTORIA', 'KLEBER-MATEMATICA', 'ZELUCIO-BIOLOGIA',
               'FARAONI-HISTORIA', 'DALTRO-BIOLOGIA', 'RODRIGO-GEOGRAFIA']

listasexta = ['RAPHAEL-PORTUGUES', 'ZEHUMBERTO-QUIMICA', 'CASTRO-FISICA',
              'LUCIO-SOCIOLOGIA', 'DANILO-FILOSOFIA', 'PROSA-QUIMICA', 'PIMENTA-MATEMATICA']


def main():
    dia = input('Que dia é hoje? ->')

    gabarito = Projeto('Tarefas Gabarito')

    def concluir():
        while True:
            concluida = input('Digite as tarefas concluidas (uma por vez), (digite end para parar)').upper()
            if concluida != 'END':
                gabarito.procurar(concluida).concluir()

            else:
                print(f'{Termco.azul}-=-{Termco.certo}'*60)
                print(f'{Termco.azul}LISTA DAS TAREFAS{Termco.certo}')
                print(f'{Termco.azul}-=-{Termco.certo}'*60)
                for tarefa in gabarito:
                    print(f'{tarefa}')
                break


    if 'segunda' in dia:
        for c in range(len(listasegunda)):
            gabarito.add(listasegunda[c])
        for tarefa in gabarito:
            print(
                f'{tarefa}'
            )
        print(f'{Termco.azul}={Termco.certo}'*60)
        concluir()


    if 'terca' in dia or 'terça' in dia:
        for c in range(len(listaterca)):
            gabarito.add(listaterca[c])
        for tarefa in gabarito:
            print(
                f'{tarefa}'
            )
        print(f'{Termco.azul}={Termco.certo}'*60)
        concluir()
        
    if 'quarta' in dia:
        for c in range(len(listaquarta)):
            gabarito.add(listaquarta[c])
        for tarefa in gabarito:
            print(
                f'{tarefa}'
            )
        print(f'{Termco.azul}={Termco.certo}'*60)
        concluir()

    if 'quinta' in dia:
        for c in range(len(listaquinta)):
            gabarito.add(listaquinta[c])
        for tarefa in gabarito:
            print(
                f'{tarefa}'
            )
        print(f'{Termco.azul}={Termco.certo}'*60)
        concluir()

    if 'sexta' in dia:
        for c in range(len(listasexta)):
            gabarito.add(listasexta[c])
        for tarefa in gabarito:
            print(
                f'{tarefa}'
            )
        print(f'{Termco.azul}={Termco.certo}'*60)
        concluir()



if __name__ == '__main__':
    main()
