
import sys
import os
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QAction, QMenuBar, QFileDialog, QPushButton, QToolBar

class InventarioRestaurante(QMainWindow):
    # __init__: None -> None
    # Corresponde al método constructor de la clase InventarioRestaurante
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inventario del Restaurante')
        self.inventario = []
        self.nombre_archivo = 'inventario.csv'  # Nombre del archivo CSV

        # Crear una barra de menú
        menu_bar = self.menuBar()
        # Crear el menú "Archivo" y sus acciones (Guardar y Cargar)
        menu_archivo = menu_bar.addMenu('Archivo')

        # El botón 'Guardar' nos permitirá guardar el inventario que se esté mostrando en la interfaz
        accion_guardar = QAction('Guardar', self)
        accion_guardar.triggered.connect(self.guardar_inventario)
        menu_archivo.addAction(accion_guardar)

        # El botón 'Cargar' nos permitirá cargar algún inventario previamente guardado, que sea necesariamente de tipo csv
        accion_cargar = QAction('Cargar', self)
        accion_cargar.triggered.connect(self.cargar_inventario)
        menu_archivo.addAction(accion_cargar)

        # Crear la tabla que muestra el inventario del restaurante
        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(['Plato', 'Cantidad'])

        # Ajustar el tamaño de las columnas
        self.tabla.resizeColumnsToContents()

        # Se agrega la tabla al layout principal
        self.setCentralWidget(self.tabla)

        # Se establece la barra de menú en la ventana principal
        self.setMenuBar(menu_bar)

        # Se crea la barra de herramientas
        barra_herramientas = QToolBar()
        self.addToolBar(barra_herramientas)
        
        # 'Agregar fila' nos permite agregar filas a la tabla del inventario del restaurante
        # pudiendo así agregar otro tipo de alimento y su stock
        self.boton_agregar_fila = QPushButton('Agregar Fila', self)
        self.boton_agregar_fila.clicked.connect(self.agregar_fila)
        barra_herramientas.addWidget(self.boton_agregar_fila)

        # 'Eliminar fila' nos permite quitar filas a la tabla del inventario del restaurante
        self.boton_eliminar_fila = QPushButton('Eliminar Fila', self)
        self.boton_eliminar_fila.clicked.connect(self.eliminar_fila)
        barra_herramientas.addWidget(self.boton_eliminar_fila)

        self.cargar_inventario()  # Cargar inventario al iniciar la aplicación
    
    # agregar_plato: nombre_plato cantidad -> None
    # Nos permite agregar un plato a la tabla del inventario del restaurante
    def agregar_plato(self, nombre_plato, cantidad):
        num_filas = self.tabla.rowCount()
        self.tabla.insertRow(num_filas)

        item_plato = QTableWidgetItem(nombre_plato)
        self.tabla.setItem(num_filas, 0, item_plato)

        item_cantidad = QTableWidgetItem(str(cantidad))
        self.tabla.setItem(num_filas, 1, item_cantidad)

        self.inventario.append([nombre_plato, cantidad])  # Agregar al inventario

    # Aquí es donde se hace uso del módulo os, ya que nos interesa guardar o cargar ciertos inventarios

    # guardar_inventario: None -> None
    # Nos permite guardar el inventario en un archivo csv
    def guardar_inventario(self):
        ruta_script = os.path.abspath(__file__)
        directorio_script = os.path.dirname(ruta_script)
        ruta_archivo = os.path.join(directorio_script, self.nombre_archivo)

        with open(ruta_archivo, 'w', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            for fila in range(self.tabla.rowCount()):
                nombre_plato = self.tabla.item(fila, 0).text()
                cantidad = self.tabla.item(fila, 1).text()
                escritor_csv.writerow([nombre_plato, cantidad])

    # cargar_inventario: None -> None
    # Nos permite cargar el inventario previamente creado
    def cargar_inventario(self):
        ruta_script = os.path.abspath(__file__)
        directorio_script = os.path.dirname(ruta_script)
        ruta_archivo = os.path.join(directorio_script, self.nombre_archivo)

        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r') as archivo:
                lector_csv = csv.reader(archivo)
                platos_cargados = list(lector_csv)  # Leer todos los platos desde el archivo

            # Eliminar todos los platos existentes en el inventario
            self.inventario.clear()

            # Eliminar todas las filas existentes en la tabla
            self.tabla.setRowCount(0)

            # Agregar los platos cargados desde el archivo
            for datos_fila in platos_cargados:
                if len(datos_fila) == 2:
                    nombre_plato, cantidad = datos_fila
                    self.agregar_plato(nombre_plato, int(cantidad))

            # Ajustar el tamaño de las columnas
            self.tabla.resizeColumnsToContents()




   # agregar_fila: None -> None
    # Nos permite agregar una fila a la tabla del inventario del restaurante
    def agregar_fila(self):  
        self.tabla.insertRow(self.tabla.rowCount())

    # eliminar_fila: None -> None
    # Nos permite quitar una fila a la tabla del inventario del restaurante
    def eliminar_fila(self):  
        filas_seleccionadas = self.tabla.selectionModel().selectedRows()
        filas_seleccionadas.reverse()  # Reversar la lista para evitar problemas al eliminar filas
        for fila in filas_seleccionadas:
            self.tabla.removeRow(fila.row())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = InventarioRestaurante()
    ventana.show()
    sys.exit(app.exec_())

    