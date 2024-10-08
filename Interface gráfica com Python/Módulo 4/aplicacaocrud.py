# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:43:22 2020

@author: smonteiro
"""


import tkinter as tk
from tkinter import ttk
import crud as crud

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()  
        #componentes
        self.lbCodigo=tk.Label(win, text='Código do Produto:')
        self.lblNome=tk.Label(win, text='Nome do Produto')
        self.lblPreco=tk.Label(win, text='Preço')
        
        self.txtCodigo=tk.Entry(bd=3)
        self.txtNome=tk.Entry()
        self.txtPreco=tk.Entry()        
        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)    


# Linha 9 - Importamos a biblioteca Tkinter para interagir com os componentes gráficos.
# Linha 10 - Importamos o módulo ttk para podermos trabalhar com o componente “TreeView”, que foi usado como uma grade para exibir os dados armazenados na tabela “PRODUTO”.
# Linha 14 - Implementamos o construtor ( __init__ ) da classe PrincipalBD, que será chamado logo que um objeto do tipo PrincipalBD for instanciado.
# Linha 17 a 23 - Instanciamos os componentes rótulos (“label”) e caixas de texto (“entry”).
# Linha 24 a 27 - Instanciamos os componentes botões (“button”), que vão acionar as operações CRUD.

     
                    
        #----- Componente TreeView --------------------------------------------
        self.dadosColunas = ("Código", "Nome", "Preço")            
                
        self.treeProdutos = ttk.Treeview(win, 
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)        
        self.verscrlbar.pack(side ='right', fill ='x')
                                
        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        
        self.treeProdutos.heading("Código", text="Código")
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("Preço", text="Preço")        

        self.treeProdutos.column("Código",minwidth=0,width=100)
        self.treeProdutos.column("Nome",minwidth=0,width=100)
        self.treeProdutos.column("Preço",minwidth=0,width=100)

        self.treeProdutos.pack(padx=10, pady=10)
        
        self.treeProdutos.bind("<<TreeviewSelect>>", 
                               self.apresentarRegistrosSelecionados)  

        # Observe nas linhas 62 e 63 que o método “apresentarRegistrosSelecionados” é vinculado à instância do componente “TreeView”. Esse método será explicado mais à frente.                
        #---------------------------------------------------------------------        
        #posicionamento dos componentes na janela
        #---------------------------------------------------------------------                
        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)
        
        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)
        
        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)
               
        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)
                   
        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=605, y=300, height=225)        
        self.carregarDadosIniciais()
#-----------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeProdutos.selection():  
            item = self.treeProdutos.item(selection)  
            codigo,nome,preco = item["values"][0:3]  
            self.txtCodigo.insert(0, codigo)  
            self.txtNome.insert(0, nome)  
            self.txtPreco.insert(0, preco)  

#Este método exibe os dados selecionados na grade (componente “TreeView”) nas caixas de texto, de modo que o usuário possa fazer alterações, ou exclusões sobre eles.
                                                              
#Linha 88 - Fazemos a chamada para a função “fLimparTela”, que limpa o conteúdo das caixas de texto.
# Linha 89 - Obtemos os registros que foram selecionados na grade de registros.
# Linha 91 - Os dados do item selecionados são, agora, associados às variáveis “codigo”, “nome” e “preco”.
# Linha 92 a 94 - Os valores das variáveis são associados às caixas de texto.
#-----------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0          
          registros=self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              codigo=item[0]
              nome=item[1]
              preco=item[2]
              print("Código = ", codigo)
              print("Nome = ", nome)
              print("Preço  = ", preco, "\n")
                        
              self.treeProdutos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(codigo,
                                           nome,
                                           preco))                        
              self.iid = self.iid + 1
              self.id = self.id + 1
          print('Dados da Base')        
        except:
          print('Ainda não existem dados para carregar')   

#Este método carrega os dados que já estão armazenados na tabela para serem exibidos na grade de dados (componente “TreeView”).

#                                                                           Linha 105 e 106 - Os atributos “id” e “iid” são iniciados com valor 0. Eles são necessários para gerenciar o componente “TreeView”.
# Linha 107 - É feita a chamada para o método “selecionarDados” que está na classe “AppBD”. Ele recupera todos os registros armazenados na tabela.
# Linha 110 e 112 - Obtemos os valores dos registros e associamos às respectivas variáveis.
# Linha 117 a 121 - Os dados são adicionados ao componente “TreeView”.         
#-----------------------------------------------------------------------------
#LerDados da Tela
#-----------------------------------------------------------------------------           
    def fLerCampos(self):
        try:
          print("************ dados dsponíveis ***********") 
          codigo = int(self.txtCodigo.get())
          print('codigo', codigo)
          nome=self.txtNome.get()
          print('nome', nome)
          preco=float(self.txtPreco.get())          
          print('preco', preco)
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return codigo, nome, preco
    
# Este método lê os dados que estão nas caixas de texto e os retorna para quem faz a chamada.

# Por exemplo, na linha 140, a variável “codigo” recebe o valor da caixa de texto “txtCodigo” depois que ele é convertido para um valor do tipo “inteiro”.

# Na linha 149, as variáveis “codigo”, “nome” e “preco” retornam para quem faz a chamada do método
#-----------------------------------------------------------------------------
#Cadastrar Produto
#-----------------------------------------------------------------------------           
    def fCadastrarProduto(self):
        try:
          print("************ dados dsponíveis ***********") 
          codigo, nome, preco= self.fLerCampos()                    
          self.objBD.inserirDados(codigo, nome, preco)                    
          self.treeProdutos.insert('', 'end',
                                iid=self.iid,                                   
                                values=(codigo,
                                        nome,
                                        preco))                        
          self.iid = self.iid + 1
          self.id = self.id + 1
          self.fLimparTela()
          print('Produto Cadastrado com Sucesso!')        
        except:
          print('Não foi possível fazer o cadastro.')

          Este método tem como objetivo fazer a inserção dos dados na tabela “PRODUTOS”.

# Linha 162 - Os dados digitados nas caixas de texto são recuperados nas variáveis “codigo”, “nome” e “preco”.
# Linha 163 - Fazemos a chamada ao método “inserirDados”, que fará a inserção dos dados na tabela “PRODUTO”.
# Linha 164 a 168 - Os dados são inseridos no componente grade (“TreeView”).
#-----------------------------------------------------------------------------
#Atualizar Produto
#-----------------------------------------------------------------------------           
    def fAtualizarProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          codigo, nome, preco= self.fLerCampos()
          self.objBD.atualizarDados(codigo, nome, preco)          
          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) 
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('Produto Atualizado com Sucesso!')        
        except:
          print('Não foi possível fazer a atualização.')
#-----------------------------------------------------------------------------
#Excluir Produto
#-----------------------------------------------------------------------------                  
    def fExcluirProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          codigo, nome, preco= self.fLerCampos()
          self.objBD.excluirDados(codigo)          
          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) 
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('Produto Excluído com Sucesso!')        
        except:
          print('Não foi possível fazer a exclusão do produto.')
#-----------------------------------------------------------------------------
#Limpar Tela
#-----------------------------------------------------------------------------                 
    def fLimparTela(self):
        try:
          print("************ dados dsponíveis ***********")        
          self.txtCodigo.delete(0, tk.END)
          self.txtNome.delete(0, tk.END)
          self.txtPreco.delete(0, tk.END)
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')
#-----------------------------------------------------------------------------
#Programa Principal
#-----------------------------------------------------------------------------          
janela=tk.Tk()
principal=PrincipalBD(janela)
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("720x600+10+10")
janela.mainloop()
#-----------------------------------------------------------------------------




