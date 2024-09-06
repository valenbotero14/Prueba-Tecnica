#Implementacion del procesamiento de los datos (logica)


import pandas as pd  # Importa la biblioteca pandas para el manejo de datos.
from PyQt5.QtWidgets import QFileDialog, QMessageBox  # Importa componentes de PyQt5 para interfaces gráficas y diálogos.

class DataProcessor:
    """
    Clase para procesar datos de un archivo Excel, aplicar filtros y exportar resultados.
    """
    def __init__(self):
        # Inicializa la clase con atributos predeterminados.
        self.df = None  # DataFrame para almacenar los datos cargados.
        self.original_df = None  # Copia del DataFrame original para revertir filtros.
        self.filePath = None  # Ruta del archivo seleccionado.
        self.maxMonths = None  # Valor máximo de meses basado en los datos.
        self.numberOfMonths = None  # Número de meses que se deben considerar.

#--------------------------------------------------------------------------------------------------------------

    def selectFile(self):
        """
        Permite al usuario seleccionar un archivo Excel y carga los datos en un DataFrame.
        Si el archivo está vacío, muestra un mensaje de error.
        """
        options = QFileDialog.Options()  # Define las opciones del diálogo de selección de archivos.
        fileName, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)", options=options)
        # Muestra un diálogo para seleccionar un archivo Excel.

        if fileName:
            self.filePath = fileName  # Guarda la ruta del archivo seleccionado.

            try:
                self.df = pd.read_excel(fileName)  # Carga los datos del archivo Excel en un DataFrame.

                # Verifica si el DataFrame está vacío.
                if self.df.empty:
                    QMessageBox.critical(None, "Error", "El archivo seleccionado está vacío.")  # Muestra un mensaje de error.
                    return None  # Sal de la función si el DataFrame está vacío.

                self.original_df = self.df.copy()  # Guarda una copia del DataFrame original.
                self.update_max_months()  # Actualiza el valor máximo de meses.
                print(f"Archivo seleccionado: {fileName}")  # Imprime la ruta del archivo seleccionado.
                print(f"Datos cargados. Primeras filas:\n{self.df.head()}")  # Imprime las primeras filas del DataFrame cargado.
                print(f"Meses máximos encontrados: {self.maxMonths}")  # Imprime el valor máximo de meses encontrado.

                return fileName  # Devuelve la ruta del archivo seleccionado.

            except Exception as e:
                QMessageBox.critical(None, "Error", f"Ha ocurrido un error al cargar el archivo: {e}")  # Muestra un mensaje de error si ocurre una excepción.
                return None  # Devuelve None en caso de error.

#--------------------------------------------------------------------------------------------------------------

    def update_max_months(self):
        """
        Actualiza el valor máximo de meses basado en la columna 'Mes'.
        """
        if self.df is not None and 'Mes' in self.df.columns:
            self.maxMonths = self.df['Mes'].max()  # Actualiza el valor máximo de meses.
        else:
            self.maxMonths = None  # Si no hay datos o la columna no existe, establece el valor en None.
        print(f"Max meses actualizado: {self.maxMonths}")  # Imprime el valor máximo de meses actualizado.

#--------------------------------------------------------------------------------------------------------------

    def acceptNumberOfMonths(self, number_of_months):
        """
        Acepta un número de meses y valida que esté dentro del rango permitido.
        """
        try:
            number_of_months = int(number_of_months)  # Intenta convertir el valor a entero.
            if self.maxMonths is not None and 0 <= number_of_months <= self.maxMonths:
                self.numberOfMonths = number_of_months  # Si es válido, guarda el número de meses.
                print(f"Número de meses aceptado: {self.numberOfMonths}")  # Imprime el número de meses aceptado.
                return True  # Devuelve True indicando que el número de meses es válido.
            else:
                print(f"Número de meses no válido: {number_of_months}")  # Imprime que el número de meses no es válido.
                return False  # Devuelve False indicando que el número de meses no es válido.
        except ValueError:
            print(f"Error en la conversión del valor: {number_of_months}")  # Imprime un error si la conversión falla.
            return False  # Devuelve False indicando que hubo un error en la conversión.

