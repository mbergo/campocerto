# Bibliotecas necessárias
from flask import Flask, render_template, request
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
        self.campos.append(novo_campo)

    # Método para listar todos os campos disponíveis para aluguel
    def listar_campos(self):
        campos_disponiveis = []
        for campo in self.campos:
            campos_disponiveis.append({'nome': campo.nome, 'endereco': campo.endereco, 'valor_hora': campo.valor_hora})
        return campos_disponiveis

    # Método para alugar um campo
    def alugar_campo(self, nome_campo, data, horario_inicio, horario_fim):
        # Verificar se o campo existe
        campo_encontrado = False
        for campo in self.campos:
            if campo.nome == nome_campo:
                campo_encontrado = True
                break

                # Método para pesquisar campos disponíveis por horário
    def pesquisar_horario(self, data, horario_inicio, horario_fim):
        campos_disponiveis = []
        for campo in self.campos:
            horario_disponivel = True
            for horario in campo.agenda:
                if horario.data == data and (horario_inicio >= horario.horario_inicio and horario_inicio < horario.horario_fim) or (horario_fim > horario.horario_inicio and horario_fim <= horario.horario_fim):
                    horario_disponivel = False
                    break
            if horario_disponivel:
                campos_disponiveis.append({'nome': campo.nome, 'endereco': campo.endereco, 'valor_hora': campo.valor_hora})
        return campos_disponiveis

# Instância da classe CampoCerto
campos_certo = CampoCerto()

# Adicionar alguns campos de exemplo
campos_certo.adicionar_campo('Campo 1', 'Endereço 1', 50)
campos_certo.adicionar_campo('Campo 2', 'Endereço 2', 60)
campos_certo.adicionar_campo('Campo 3', 'Endereço 3', 70)

# Criar a aplicação Flask
app = Flask(__name__)

# Rotas da aplicação

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar_campos')
def listar_campos():
    campos = campos_certo.listar_campos()
    return render_template('listar_campos.html', campos=campos)

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True)


