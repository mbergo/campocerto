# Bibliotecas necessárias
import tkinter as tk

# Classe da janela de pesquisa
class JanelaPesquisa(tk.Tk):
    def __init__(self, campos_certo):
        super().__init__()
        self.title('Pesquisar campos')
        self.geometry('400x100')
        self.campos_certo = campos_certo

        # Campo de entrada para pesquisa
        self.campo_pesquisa = tk.Entry(self)
        self.campo_pesquisa.pack()

        # Botão de pesquisa
        self.botao_pesquisa = tk.Button(self, text='Pesquisar', command=self.pesquisar)
        self.botao_pesquisa.pack()

    # Método para pesquisar campos
    def pesquisar(self):
        # Obter o texto digitado no campo de pesquisa
        texto_pesquisa = self.campo_pesquisa.get()
        resultados = []
        # Verificar se o texto pesquisado corresponde ao nome de algum campo
        for campo in self.campos_certo.campos:
            if campo.nome.lower().startswith(texto_pesquisa.lower()):
                resultados.append(campo)
        # Mostrar resultados da pesquisa
        if resultados:
            print('Campos encontrados:')
            for campo in resultados:
                print(f' - {campo.nome}')
        else:
            print('Nenhum campo encontrado')

# Criar a janela de pesquisa
janela = JanelaPesquisa(campos_certo)
janela.mainloop()