#--------------------------------------------------------------------------------------------------------------

    def filterType(self, type_filter):
        """
        Filtra los datos en el DataFrame basado en el tipo de generación.
        """
        if self.df is not None and type_filter:
            self.df = self.df[self.df['Tipo Generacion'] == type_filter]  # Filtra por tipo de generación
            if self.df.empty:
                return False  # Devuelve False si el DataFrame filtrado está vacío
            return True  # Devuelve True si el filtrado fue exitoso
        return False  # Devuelve False si no hay datos para filtrar o no se proporcionó un filtro

#--------------------------------------------------------------------------------------------------------------

    def filterData(self, data_filter):
        """
        Filtra los datos en el DataFrame basado en el estado de generación.
        """
        if self.df is not None and data_filter:
            self.df = self.df[self.df['Estado Recurso'] == data_filter]  # Filtra por tipo de generación
            if self.df.empty:
                return False  # Devuelve False si el DataFrame filtrado está vacío
            return True  # Devuelve True si el filtrado fue exitoso
        return False  # Devuelve False si no hay datos para filtrar o no se proporcionó un filtro

#--------------------------------------------------------------------------------------------------------------

    def clearFilter(self):
        """
        Reestablece el DataFrame a su estado original.
        """
        if self.original_df is not None:
            self.df = self.original_df.copy()  # Restaura el DataFrame original.
            return True  # Devuelve True indicando que se restableció correctamente.
        return False  # Devuelve False si no se pudo restablecer.

#--------------------------------------------------------------------------------------------------------------

    def exportData(self, category):
        """
        Exporta los datos filtrados a un archivo Excel basado en la categoría especificada.
        """
        if self.df is not None and self.numberOfMonths is not None:
            try:
                self.df['Fecha'] = pd.to_datetime(self.df[['Año', 'Mes']].astype(str).agg('-'.join, axis=1), format='%Y-%m', errors='coerce')
                # Crea una columna 'Fecha' combinando 'Año' y 'Mes' y convierte a formato de fecha.
                self.df = self.df.dropna(subset=['Fecha'])  # Elimina filas con valores nulos en la columna 'Fecha'.
                self.df = self.df.sort_values(by='Fecha', ascending=False)  # Ordena el DataFrame por la columna 'Fecha' en orden descendente.

                if not self.df.empty:
                    latest_date = self.df['Fecha'].max()  # Obtiene la fecha más reciente en el DataFrame.
                    start_date = latest_date - pd.DateOffset(months=self.numberOfMonths - 1)  # Calcula la fecha de inicio en función del número de meses.
                    df_filtered = self.df[self.df['Fecha'] >= start_date]  # Filtra los datos basados en el rango de fechas.

                    if df_filtered.empty:
                        return False  # Devuelve False si no hay datos después del filtrado.

                    if category == "Recurso":
                        df_grouped = df_filtered.groupby(['Fecha', 'Recurso'])['Generación'].sum().reset_index()
                        column_to_export = 'Recurso'
                    elif category == "Agente Generacion":
                        df_grouped = df_filtered.groupby(['Fecha', 'Agente Generacion'])['Generación'].sum().reset_index()
                        column_to_export = 'Agente Generacion'
                    else:
                        print(f"Categoría no válida: {category}")  # Imprime un error si la categoría no es válida.
                        return False  # Devuelve False si la categoría no es válida.

                    df_grouped = df_grouped.sort_values(by=['Fecha', 'Generación'], ascending=[False, False])
                    df_grouped = df_grouped.groupby('Fecha').apply(lambda x: x.nlargest(1, 'Generación')).reset_index(drop=True)
                    # Ordena por 'Fecha' y 'Generación' en orden descendente y selecciona el valor más grande para cada fecha.

                    df_grouped['Mes'] = df_grouped['Fecha'].dt.strftime('%B')  # Añade una columna 'Mes' en formato de nombre del mes.
                    df_export = df_grouped[['Mes', column_to_export]]  # Selecciona las columnas 'Mes' y la columna correspondiente a la categoría para exportar.

                    fileName, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)")
                    # Muestra un diálogo para guardar el archivo exportado.
                    if fileName:
                        df_export.to_excel(fileName, index=False)  # Guarda el DataFrame exportado en un archivo Excel.
                        return True  # Devuelve True si la exportación fue exitosa.
                    return False  # Devuelve False si el DataFrame estaba vacío o hubo un error.

            except Exception as e:
                print(f"Error en exportData: {e}")  # Imprime un error si ocurre una excepción durante la exportación.
                return False  # Devuelve False indicando que hubo un error durante la exportación.

