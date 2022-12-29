# Bibliotecas necessárias
import datetime
import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user='user',
    password='password',
    host='host',
    database='database'
)
cursor = cnx.cursor()

# Classe Agenda
class Agenda:
    def __init__(self, data, horario_inicio, horario_fim):
        self.data = data
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim

# Classe Campo
class Campo:
    def __init__(self, nome, endereco, valor_hora):
        self.nome = nome
        self.endereco = endereco
        self.valor_hora = valor_hora
        self.agenda = []

    # Método para adicionar horários à agenda do campo
    def adicionar_horario(self, data, horario_inicio, horario_fim):
        novo_horario = Agenda(data, horario_inicio, horario_fim)
        self.agenda.append(novo_horario)

# Classe CampoCerto
class CampoCerto:
    def __init__(self):
        self.campos = []

    # Método para adicionar um novo campo
    def adicionar_campo(self, nome, endereco, valor_hora):
        novo_campo = Campo(nome, endereco, valor_hora)
        self.campos.append(nome, endereco, valor_hora)

    # Método para listar todos os campos disponíveis para aluguel
    def listar_campos(self):
        for campo in self.campos:
            print(f'Campo: {campo.nome} - Endereço: {campo.endereco} - Valor/hora: R${campo.valor_hora:.2f}')

    # Método para alugar um campo
    def alugar_campo(self, nome_campo, data, horario_inicio, horario_fim):
        # Verificar se o campo existe
        campo_encontrado = False
        for campo in self.campos:
            if campo.nome == nome_campo:
                campo_encontrado = True
                # Verificar disponibilidade do campo no horário solicitado
                horario_disponivel = True
                for horario in campo.agenda:
                    if horario.data == data and (horario_inicio >= horario.horario_inicio and horario_inicio < horario.horario_fim) or (horario_fim > horario.horario_inicio and horario_fim <= horario.horario_fim):
                        horario_disponivel = False
                        break
                if horario_disponivel:
                    # Adicionar horário à agenda do campo
                    campo.adicionar_horario(data, horario_inicio, horario_fim)
                    print(f'Campo "{campo.nome}" alugado com sucesso!')
