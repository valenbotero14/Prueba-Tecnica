# interfaz gráfica de usuario.

from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        # Configuración inicial del formulario
        Form.setObjectName("Form")
        Form.resize(765, 558)

        # Etiquetas
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(410, 20, 171, 31))
        self.label.setObjectName("label")

        self.filePathLabel = QtWidgets.QLabel(Form)
        self.filePathLabel.setGeometry(QtCore.QRect(30, 100, 300, 28))
        self.filePathLabel.setObjectName("filePathLabel")
        self.filePathLabel.setText("Ruta del archivo")

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 171, 31))
        self.label_7.setObjectName("label_7")

        # Botones
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(430, 90, 121, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 460, 151, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 520, 121, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 330, 151, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 60, 111, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 360, 151, 28))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 450, 151, 28))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(590, 480, 151, 28))
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 500, 231, 28))
        self.pushButton_9.setObjectName("pushButton_9")

        # Campos de texto
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 60, 121, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        # Grupo de opciones: Categoría de datos
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 170, 151, 80))
        self.groupBox.setObjectName("groupBox")

        # Radio Buttons dentro del grupo de Categoría de datos
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 131, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        # Grupo de opciones: Estado de operación
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 170, 141, 141))
        self.groupBox_2.setObjectName("groupBox_2")

        # Radio Buttons dentro del grupo de Estado de operación
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 80, 95, 20))
        self.radioButton_7.setObjectName("radioButton_7")

        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 110, 95, 20))
        self.radioButton_8.setObjectName("radioButton_8")

        # Grupo de opciones: Tipo de energía
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(590, 230, 141, 211))
        self.groupBox_3.setObjectName("groupBox_3")

        # Radio Buttons dentro del grupo de Tipo de energía
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radioButton_5.setObjectName("radioButton_5")

        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.radioButton_6.setObjectName("radioButton_6")

        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_9.setGeometry(QtCore.QRect(10, 80, 101, 20))
        self.radioButton_9.setObjectName("radioButton_9")

        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_10.setGeometry(QtCore.QRect(10, 110, 95, 20))
        self.radioButton_10.setObjectName("radioButton_10")

        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 140, 95, 20))
        self.radioButton_11.setObjectName("radioButton_11")

        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_12.setGeometry(QtCore.QRect(10, 170, 95, 20))
        self.radioButton_12.setObjectName("radioButton_12")

        # Traducción de textos y etiquetas
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        # Configuración de textos para etiquetas
        self.label.setText(_translate("Form", "Cantidad de meses a revisar"))
        self.filePathLabel.setText(_translate("Form", "Ruta del archivo"))
        self.label_7.setText(_translate("Form", "Seleccionar archivo"))

        # Configuración de textos para botones
        self.pushButton.setText(_translate("Form", "Aceptar Cantidad"))
        self.pushButton_2.setText(_translate("Form", "Exportar datos a excel"))
        self.pushButton_9.setText(_translate("Form", "Exportar datos a excel con Genreacion"))
        self.pushButton_3.setText(_translate("Form", "Cerrar aplicación"))
        self.pushButton_4.setText(_translate("Form", "Filtrar Estado"))
        self.pushButton_5.setText(_translate("Form", "Archivo"))
        self.pushButton_6.setText(_translate("Form", "Eliminar Filtro"))
        self.pushButton_7.setText(_translate("Form", "Filtrar Tipo"))
        self.pushButton_8.setText(_translate("Form", "Eliminar Filtro"))

        # Configuración de títulos para grupos
        self.groupBox.setTitle(_translate("Form", "Categoría de datos"))
        self.groupBox_2.setTitle(_translate("Form", "Estado de operación"))
        self.groupBox_3.setTitle(_translate("Form", "Tipo de energía"))

        # Configuración de textos para radio buttons en el grupo de Categoría de datos
        self.radioButton.setText(_translate("Form", "Recurso"))
        self.radioButton_2.setText(_translate("Form", "Agente generación"))

        # Configuración de textos para radio buttons en el grupo de Estado de operación
        self.radioButton_3.setText(_translate("Form", "Inactivo"))
        self.radioButton_4.setText(_translate("Form", "Operación"))
        self.radioButton_7.setText(_translate("Form", "Pruebas"))
        self.radioButton_8.setText(_translate("Form", "Todas"))

        # Configuración de textos para radio buttons en el grupo de Tipo de energía
        self.radioButton_5.setText(_translate("Form", "Cogenerador"))
        self.radioButton_6.setText(_translate("Form", "Eólica"))
        self.radioButton_9.setText(_translate("Form", "Hidráulica"))
        self.radioButton_10.setText(_translate("Form", "Solar"))
        self.radioButton_11.setText(_translate("Form", "Térmica"))
        self.radioButton_12.setText(_translate("Form", "Todas"))