#---------------------------------------------------------------------------------------------------------------------------------------------

    def exportDataG(self, category):
        """
        Exporta los datos filtrados a un archivo Excel basado en la categoría especificada.
        """
        if self.df is not None and self.numberOfMonths is not None:
            try:
                self.df['Fecha'] = pd.to_datetime(self.df[['Año', 'Mes']].astype(str).agg('-'.join, axis=1), format='%Y-%m', errors='coerce')
                # Crea una columna 'Fecha' combinando 'Año' y 'Mes' y convierte a formato de fecha.
                self.df = self.df.dropna(subset=['Fecha'])  # Elimina filas con valores nulos en la columna 'Fecha'.
                self.df = self.df.sort_values(by='Fecha', ascending=False)  # Ordena el DataFrame por la columna 'Fecha' en orden descendente.

                if not self.df.empty:
                    latest_date = self.df['Fecha'].max()  # Obtiene la fecha más reciente en el DataFrame.
                    start_date = latest_date - pd.DateOffset(months=self.numberOfMonths - 1)  # Calcula la fecha de inicio en función del número de meses.
                    df_filtered = self.df[self.df['Fecha'] >= start_date]  # Filtra los datos basados en el rango de fechas.

                    if df_filtered.empty:
                        return False  # Devuelve False si no hay datos después del filtrado.

                    if category == "Recurso":
                        df_grouped = df_filtered.groupby(['Fecha', 'Recurso'])['Generación'].sum().reset_index()
                        column_to_export = 'Recurso'
                    elif category == "Agente Generacion":
                        df_grouped = df_filtered.groupby(['Fecha', 'Agente Generacion'])['Generación'].sum().reset_index()
                        column_to_export = 'Agente Generacion'
                    else:
                        print(f"Categoría no válida: {category}")  # Imprime un error si la categoría no es válida.
                        return False  # Devuelve False si la categoría no es válida.

                    df_grouped = df_grouped.sort_values(by=['Fecha', 'Generación'], ascending=[False, False])
                    df_grouped = df_grouped.groupby('Fecha').apply(lambda x: x.nlargest(1, 'Generación')).reset_index(drop=True)
                    # Ordena por 'Fecha' y 'Generación' en orden descendente y selecciona el valor más grande para cada fecha.

                    df_grouped['Mes'] = df_grouped['Fecha'].dt.strftime('%B')  # Añade una columna 'Mes' en formato de nombre del mes.
                    df_export = df_grouped[['Mes', column_to_export, 'Generación']]  # Selecciona las columnas 'Mes' y la columna correspondiente a la categoría para exportar.

                    fileName, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)")
                    # Muestra un diálogo para guardar el archivo exportado.
                    if fileName:
                        df_export.to_excel(fileName, index=False)  # Guarda el DataFrame exportado en un archivo Excel.
                        return True  # Devuelve True si la exportación fue exitosa.
                    return False  # Devuelve False si el DataFrame estaba vacío o hubo un error.

            except Exception as e:
                print(f"Error en exportData: {e}")  # Imprime un error si ocurre una excepción durante la exportación.
                return False  # Devuelve False indicando que hubo un error durante la exportación.