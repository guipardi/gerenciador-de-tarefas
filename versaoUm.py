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

        return len(tarefaspendentes)

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

        else:
            status.append('Tarefa Pendente')

        return f'{self.descricao} -> {status}'

    

if __name__ == '__main__':
    gabarito = Projeto('Tarefas Gabarito')

    gabarito.add('Castro-Fisica')
    gabarito.add('Danilo-Filosofia')
    gabarito.add('Pimenta-Matematica')
    gabarito.add('Prosa-Quimica')

    gabarito.procurar('Prosa-Quimica').concluir()
    gabarito.procurar('Danilo-Filosofia').concluir()


    print(gabarito)
    for tarefa in gabarito:
        print(f'{tarefa}')
