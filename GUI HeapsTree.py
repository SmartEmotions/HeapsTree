#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from Listas import*
from PyQt4 import QtCore, QtGui, uic
from HeapTree import HeapTree
from ImportProducts import ImportProducts
from PrintTree import preorder, posorder, inorder
from PyQt4.QtCore import *
from PyQt4.QtGui import *

form_class = uic.loadUiType("GraphicGUIHeapTree.ui")[0]


class MyWindowClass(QtGui.QMainWindow, form_class):
    '''
    Funcion que inicia objetos de la ventanan grafica para el
    programa de interfaz grafica, aqui se instancia el objeto
    arbol de importacion, se habilita la visibilidad de algunos
    objetos y se deshabilita aquellos que no se necesita en principio
    o aquellos que no deben esta habiles cuando el programa es iniciado
    Tambien se instancian los menus de opciones en la ventana superior
    y se conecta señales o slots de botones y menus.
    Ademas de eso tambien se hace la validacion con la funcion
    validator para los QLineEdit, que solo recibiran valores
    numericos de tipo float
    '''
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.arbol = HeapTree()
        self.listCode = ['-Select-', '01', '02', '03',
                         '04', '05', '06',
                         '07', '08', '09', '10', '11']
        self.visibleGUI(True)
        self.productChangeValues = 'Cambiar precio y/o cantidad'

        self.manual = QtGui.QAction('Manual', self)
        self.about = QtGui.QAction('About',self)
        self.printInorder = QtGui.QAction('Inorder', self)
        self.printPosorder = QtGui.QAction('Posorder', self)
        self.printPreorder = QtGui.QAction('Preorder', self)
        self.saveasTXT = QtGui.QAction('Save as TXT', self)
        self.saveasBin = QtGui.QAction('Save as Bin',self)
        self.openTXT = QtGui.QAction('Open TXT', self)
        self.openBin = QtGui.QAction('Open Bin',self)

        self.header = ['Code',
							'ProductName',
							'PaisExport',
							'Cost $',
							'Cant',
							'Unit',
							'Tariff']

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Archivo')
        fileMenu.addAction(self.openTXT)
        fileMenu.addAction(self.openBin)
        fileMenu.addAction(self.saveasTXT)
        fileMenu.addAction(self.saveasBin)
        self.showMenu = menubar.addMenu('&Imprimir Arbol')
        self.showMenu.addAction(self.printPreorder)
        self.showMenu.addAction(self.printPosorder)
        self.showMenu.addAction(self.printInorder)
        helpMenu = menubar.addMenu('&Ayuda')
        helpMenu.addAction(self.manual)
        helpMenu.addAction(self.about)

        self.codeLabel.addItems(self.listCode)
        self.codeProducts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        self.codeLabel.activated['QString'].connect(self.codeActivated)
        self.nameLabel.activated['QString'].connect(self.nameActivated)
        self.countryLabel.activated['QString'].connect(self.countryActivated)
        self.unitLabel.activated['QString'].connect(self.unitActivated)

        self.insertData.setHidden(True)
        self.searchData.setHidden(True)
        self.findData.setHidden(True)
        self.arancelLabel.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.searchButton.setEnabled(False)
        self.findButtons.setEnabled(False)
        self.welcomeText.setHidden(False)
        self.manualWidget.setHidden(True)
        self.showMenu.setEnabled(False)

        txtManual = open('Manual.txt', 'r')
        listManual = []
        for line in txtManual:
            listManual.append(line)
        importManual = MyListModel(listManual)
        self.manualListView.setModel(importManual)
        

        self.connect(self.openTXT, QtCore.SIGNAL('triggered()'), self.opentxtDialog)
        self.connect(self.openBin, QtCore.SIGNAL('triggered()'), self.openbinaryDialog)
        self.connect(self.saveasTXT, QtCore.SIGNAL('triggered()'), self.savetxtDialog)
        self.connect(self.saveasBin, QtCore.SIGNAL('triggered()'), self.savebinaryDialog)
        self.connect(self.printPreorder, QtCore.SIGNAL('triggered()'), self.showPreorder)
        self.connect(self.printPosorder, QtCore.SIGNAL('triggered()'), self.showPosorder)
        self.connect(self.printInorder, QtCore.SIGNAL('triggered()'), self.showInorder)
        self.connect(self.manual, QtCore.SIGNAL('triggered()'), self.showManual)
        self.connect(self.about, QtCore.SIGNAL('triggered()'), self.showAbout)

        self.insertButton.clicked.connect(self.insertClicked)
        self.insertData.clicked.connect(self.insertNewData)
        self.deleteButton.clicked.connect(self.delete)
        self.searchButton.clicked.connect(self.searchClicked)
        self.searchData.clicked.connect(self.searchKey)
        self.findButtons.clicked.connect(self.findClicked)
        self.findData.clicked.connect(self.findKey)
        self.modificarProducto.clicked.connect(self.activedChangeValues)
        self.changeNewValues.clicked.connect(self.changeValues)
        self.costLabel.setValidator(QtGui.QDoubleValidator())
        self.cantLabel.setValidator(QtGui.QDoubleValidator())
        self.newCant.setValidator(QtGui.QDoubleValidator())
        self.newCost.setValidator(QtGui.QDoubleValidator())

    def showManual(self):
        self.visibleGUI(True)
        self.manualWidget.setHidden(False)
        
    def showAbout(self):
        showFrame = AboutDialogWindow().exec_()

    def visibleGUI(self, unable):
        '''
        Esta funcion es necesaria para esconder los widgets, cada vez que
        el usuario a elegido una nueva opcion o funcion del programa
        :unable: es la variable boleana que se recibe cada vez que se
        llama la funcion los valores pueden ser True or False
        si es True los widgets seran escondidos y no estaran
        disponibles, si es False, se mostrara los widgets
        '''
        self.manualWidget.setHidden(unable)
        self.inputUser.setHidden(unable)
        self.infoProduct.setHidden(unable)
        self.welcomeText.setHidden(unable)
        self.searchInfo.setHidden(unable)
        self.tableWidget.setHidden(unable)
        for i in range(self.layoutMessage.count()):
            self.layoutMessage.itemAt(i).widget().close()
        self.nameLabel.clear()
        self.countryLabel.clear()
        self.unitLabel.clear()
        self.codeLabel.clear()
        self.costLabel.setText('')
        self.cantLabel.setText('')
        self.newCant.setText('')
        self.newCost.setText('')
        self.codeLabel.addItems(self.listCode)

    def codeActivated(self, text):
        '''Funcion que lanza las opciones a el objeto de name
        es decir, en la funcion insertar nueva importacion, el
        usuario tendra la posibilidad de elegir unos codigos del
        proucto, pero cada codigo tiene productos diferentes, entonces
        caba vez que el usuario seleccione un codigo la
        lista para el QComboBox sera diferente
        '''
        self.nameLabel.clear()
        self.countryLabel.clear()
        self.unitLabel.clear()
        if self.insertData.isEnabled():
                self.insertData.setEnabled(False)
        if self.costLabel.isEnabled():
                self.costLabel.setEnabled(False)
                self.cantLabel.setEnabled(False)
        if text != '-Select-':
            new_items = listaImportaciones[int(text) -1]
            self.nameLabel.addItems(new_items)

    def nameActivated(self, text):
        '''Funcion que lanza las opciones a el objeto de pais del producto
        en la funcion insertar nueva importacion, el
        usuario tendra la posibilidad de elegir nombres del producto
        dependiendo del codigo seleccionado
        pero los productos no estan disponibles en todos los paises, entonces
        caba vez que el usuario seleccione un nombre la
        lista para el QComboBox  de pais del producto sera diferente
        '''
        self.countryLabel.clear()
        self.unitLabel.clear()
        if self.insertData.isEnabled():
                self.insertData.setEnabled(False)
        if self.costLabel.isEnabled():
                self.costLabel.setEnabled(False)
                self.cantLabel.setEnabled(False)
        if text != '-Select-':
            new_items = listcountryProduct(text, [])
            self.countryLabel.addItems(new_items)

    def countryActivated(self, text):
        '''
        Esta funcion cumple dos tareas, la primera
        es que cuando se desea buscar o encontrar un producto
        este se puede encontrar con las primeras tres caracteristicas
        Nobre, Codigo y Pais entonces este QComboBox le habilita al
        usuario el boton de busqueda o encontra producto
        Y la segunda de las funciones es cuando el usuario esta insertando
        un nuevo producto a importar, entonces este habilita el
        siguiente CajaDeOpcioness para seleccionar en que medidas
        o unidades se importara el producto
        '''
        if self.insertData.isEnabled():
                self.insertData.setEnabled(False)
        if self.costLabel.isEnabled():
                self.costLabel.setEnabled(False)
                self.cantLabel.setEnabled(False)
        self.unitLabel.clear()
        if text != '-Select-':
            self.unitLabel.addItems(listunitProduct(
                           self.nameLabel.currentText(), []))
            position = paisesExportadores.index(text)
            self.arancelLabel.setText(str(arancelCountries[position]))
            if not self.searchData.isHidden():
                self.searchData.setEnabled(True)
            if not self.findData.isHidden():
                self.findData.setEnabled(True)

    def unitActivated(self, text):
        '''
        Esta funcion de El QComboBox Seleccion de unidades, si el usuario
        selecciona las unidades de medida, se le habilita dos QLineEdit
        uno de digitar precio y otro de cantidad, la dos anteriores
        deberan digitarse en acorde a la opcion digitada
        '''
        if text != '-Select-':
            if not self.insertData.isHidden():
                self.insertData.setEnabled(True)
            self.costLabel.setEnabled(True)
            self.cantLabel.setEnabled(True)
            self.cantTitle.setText('Cantidad en ' +
                                   self.unitLabel.currentText())
            self.costTitle.setText('Precio por ' +
                                   self.unitLabel.currentText())

    def activedChangeValues(self):
        '''
        Cuando el usuario a encontrado un producto se presenta la
        opcion de cambiar el precio y el costo, si el usuario a optado
        por hacer cambios se ejecuta esta accion habilitando QLineEdit
        para que digite los nuevos precios y la nueva cantidad
        '''
        self.newCant.setEnabled(True)
        self.newCost.setEnabled(True)
        self.changeCantTitle.setText('Nueva cantidad en ' +
                                     self.productChangeValues.unitProduct)
        self.changeCostTitle.setText('Nuevo costo por ' +
                                     self.productChangeValues.unitProduct)
        self.changeNewValues.setEnabled(True)

    def changeValues(self):
        '''
        Esta funcio se ejecuta cuando el usuario digita los nuevos
        cambios para un producto encontrado, los precios no
        pueden disminuir mas del 50% por unidad de medida, y la
        cantidad no puede ser menor a 1
        '''
        for i in range(self.layoutMessage.count()):
            self.layoutMessage.itemAt(i).widget().close()
        newCant = (self.newCant.text())
        newCost = (self.newCost.text())
        porcentaje1 = float(self.productChangeValues.costProduct)
        porcentaje2 = float(self.productChangeValues.cantProduct)
        if newCant != '' and newCost != '':
            if  float(newCost) >= porcentaje1*0.5 and  float(newCost) <= porcentaje1*1.5:
                if float(newCant) >= 1 and float(newCant) <= 100000:
                    self.productChangeValues.costProduct = float(newCost)
                    self.productChangeValues.cantProduct = float(newCant)
                    self.arbol.changeValuesProduct()
                    message = ['Los nuevos valores fueron modificados correctamente']
                else:
                    message =['La nueva cantidad no puede' +
                                              ' ser menor a 1 ni mayor ' +
                                              'a 100 mil unidades']
            else:
                message = ['El nuevo costo no puede ser menor ' +
                                          ' ni mayor al 50% del valor actual',
                                          'Digite costos entre 100% - 50% y ' +
                                          '100% + 50%']
        else:
            message = ['No deje en blanco los cambios, por favor' +
                                      ' rellene la informacion necesaria']
        listview = QListView()
        model = MyListModel(message)
        listview.setModel(model)
        self.layoutMessage.addWidget(listview)

        self.newCant.setText('')
        self.newCost.setText('')
        self.newCant.setEnabled(False)
        self.newCost.setEnabled(False)
        self.changeNewValues.setEnabled(False)

    def insertClicked(self):
        '''
        Esta funcion pertenece a la señal enviada dese el QPressButton
        de insertar nueva importacion, aqui se habilita los objetos para
        el usuario, y se deshabilita las tareas anteriores
        '''
        self.nameLabel.clear()
        self.countryLabel.clear()
        self.unitLabel.clear()
        self.visibleGUI(True)
        if (not self.searchData.isHidden() or
            not self.findData.isHidden()):
            self.findData.setHidden(True)
            self.searchData.setHidden(True)
        if not self.unitLabel.isEnabled():
            self.unitLabel.setEnabled(True)
        self.costLabel.setEnabled(False)
        self.cantLabel.setEnabled(False)
        self.inputUser.setHidden(False)
        self.insertData.setEnabled(False)
        self.insertData.setHidden(False)

    def searchClicked(self):
        '''
        Funcion que habilita los widgets necesarios para hacer una busqueda
        de producto
        '''
        self.nameLabel.clear()
        self.countryLabel.clear()
        self.unitLabel.clear()
        if (not self.insertData.isHidden() or
            not self.findData.isHidden()):
            self.findData.setHidden(True)
            self.insertData.setHidden(True)
        self.visibleGUI(True)
        self.inputUser.setHidden(False)
        self.hiddenObjects(False)
        self.searchData.setHidden(False)
        self.searchData.setEnabled(False)

    def findClicked(self):
        '''
        Este metodo habilita los widgets de buscar cuando el
        boton buscar a recibido un click por parte del
        usuario
        '''
        self.nameLabel.clear()
        self.countryLabel.clear()
        self.unitLabel.clear()
        if (not self.insertData.isHidden() or
            not self.searchData.isHidden()):
            self.insertData.setHidden(True)
            self.searchData.setHidden(True)
        self.visibleGUI(True)
        self.inputUser.setHidden(False)
        self.hiddenObjects(False)
        self.findData.setHidden(False)
        self.findData.setEnabled(False)

    def hiddenObjects(self, unable):
        self.unitLabel.setEnabled(unable)
        self.costLabel.setEnabled(unable)
        self.cantLabel.setEnabled(unable)

    def showPreorder(self):
        '''
        Metodo que extrae la informacion del arbol en preorder
        cuando el arbol, tiene datos, se genera una lista con los
        nodos y se la presenta en una tabla con la informacion
        de cada uno de los nodos
        '''
        self.visibleGUI(True)
        self.tableWidget.setHidden(False)
        for i in range(self.tableLayout.count()):
            self.tableLayout.itemAt(i).widget().close()
        table = QTableView()
        tableModel = MyTableModel(preorder(self.arbol), self.header)
        table.setModel(tableModel)
        self.tableLayout.addWidget(table)

    def showPosorder(self):
        '''
        Metodo que extrae la informacion del arbol en posorder
        cuando el arbol, tiene datos, se genera una lista con los
        nodos y se la presenta en una tabla con la informacion
        de cada uno de los nodos
        '''
        self.visibleGUI(True)
        self.tableWidget.setHidden(False)
        for i in range(self.tableLayout.count()):
            self.tableLayout.itemAt(i).widget().close()
        table = QTableView()
        tableModel = MyTableModel(posorder(self.arbol), self.header)
        table.setModel(tableModel)
        self.tableLayout.addWidget(table)

    def showInorder(self):
        '''
        Metodo que extrae la informacion del arbol en preorder
        cuando el arbol, tiene datos, se genera una lista con los
        nodos y se la presenta en una tabla con la informacion
        de cada uno de los nodos
        '''
        self.visibleGUI(True)
        self.tableWidget.setHidden(False)
        for i in range(self.tableLayout.count()):
            self.tableLayout.itemAt(i).widget().close()
        table = QTableView()
        print(inorder(self.arbol))
        tableModel = MyTableModel(inorder(self.arbol), self.header, self)
        table.setModel(tableModel)
        self.tableLayout.addWidget(table)

    def insertNewData(self):
        '''
        Este metodo toma todos los datos selecionados por el usuario
        en el widget de input user, los textos de cada QComboBox
        y los QLineEdit, y los reune para crear un objeto del tipo
        ImportProducts, se validan algunas cantidades en los precios
        y las cnatidades a digitar
        '''
        listview = QListView()
        for i in range(self.layoutMessage.count()):
            self.layoutMessage.itemAt(i).widget().close()
        self.arancelLabel.setEnabled(True)
        codeProduct = self.codeLabel.currentText()
        nameProduct = self.nameLabel.currentText()
        countryProduct = self.countryLabel.currentText()
        costProduct = self.costLabel.text()
        cantProduct = self.cantLabel.text()
        unitProduct = self.unitLabel.currentText()
        arancelProduct = self.arancelLabel.text()
        if(costProduct != '' and cantProduct != ''):
            if (float(costProduct) >= 1000 and
                float(costProduct) <= 10000000000 and
                float(cantProduct) >= 1 and
                float(cantProduct) <= 100000):
                new_product = ImportProducts(codeProduct,
                                            nameProduct,
                                            countryProduct,
                                            costProduct,
                                            cantProduct,
                                            arancelProduct,
                                            unitProduct)
                self.arbol.insert(new_product)
                messageinsert = ['Se adiciono una importacion ' +
                                 'correctamente']
            else:
                messageinsert = ['El costo del producto no puede ' +
                                          'ser menor a $1000 ni mayor a 10 mil millones',
                                          'La cantidad debe ser minimo una unidad' +
                                          ' y como maximo 100 mil unidades ']
        else:
            messageinsert = ['No deje en blanco el precio del producto' +
                                      ' o la cantidad de producto a importar',
                                      'Por favor rellene la informacion necesaria']
        model = MyListModel(messageinsert)
        listview.setModel(model)
        self.layoutMessage.addWidget(listview)
        self.costLabel.setText("")
        self.cantLabel.setText("")
        self.arancelLabel.setText("")
        self.nameLabel.clear()
        self.countryLabel.clear()
        self.unitLabel.clear()
        self.codeLabel.clear()
        self.codeLabel.addItems(self.listCode)
        self.insertData.setEnabled(False)
        self.arancelLabel.setEnabled(False)
        self.showinfoTree()

    def searchKey(self):
        '''
        Metodo que toma las entradas de usuario, en este caso
        Codigo del producto, nombre del producto y pais del
        producto, el resto de atributos se rellenan con ceros
        y se crea el objeto a buscar, si el objeto se encuentra
        en la lista del importaciones, se muestra mensaje
        afirmativo y por el contrario se dice que el
        producto no fue encotrado
        '''
        codeProduct = self.codeLabel.currentText()
        nameProduct = self.nameLabel.currentText()
        countryProduct = self.countryLabel.currentText()
        new_product = ImportProducts(codeProduct,
														nameProduct,
														countryProduct,
														"0", "0", "0", '0')
        self.visibleGUI(True)
        self.searchInfo.setHidden(False)
        searchTree = self.arbol.search(new_product)
        if searchTree == True:
            self.searchInfo2.setText('El Producto se encuentra en la')
            self.searchInfo1.setText("cola de Importaciones !")
        else:
            self.searchInfo2.setText("Este Producto no existe en las " )
            self.searchInfo1.setText("importaciones")
        self.searchData.setHidden(True)
        self.nameLabel.clear()
        self.countryLabel.clear()
        self.unitLabel.clear()
        self.codeLabel.clear()
        self.codeLabel.addItems(self.listCode)

    def findKey(self):
        '''
        Metodo que toma las entradas de usuario, en este caso
        Codigo del producto, nombre del producto y pais del
        producto, el resto de atributos se rellenan con ceros
        y se crea el objeto a buscar, si el objeto se encuentra
        en la lista del importaciones, se muestra la informacion
        del producto en pantalla, y se presenta la
        opcion de hacer cambios en el producto encontrado
        si el usuario lo desea, si el producto no es encontrado
        se muestra mensaje que no existe el producto
        '''
        self.infoProduct.setHidden(False)
        codeProduct = self.codeLabel.currentText()
        nameProduct = self.nameLabel.currentText()
        countryProduct = self.countryLabel.currentText()
        new_product = ImportProducts(codeProduct,
                                    nameProduct,
                                    countryProduct,
                                    "0", "0", "0", '0')
        self.visibleGUI(True)
        self.findData.setHidden(True)
        search = self.arbol.find(new_product)
        if search is not None:
            self.infoProduct.setHidden(False)
            self.infoName.setText(search.nameProduct)
            self.infoCode.setText(str(search.codeProduct))
            self.infoCountry.setText(str(search.countryProduct))
            self.infoCost.setText(str(search.costProduct))
            self.infoCant.setText(str(search.cantProduct))
            self.infoArancel.setText(str(search.arancelProduct))
            self.costinfoTitle.setText('Precio por ' + search.unitProduct)
            self.cantinfoTitle.setText('Cantidad en ' + search.unitProduct)
            self.productChangeValues = search
            self.newCant.setEnabled(False)
            self.newCost.setEnabled(False)
            self.changeNewValues.setEnabled(False)
        else:
            self.searchInfo.setHidden(False)
            self.searchInfo2.setText("Este Producto no fue encontrado " )
            self.searchInfo1.setText("en la cola de importaciones")
        self.nameLabel.clear()
        self.countryLabel.clear()
        self.unitLabel.clear()
        self.codeLabel.clear()
        self.codeLabel.addItems(self.listCode)

    def opentxtDialog(self):
        '''
        Funcion que permite abrir un archivo de texto
        con formato del programa ImportColombia, las lineas, y parametros
        deben tener una configuracion definida para que se cargen
        de manera correcta, si las lineas escritas en el archivo
        no coinciden con los datos del programa no se agrega el archivo
        los mensajes de error se mostraran en la caja de texto inferior
        este metodo solo habilita la apertura de archivos *.txt
        NOTA: Los productos o objetos de tipo ImportProduct se agregaran
        si en el arbol creado por el usuario no contiene ya productos
        similares
        '''
        self.visibleGUI(True)
        filename = QtGui.QFileDialog.getOpenFileName(self,
                                                     'Abrir archivo',
                                                     '/home',
                                                     "(*.txt)")
        if filename:
            listMessage = []
            regTree = open(filename, "r")
            i = 1
            for line in regTree:
                if line != "" and '|' in line:
                    line = line.replace("\n", "")
                    line = line.split("|")
                    if len(line) == 7:
                        codeProduct = line[0]
                        nameProduct = line[1]
                        countryProduct = line[2]
                        costProduct = line[3]
                        cantProduct = line[4]
                        unitProduct = line[5]
                        arancelProduct = line[6]
                        new_product = ImportProducts(codeProduct,
                                                    nameProduct,
                                                    countryProduct,
                                                    costProduct,
                                                    cantProduct,
                                                    arancelProduct,
                                                    unitProduct)
                        validar, message = self.validarProduct(new_product)
                        if validar:
                            self.arbol.insert(new_product)
                            listMessage.append('Archivo en la linea ' + str(i) +
                                               ' abierto correctamente')
                        else:
                            listMessage.append("El archivo en la linea " + str(i) +
                                               ' no es correcto')
                    else:
                        listMessage.append("Archivo en la linea " + str(i) +
                                           ' es corrupto')
                else:
                    listMessage.append("La linea " + str(i) +
                                       ' esta vacia o no corresponde' +
                                       ' a una importacion')
                i = i + 1
            regTree.close()
            listMessage.append('FIN DEL ARCHIVO')
            listview = QListView()
            model = MyListModel(listMessage)
            listview.setModel(model)
            self.layoutMessage.addWidget(listview)
        self.showinfoTree()

    def openbinaryDialog(self):
        '''
        Funcion que permite abrir un archivo de texto
        con formato del programa ImportColombia, las lineas, y parametros
        deben tener una configuracion definida para que se cargen
        de manera correcta, si las lineas escritas en el archivo
        no coinciden con los datos del programa no se agrega el archivo
        los mensajes de error se mostraran en la caja de texto inferior
        este metodo solo habilita la apertura de archivos *.bin
        NOTA: Los productos o objetos de tipo ImportProduct se agregaran
        si en el arbol creado por el usuario no contiene ya productos
        similares
        '''
        self.visibleGUI(True)
        filename = QtGui.QFileDialog.getOpenFileName(self,
                                                     'Abrir archivo',
                                                     '/home',
                                                     "(*.bin)")
        if filename:
            i = 0
            listMessage = []
            regTree = open(filename, "rb")
            for line in regTree:
                if line != "" and '|' in  line:
                    line = line.replace("\n", "")
                    line = line.split("|")
                    if len(line) == 7:
                        codeProduct = line[0]
                        nameProduct = line[1]
                        countryProduct = line[2]
                        costProduct = line[3]
                        cantProduct = line[4]
                        unitProduct = line[5]
                        arancelProduct = line[6]
                        new_product = ImportProducts(codeProduct,
                                                    nameProduct,
                                                    countryProduct,
                                                    costProduct,
                                                    cantProduct,
                                                    arancelProduct,
                                                    unitProduct)
                        validar, message = self.validarProduct(new_product)
                        if validar:
                            if not self.arbol.search(new_product):
                                self.arbol.insert(new_product)
                                listMessage.append('Archivo en la linea ' + str(i) +
                                               ' abierto correctamente')
                            else:
                                listMessage.append('Archivo en la linea ' + str(i) +
                                               ' Ya se encuentra en la cola')
                        else:
                            listMessage.append("El archivo en la linea " + str(i) +
                                               ' no es correcto ' +message )
                    else:
                        listMessage.append("Archivo en la linea " + str(i) +
                                           ' es corrupto')
                else:
                    listMessage.append("La linea " + str(i) +
                                       ' esta vacia o no corresponde' +
                                       ' a una importacion')
                i = i + 1
            regTree.close()
            listMessage.append('FIN DEL ARCHIVO')
            listview = QListView()
            model = MyListModel(listMessage)
            listview.setModel(model)
            self.layoutMessage.addWidget(listview)
        self.showinfoTree()

    def savetxtDialog(self):
        '''
        Metodo que guarda todo la informacion de la cola de Importaciones
        este metodo esta implementado en la Clase HeapTree, y se invoca
        solamente desde salvar en text o en binario, cuando el ususario
        seleccione las opciones mensionadas, el usuario debera digitar el
        nombre del archivo a guardarse, y la extension .txt o .bin una vez
        aceptado, el arbol se cierra automaticamente, y los datos son salvados
        si se necesitara seguir trabajando con el arbol, se debera abrir
        el archivo guardado
        '''
        self.visibleGUI(True)
        nameTree = QtGui.QFileDialog.getSaveFileName(self,
                                                     "Guardar fichero",
                                                     "/home/carlos/Escritorio",
                                                     "(*.txt)")
        if nameTree:
            writeTree = open(nameTree, 'w') # Indicamos el valor 'w'.
            savetxtList = self.arbol.saveTree()
            for node in savetxtList:
                writeTree.write(str(node.codeProduct) + "|" +
                                str(node.nameProduct) + "|" +
                                str(node.countryProduct) + "|" +
                                str(node.costProduct) + "|" +
                                str(node.cantProduct) + "|" +
                                str(node.unitProduct) + '|' +
                                str(node.arancelProduct) + "\n")
            writeTree.close()
        self.showinfoTree()

    def savebinaryDialog(self):
        '''
        Metodo que guarda todo la informacion de la cola de Importaciones
        este metodo esta implementado en la Clase HeapTree, y se invoca
        solamente desde salvar en text o en binario, cuando el ususario
        seleccione las opciones mensionadas, el usuario debera digitar el
        nombre del archivo a guardarse, y la extension .txt o .bin una vez
        aceptado, el arbol se cierra automaticamente, y los datos son salvados
        si se necesitara seguir trabajando con el arbol, se debera abrir
        el archivo guardado
        '''
        self.visibleGUI(True)
        nameTree = QtGui.QFileDialog.getSaveFileName(self,
                                                     "Guardar fichero",
                                                     "/home/carlos/Escritorio",
                                                     "(*.bin)")
        if nameTree:
            writeTree = open(nameTree, 'wb')
            savetxtList = self.arbol.saveTree()
            for node in savetxtList:
                writeTree.write(str(node.codeProduct) + "|" +
                                str(node.nameProduct) + "|" +
                                str(node.countryProduct) + "|" +
                                str(node.costProduct) + "|" +
                                str(node.cantProduct) + "|" +
                                str(node.unitProduct) + '|' +
                                str(node.arancelProduct) + "\n")
            writeTree.close()
        self.showinfoTree()

    def showinfoTree(self):
        '''
        Metodo que actualiza los cambios en el arbol
        este permite observar cuantos nodos han sido agregados, las
        hojas que contiene, los inodes, y la profundidad del arbol
        '''
        self.lenLabel.setText(str(len(self.arbol)))
        self.leavesLabel.setText(str(self.arbol.leaves(self.arbol._root)))
        self.depthLabel.setText(str(self.arbol.depth(self.arbol._root)))
        self.inodesLabel.setText(str(self.arbol.inodes()))
        if self.arbol.is_empty():
            self.showMenu.setEnabled(False)
            self.deleteButton.setEnabled(False)
            self.searchButton.setEnabled(False)
            self.findButtons.setEnabled(False)
        else:
            self.deleteButton.setEnabled(True)
            self.searchButton.setEnabled(True)
            self.findButtons.setEnabled(True)
            self.showMenu.setEnabled(True)

    def delete(self):
        '''
        Metodo para atender al primero de la cola en la lista
        este metodo elimina el primer nodo, es decir la raiz del arbol
        la funcion del metodo se especifica mejor en la clase HeapTree
        '''
        self.visibleGUI(True)
        self.arbol.delete()
        self.showinfoTree()

    def validarProduct(self, product):
        '''
        Metodo que valida las entradas por archivo
        dado que los archivos no se tiene control
        de las entradas, entonces este valida un objeto que se crea
        desde el archivo abierto, si alguna linea ah sido
        cambiada con valores no acordes al sistema
        '''
        if product.codeProduct in self.codeProducts:
            listadeproductos = self.codeProducts.index(product.codeProduct)
            if product.nameProduct in listaImportaciones[listadeproductos]:
                if product.countryProduct in paisesExportadores:
                    codeCountry = paisesExportadores.index(product.countryProduct)
                    if product.nameProduct in productsCountry[codeCountry]:
                        return True, 'Importacion Correcta !'
                    else:
                        return False, (product.countryProduct +
                                       ' No exporta ' +
                                       product.nameProduct)
                else:
                    return False, (product.countryProduct +
                                   ' No es un pais Proveedor de importaciones' +
                                   ' para Colombia')
            else:
                return False, (product.nameProduct + ' No pertenece a' +
                               ' productos del codigo ' +
                               str(product.codeProduct) +
                               ' o este producto no forma parte ' +
                               ' de las importaciones')
        return False, ('El codigo ' + product.codeProduct + ' No Existe')


