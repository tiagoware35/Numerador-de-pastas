# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Importar_XML.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import os, os.path
import xml.etree.ElementTree as ET
from PyQt5 import QtCore, QtGui, QtWidgets, QtXml, QtSql

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 899)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #Botão Selecionar XML
        self.cbtnSelecionarXML = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.cbtnSelecionarXML.setObjectName("cbtnSelecionar")
        self.horizontalLayout.addWidget(self.cbtnSelecionarXML)
        self.cbtnSelecionarXML.clicked.connect(self.selecionarXML)
        
        #Botão Selecionar EFD
        self.cbtnSelecionarEFD = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.cbtnSelecionarEFD.setObjectName("cbtnSelecionarEFD")
        self.horizontalLayout.addWidget(self.cbtnSelecionarEFD)
        self.cbtnSelecionarEFD.clicked.connect(self.selecionarEFD)        
        
        #Botão Numerar Pastas
        self.cbtnNumerarPastas = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.cbtnNumerarPastas.setObjectName("cbtnNumerarPastas")
        self.horizontalLayout.addWidget(self.cbtnNumerarPastas)
        self.cbtnNumerarPastas.clicked.connect(lambda: self.selecionarPasta(self.cbtnNumerarPastas))

        #Botão Limpar numeração
        self.cbtnLimparNumeracao = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.cbtnLimparNumeracao.setObjectName("cbtnLimparNumeracao")
        self.horizontalLayout.addWidget(self.cbtnLimparNumeracao)
        self.cbtnLimparNumeracao.clicked.connect(lambda: self.selecionarPasta(self.cbtnLimparNumeracao))
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Maintab = QtWidgets.QTabWidget(self.centralwidget)
        self.Maintab.setObjectName("Maintab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        #XML TreeView & Model
        self.XMLTreeView = QtWidgets.QTreeView(self.tab)
        self.XMLTreeView.setObjectName("XMLtreeView")
        self.XMLTreeView.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.XMLTreeViewModel = QtGui.QStandardItemModel()
        self.XMLTreeViewModel.setHorizontalHeaderLabels(['Tags','Atributos','Texto'])
        self.XMLTreeView.setModel(self.XMLTreeViewModel)


        self.gridLayout_2.addWidget(self.XMLTreeView, 0, 0, 1, 1)
        self.Maintab.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.tab_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        
        #SQLite3 TreeView e Model
        self.SQLite3TreeView = QtWidgets.QTreeView(self.splitter)
        self.SQLite3TreeView.setObjectName("SQLite3ListView")
        self.SQLite3TreeView.clicked.connect(self.mudarTabela)
        self.SQLite3TreeViewModel = QtGui.QStandardItemModel()
        self.SQLite3TreeViewModel.setHorizontalHeaderLabels(['Tabelas do SQLite3'])
       
        #SQLite3 TableView e Model
        self.SQLite3tableView = QtWidgets.QTableView(self.splitter)
        self.SQLite3tableView.setObjectName("SQLite3tableView")
        self.SQLite3tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.horizontalLayout_2.addWidget(self.splitter)
        self.Maintab.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")

        self.PostgreSQLListView = QtWidgets.QListView(self.splitter_2)
        self.PostgreSQLListView.setObjectName("PostgreSQLtreeView")
        self.PostgreSQLtableView = QtWidgets.QTableView(self.splitter_2)
        self.PostgreSQLtableView.setObjectName("PostgreSQLtableView")
        self.horizontalLayout_3.addWidget(self.splitter_2)
        self.Maintab.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.Maintab, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Maintab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.splitter.setSizes([200, 500])
        self.splitter_2.setSizes([200, 500])

        self.listaRollback = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App XML2DB | Versão 1.0"))
        self.cbtnSelecionarXML.setText(_translate("MainWindow", "Selecionar XML"))
        self.cbtnSelecionarEFD.setText(_translate("MainWindow", "Selecionar EFD"))
        self.cbtnNumerarPastas.setText(_translate("MainWindow", "Numerar Pastas"))
        self.cbtnLimparNumeracao.setText(_translate("MainWindow", "Limpar Numeração"))
        self.Maintab.setTabText(self.Maintab.indexOf(self.tab), _translate("MainWindow", "XML"))
        self.Maintab.setTabText(self.Maintab.indexOf(self.tab_3), _translate("MainWindow", "SQLite3"))
        self.Maintab.setTabText(self.Maintab.indexOf(self.tab_2), _translate("MainWindow", "PostgreSQL"))

    def selecionarXML(self):
        arquivoselecionado = QtWidgets.QFileDialog.getOpenFileName(None,'Selecione Arquivo XML','','Arquivos XML(*.xml)','',)[0]
        if arquivoselecionado:
            arquivotree = QtGui.QStandardItem()
            arquivotree.setIcon(QtGui.QIcon('xml_file.png'))
            arquivotree.setData(os.path.basename(arquivoselecionado), QtCore.Qt.DisplayRole)
            self.XMLTreeViewModel.appendRow(arquivotree)
            self.preencherTreeView(arquivotree, ET.parse(arquivoselecionado).getroot())

            SQLite3DB = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            SQLite3DB.setDatabaseName("PythonDB.db")
            SQLite3DB.open()
            
            nometabelaSQLite3 = 'xml' + os.path.basename(arquivoselecionado[:-4])
            SQLLite3Query = QtSql.QSqlQuery()
            
            SQLLite3Query.exec_("CREATE TABLE IF NOT EXISTS {} (`Tags` TEXT, `Atributos` TEXT, `Texto` TEXT)"
            .format(nometabelaSQLite3))
            
            arquivoXML = ET.parse(arquivoselecionado)
            for tags in arquivoXML.iter():
                atributos = str(tags.attrib).strip('{}')
                atributos = atributos.replace("\'","")
                if tags.text is None:
                    SQLLite3Query.exec_("INSERT INTO {} VALUES (\'{}\',\'{}\',\'{}\')".format(nometabelaSQLite3, tags.tag[36:],atributos,''))
                else:
                    SQLLite3Query.exec_("INSERT INTO {} VALUES (\'{}\',\'{}\',\'{}\')".format(nometabelaSQLite3, tags.tag[36:],atributos,tags.text))
            
            SQLite3TableViewModel = QtSql.QSqlTableModel()
            SQLite3TableViewModel.setTable(nometabelaSQLite3)
            SQLite3TableViewModel.select()
            self.SQLite3tableView.setModel(SQLite3TableViewModel)        
            
            SQLLite3TreeViewQuery = QtSql.QSqlQuery()
            SQLLite3TreeViewQuery.exec_("SELECT name FROM sqlite_master WHERE type='table';")
            while (SQLLite3TreeViewQuery.next()):
                nometabelaSQLite3 = QtGui.QStandardItem()
                nometabelaSQLite3.setIcon(QtGui.QIcon('tabela.png'))
                nometabelaSQLite3.setData(SQLLite3TreeViewQuery.value(0), QtCore.Qt.DisplayRole)
                self.SQLite3TreeViewModel.appendRow(nometabelaSQLite3)        
            self.SQLite3TreeView.setModel(self.SQLite3TreeViewModel)

    def preencherTreeView(self, parent, node):    
        tag = QtGui.QStandardItem()
        tag.setIcon(QtGui.QIcon('xml_tag.png'))
        tag.setData(node.tag[36:], QtCore.Qt.DisplayRole)
        tagatributos = QtGui.QStandardItem()
        tagatributos.setData(str(node.attrib).strip('{}'), QtCore.Qt.DisplayRole)
        tagtexto = QtGui.QStandardItem()
        tagtexto.setData(node.text, QtCore.Qt.DisplayRole)
        parent.appendRow([tag, tagatributos, tagtexto])
        for element in node:
            self.preencherTreeView(tag, element)
    
    def mudarTabela(self):
        index = self.SQLite3TreeView.selectedIndexes()[0]
        nomeTabela = self.SQLite3TreeViewModel.itemFromIndex(index).text()
        
        SQLite3TableViewModel = QtSql.QSqlTableModel()
        SQLite3TableViewModel.setTable(nomeTabela)
        SQLite3TableViewModel.select()
        self.SQLite3tableView.setModel(SQLite3TableViewModel)

    def selecionarEFD(self):
        arquivoselecionado = QtWidgets.QFileDialog.getOpenFileName(None,'Selecione Arquivo EFD','','Arquivos TXT(*.txt)','',)[0]
        if arquivoselecionado:
            with open(arquivoselecionado, encoding="latin-1") as arquivo:
                texto = arquivo.readlines()
                for linha in texto :
                    dados = linha.split('|')
                    if len(dados)>1:
                        print('Esse é um registro do tipo: ' + dados[1])
                        print(linha.strip())
                        print(dados)
                        print('\n')


    #Função para selecionar a pasta a ser numerada e, em caso de erro, fazer o rollback
    def selecionarPasta(self, button):
        self.listaRollback.clear()
        pastaselecionada = QtWidgets.QFileDialog.getExistingDirectory(None,'Selecione uma pasta')
        if pastaselecionada:
            try:
                msgBox = QtWidgets.QMessageBox()              
                self.renomearConteudo(button, pastaselecionada)
                self.criarArquivosTXT(button, pastaselecionada)
                msgBox.setIcon(QtWidgets.QMessageBox.Information) 
                msgBox.setText("Todo conteúdo foi renomeado com sucesso!\n\nPasta: " + pastaselecionada)
                msgBox.setWindowTitle('Informação')
                msgBox.exec_()
            except PermissionError as err:
                self.listaRollback.reverse()
                for arquivo in self.listaRollback:
                    os.rename(arquivo[0],arquivo[1])    
                msgBox.setIcon(QtWidgets.QMessageBox.Critical) 
                msgBox.setText("Verifique se a pasta está aberta em outro aplicativo!\n\n" + str(err))
                msgBox.setWindowTitle('Erro de permissão')
                msgBox.exec_()
            except Exception as err:
                msgBox.setIcon(QtWidgets.QMessageBox.Critical) 
                msgBox.setText(str(err))
                msgBox.setWindowTitle('Atenção!')
                msgBox.exec_()
                print("Ocorreu um erro inesperado: ", sys.exc_info()[0])

    #Função recursiva para numerar ou limpar todo o conteúdo da pasta inicial.
    #A função depende do botão que foi clicado na interface.
    def renomearConteudo(self, button, pasta, indent=''):     
        conteudopasta = os.listdir(pasta)
        for item in conteudopasta:
            fullpathitem = os.path.join(pasta, item)                       
            if (conteudopasta.index(item) < 9): numeroitem = indent + '0' + str(conteudopasta.index(item) + 1) + '.'
            else: numeroitem = indent + str(conteudopasta.index(item) + 1) + '.'
            
            if os.path.isdir(fullpathitem):
                self.renomearConteudo(button, fullpathitem, numeroitem)
            if (button.objectName() == 'cbtnNumerarPastas'):
                os.rename(fullpathitem, os.path.join(pasta, numeroitem + ' ' + item))
                self.listaRollback.append((os.path.join(pasta, numeroitem + ' ' + item), fullpathitem))
            elif (button.objectName() == 'cbtnLimparNumeracao'):
                numlimpar = item.split(' ')
                if (len(numlimpar)>1 and os.path.exists(fullpathitem)):
                    os.rename(fullpathitem, os.path.join(pasta, item[len(numlimpar[0])+1:]))       
                    self.listaRollback.append((os.path.join(pasta, item[len(numlimpar[0])+1:]), fullpathitem))

    def criarArquivosTXT(self, button, pasta):
        fullpathArquivo = os.path.join(pasta, os.path.basename(pasta)) + '.txt'
        if (button.objectName() == 'cbtnNumerarPastas'):
#            open(fullpathArquivo,'w')
            with open(fullpathArquivo,'w') as arquivotxt:
                arquivotxt.write(os.path.basename(pasta) + '.txt')
        elif (button.objectName() == 'cbtnLimparNumeracao'):
            if (os.path.exists(fullpathArquivo)): os.remove(fullpathArquivo)

        conteudopasta = os.listdir(pasta)
        for item in conteudopasta:
            if (os.path.isdir(os.path.join(pasta, item))): self.criarArquivosTXT(button, os.path.join(pasta, item))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())