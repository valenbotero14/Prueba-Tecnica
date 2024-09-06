# punto de entrada de la aplicación y combinará el código de la interfaz y el procesamiento de datos

import sys  # Importa el módulo sys, que proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete de Python
from PyQt5 import QtWidgets  # Importa el módulo QtWidgets de PyQt5, que contiene las clases para construir la interfaz gráfica
from interface import Ui_Form  # Importa la clase Ui_Form del módulo interface, que define la interfaz gráfica
from App_Logic import DataProcessor  # Importa la clase DataProcessor del módulo App_Logic, que maneja la lógica de procesamiento de datos

class MyApp(QtWidgets.QWidget, Ui_Form):
    # Define una clase llamada MyApp que hereda de QtWidgets.QWidget y Ui_Form

    def __init__(self):
        # Constructor de la clase MyApp
        super().__init__()  # Llama al constructor de la clase base QtWidgets.QWidget para inicializar la instancia
        self.setupUi(self)  # Configura la interfaz gráfica utilizando el método setupUi proporcionado por Ui_Form
        self.data_processor = DataProcessor()  # Crea una instancia de DataProcessor para manejar la lógica de datos

        # Conecta los botones de la interfaz con sus respectivos métodos de manejo de eventos
        self.pushButton.clicked.connect(self.handleAcceptNumberOfMonths)
        self.pushButton_5.clicked.connect(self.handleSelectFile)
        self.pushButton_2.clicked.connect(self.handleExportData)
        self.pushButton_9.clicked.connect(self.handleExportDataG)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.applyStateFilter)
        self.pushButton_6.clicked.connect(self.clearFilter)
        self.pushButton_7.clicked.connect(self.applyTypeFilter)
        self.pushButton_8.clicked.connect(self.clearFilter)

#--------------------------------------------------------------------------------------------------------------

    def handleSelectFile(self):
        """Maneja la selección de archivo y actualiza la etiqueta del camino del archivo."""
        file_name = self.data_processor.selectFile()  # Llama al método selectFile de DataProcessor para abrir un diálogo de selección de archivo
        if file_name:  # Verifica si se ha seleccionado un archivo
            self.filePathLabel.setText(f"Archivo seleccionado: {file_name}")  # Actualiza la etiqueta con el nombre del archivo seleccionado