class MyTableModel(QAbstractTableModel):
    '''
    Clase implementada para el modelo de la tabla, cuando se desea presentar
    el arbol en las diferentes formas, se reciben los datos desde y se crea un
    modelo de Tabla y se actualizan los datos, y el orden de los mismos
    '''
    def __init__(self, datain, headerdata, parent=None, *args):
        '''
        Metodo de inicio de un objeto abstracto, se reciben por parametro.
        :datain: Es la lista en preorder, posorder o inorder
        :headerdata: Son los nombres de las cabeceras de cada columna
                     lo que identifica los datos
        :parent: valor por defecto de la clase
        :*args: argumentos necesarios que se cargan para la creacion objeto
        abstracto
        '''
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata
    def rowCount(self, parent=QModelIndex()):
        '''
        Este metodo cuenta cuanta filas tendra la tabla
        '''
        return len(self.arraydata)

    def columnCount(self, parent=QModelIndex()):
        '''
        Metodo que retorna cuantas columnas tendra la tabla
        depende del tamaño del primer dato en la lista
        '''
        return len(self.arraydata[0])

    def data(self, index, role):
        '''
        Metodo por defecto carga los datos de la lista en el orden
        de fila columna creada en un principio
        '''
        if role == Qt.BackgroundRole:
            return QBrush(Qt.yellow)
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        '''
        Metodo que carga los nombres de las cabeceras en la tabla
        '''
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

