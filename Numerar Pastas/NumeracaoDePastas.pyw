# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NumeracaoDePastas.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 224)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Botão Numerar Pastas
        self.cbtnNumerarPastas = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.cbtnNumerarPastas.setGeometry(QtCore.QRect(80, 40, 185, 41))
        self.cbtnNumerarPastas.setObjectName("cbtnNumerarPastas")
        self.cbtnNumerarPastas.clicked.connect(lambda: self.selecionarPasta(self.cbtnNumerarPastas))

        #Botão Limpar numeração
        self.cbtnLimparNumeracao = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.cbtnLimparNumeracao.setGeometry(QtCore.QRect(80, 120, 185, 41))
        self.cbtnLimparNumeracao.setObjectName("cbtnLimparNumeracao")
        self.cbtnLimparNumeracao.clicked.connect(lambda: self.selecionarPasta(self.cbtnLimparNumeracao))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listaRollback = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numeração de Pastas"))
        self.cbtnNumerarPastas.setText(_translate("MainWindow", "Numerar Pastas"))
        self.cbtnLimparNumeracao.setText(_translate("MainWindow", "Limpar Numeração"))

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

    #Função recursiva para numerar ou limpar todo o conteúdo da pasta inicial.
    #A função depende do botão que foi clicado na interface.
    def renomearConteudo(self, button, pasta, indent=''):     
        conteudopasta = os.listdir(pasta)
        for item in conteudopasta:
            fullpathitem = os.path.join(pasta, item)                       
            if (conteudopasta.index(item) < 9):
                numeroitem = indent + '0' + str(conteudopasta.index(item) + 1) + '.'
            else:
                numeroitem = indent + str(conteudopasta.index(item) + 1) + '.'
            
            if os.path.isdir(fullpathitem):
                self.renomearConteudo(button, fullpathitem, numeroitem)
            if (button.objectName() == 'cbtnNumerarPastas'):
                os.rename(fullpathitem, os.path.join(pasta, numeroitem + ' ' + item))
                self.listaRollback.append((os.path.join(pasta, numeroitem + ' ' + item), fullpathitem))
            elif (button.objectName() == 'cbtnLimparNumeracao'):
                numlimpar = item.split(' ')
                if (len(numlimpar)>1):
                    os.rename(fullpathitem, os.path.join(pasta, item[len(numlimpar[0])+1:]))       
                    self.listaRollback.append((os.path.join(pasta, item[len(numlimpar[0])+1:]), fullpathitem))

    def criarArquivosTXT(self, button, pasta):
        fullpathArquivo = os.path.join(pasta, os.path.basename(pasta)) + '.txt'
        if (button.objectName() == 'cbtnNumerarPastas'):
            with open(fullpathArquivo,'w') as arquivotxt:
                arquivotxt.write(os.path.basename(fullpathArquivo))
        elif (button.objectName() == 'cbtnLimparNumeracao'):
            if (os.path.exists(fullpathArquivo)): 
                os.remove(fullpathArquivo)

        conteudopasta = os.listdir(pasta)
        for item in conteudopasta:
            fullpathitem = os.path.join(pasta, item)
            if (os.path.isdir(fullpathitem)):
                self.criarArquivosTXT(button, fullpathitem)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())