#--------------------------------------------------------------------------------------------------------------

    def handleAcceptNumberOfMonths(self):
        """Acepta el número de meses e informa al usuario."""
        if self.data_processor.acceptNumberOfMonths(self.lineEdit_2.text()):  # Llama al método acceptNumberOfMonths con el texto del campo de entrada
            QtWidgets.QMessageBox.information(self, "Éxito", "Número de meses aceptado.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de éxito
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Ingrese un número entero válido para los meses.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de error si el número no es válido

#--------------------------------------------------------------------------------------------------------------

    def applyStateFilter(self):
        """Aplica un filtro de estado basado en el botón de radio seleccionado."""
        state_filter = self.getSelectedStateFilter()  # Obtiene el filtro de estado seleccionado
        if self.data_processor.filterData(state_filter):  # Llama al método filterData con el filtro de estado
            QtWidgets.QMessageBox.information(self, "Éxito", "Datos filtrados exitosamente.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de éxito si la filtración es exitosa
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay datos que cumplan con los filtros aplicados.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de advertencia si no se encuentran datos

#--------------------------------------------------------------------------------------------------------------

    def applyTypeFilter(self):
        """Aplica un filtro de tipo basado en el botón de radio seleccionado."""
        type_filter = self.getSelectedTypeFilter()  # Obtiene el filtro de tipo seleccionado
        if self.data_processor.filterType(type_filter):  # Llama al método filterType con el filtro de tipo
            QtWidgets.QMessageBox.information(self, "Éxito", "Datos filtrados exitosamente.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de éxito si la filtración es exitosa
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay datos que cumplan con los filtros aplicados.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de advertencia si no se encuentran datos

#--------------------------------------------------------------------------------------------------------------

    def clearFilter(self):
        """Limpia todos los filtros y desmarca todos los botones de radio."""
        if self.data_processor.clearFilter():  # Llama al método clearFilter para eliminar los filtros aplicados
            self.uncheckAllRadioButtons()  # Desmarca todos los botones de radio
            QtWidgets.QMessageBox.information(self, "Éxito", "Filtro eliminado, datos restaurados.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de éxito si los filtros se eliminan correctamente
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "No hay filtros para eliminar.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de error si no hay filtros para eliminar

#--------------------------------------------------------------------------------------------------------------

    def handleExportData(self):
        """Exporta datos basados en la categoría seleccionada."""
        category = self.getSelectedCategory()  # Obtiene la categoría seleccionada
        if category and self.data_processor.exportData(category):  # Verifica si se ha seleccionado una categoría y llama al método exportData con la categoría
            QtWidgets.QMessageBox.information(self, "Éxito", "Datos exportados con éxito.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de éxito si la exportación es exitosa
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No se pudo exportar los datos.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de advertencia si la exportación falla

#--------------------------------------------------------------------------------------------------------------

    def handleExportDataG(self):
        """Exporta datos basados en la categoría seleccionada."""
        category = self.getSelectedCategory()  # Obtiene la categoría seleccionada
        if category and self.data_processor.exportDataG(category):  # Verifica si se ha seleccionado una categoría y llama al método exportData con la categoría
            QtWidgets.QMessageBox.information(self, "Éxito", "Datos exportados con éxito.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de éxito si la exportación es exitosa
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No se pudo exportar los datos.", QtWidgets.QMessageBox.Ok)  # Muestra un mensaje de advertencia si la exportación falla

#--------------------------------------------------------------------------------------------------------------------

    def getSelectedStateFilter(self):
        """Obtiene el filtro de estado seleccionado de los botones de radio."""
        if self.radioButton_3.isChecked():  # Verifica si el botón de radio para 'INACTIVO' está seleccionado
            return 'INACTIVO'
        elif self.radioButton_4.isChecked():  # Verifica si el botón de radio para 'OPERACION' está seleccionado
            return 'OPERACION'
        elif self.radioButton_7.isChecked():  # Verifica si el botón de radio para 'PRUEBAS' está seleccionado
            return 'PRUEBAS'
        return None  # Retorna None si ningún botón de radio está seleccionado

#--------------------------------------------------------------------------------------------------------------

    def getSelectedTypeFilter(self):
        """Obtiene el filtro de tipo seleccionado de los botones de radio."""
        if self.radioButton_5.isChecked():  # Verifica si el botón de radio para 'COGENERADOR' está seleccionado
            return 'COGENERADOR'
        elif self.radioButton_6.isChecked():  # Verifica si el botón de radio para 'EOLICA' está seleccionado
            return 'EOLICA'
        elif self.radioButton_9.isChecked():  # Verifica si el botón de radio para 'HIDRAULICA' está seleccionado
            return 'HIDRAULICA'
        elif self.radioButton_10.isChecked():  # Verifica si el botón de radio para 'SOLAR' está seleccionado
            return 'SOLAR'
        elif self.radioButton_11.isChecked():  # Verifica si el botón de radio para 'TERMICA' está seleccionado
            return 'TERMICA'
        return None  # Retorna None si ningún botón de radio está seleccionado

#--------------------------------------------------------------------------------------------------------------

    def getSelectedCategory(self):
        """Obtiene la categoría seleccionada de los botones de radio."""
        if self.radioButton.isChecked():  # Verifica si el botón de radio para 'Recurso' está seleccionado
            return "Recurso"
        elif self.radioButton_2.isChecked():  # Verifica si el botón de radio para 'Agente Generacion' está seleccionado
            return "Agente Generacion"
        return None  # Retorna None si ningún botón de radio está seleccionado

#--------------------------------------------------------------------------------------------------------------

    def uncheckAllRadioButtons(self):
        """Desmarca todos los botones de radio."""
        for button in [self.radioButton_5, self.radioButton_6, self.radioButton_9,
                        self.radioButton_10, self.radioButton_11, self.radioButton_3,
                        self.radioButton_4, self.radioButton_7, self.radioButton_8]:
            button.setChecked(False)  # Desmarca cada botón de radio en la lista

#--------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Crea una instancia de QApplication, que gestiona la GUI
    window = MyApp()  # Crea una instancia de MyApp, que es la ventana principal
    window.show()  # Muestra la ventana principal
    sys.exit(app.exec_())  # Ejecuta el bucle de eventos de la aplicación y sale cuando termina