class MyListModel(QAbstractListModel):
    '''
    Clase implementada para poder mostrar los mensajes en el pie
    del programa, se reciben los textos y se se apilan
    para mostrarlos completos, esta clase tambien se implementa para
    mostrar el manual del programa
    '''
    def __init__(self, datain, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.listdata = datain
        self.headerdata = datain

    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.listdata[index.row()])

    def removeData(self, parent=QModelIndex()):
        self.listdata = []
        return QVariant
        
class AboutDialogWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setFixedSize(600,400)
        self.setWindowTitle('About')
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("NatureGlass.jpg")))
        self.setPalette(palette)
        self.setLayout(contenedor)
        
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        contenedor.addWidget(QLabel())
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(18)
        
        labelCarlos = QLabel('Carlos Hernan Guadir Aza')
        labelDario = QLabel('Dario Fernando Criollo')
        labelInfo = QLabel('Telf: 3186522909')
        labelUn = QLabel('Ingenieria de Sistemas - UDENAR')
        labelTime = QLabel('2015 - 2016')
        labelCarlos.setAlignment(QtCore.Qt.AlignCenter)
        labelDario.setAlignment(QtCore.Qt.AlignCenter)
        labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        labelUn.setAlignment(QtCore.Qt.AlignCenter)
        labelTime.setAlignment(QtCore.Qt.AlignCenter)
        
        labelCarlos.setFont(font)
        labelDario.setFont(font)
        labelInfo.setFont(font)
        labelUn.setFont(font)
        labelTime.setFont(font)
        contenedor.addWidget(labelCarlos)
        contenedor.addWidget(labelDario)
        contenedor.addWidget(labelInfo)
        contenedor.addWidget(labelUn)
        contenedor.addWidget(labelTime)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.setWindowTitle(('Importaciones Colombia').center(150, " "))
    screen = QtGui.QDesktopWidget().screenGeometry()
    size = MyWindow.geometry()
    MyWindow.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)
    MyWindow.show()
    app.exec_()
