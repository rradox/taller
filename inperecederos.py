import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QMessageBox

class InventarioImperecederos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inventario de Alimentos Imperecederos')
        self.resize(800, 600)  # Establecer tamaño de la ventana

        # Crear etiquetas y campos de texto para el ingreso de alimentos imperecederos
        label_nombre = QLabel('Nombre:')
        self.input_nombre = QLineEdit()

        label_cantidad = QLabel('Cantidad:')
        self.input_cantidad = QLineEdit()

        # Crear botones para agregar y eliminar alimentos imperecederos
        btn_agregar = QPushButton('Agregar')
        btn_agregar.clicked.connect(self.agregar_alimento)

        btn_eliminar = QPushButton('Eliminar')
        btn_eliminar.clicked.connect(self.eliminar_alimento)

        # Crear tabla para mostrar el inventario de alimentos imperecederos
        self.tabla_inventario = QTableWidget(self)
        self.tabla_inventario.setColumnCount(3)
        self.tabla_inventario.setHorizontalHeaderLabels(['Nombre', 'Estado', 'Cantidad'])

        # Crear layout vertical y agregar los widgets
        layout = QVBoxLayout()
        layout.addWidget(label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(label_cantidad)
        layout.addWidget(self.input_cantidad)
        layout.addWidget(btn_agregar)
        layout.addWidget(btn_eliminar)
        layout.addWidget(self.tabla_inventario)

        # Crear widget central y establecer el layout
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer el widget central en la ventana principal
        self.setCentralWidget(widget)

        # Crear el inventario como una lista de alimentos imperecederos
        self.inventario = []

        # Cargar inventario previo si existe
        self.cargar_inventario()

    def agregar_alimento(self):
        nombre = self.input_nombre.text()
        cantidad = self.input_cantidad.text()

        if nombre and cantidad:
            alimento = [nombre, 'Activo', cantidad]
            self.inventario.append(alimento)

            num_filas = self.tabla_inventario.rowCount()
            self.tabla_inventario.insertRow(num_filas)

            for col, valor in enumerate(alimento):
                item = QTableWidgetItem(valor)
                self.tabla_inventario.setItem(num_filas, col, item)

            self.input_nombre.clear()
            self.input_cantidad.clear()

            self.guardar_inventario()
        else:
            QMessageBox.warning(self, 'Error', 'Por favor complete todos los campos.')

    def eliminar_alimento(self):
        filas_seleccionadas = self.tabla_inventario.selectionModel().selectedRows()
        filas_seleccionadas.reverse()
        alimentos_eliminados = []

        for fila in filas_seleccionadas:
            alimento = self.inventario[fila.row()]
            alimentos_eliminados.append(alimento)
            self.tabla_inventario.removeRow(fila.row())
            del self.inventario[fila.row()]

        self.guardar_inventario()
        self.guardar_mermas(alimentos_eliminados)

    def guardar_inventario(self):
        with open('alimentos_imperecederos.csv', 'w', newline='',encoding="utf-8-sig") as archivo:
            escritor_csv = csv.writer(archivo)
            for alimento in self.inventario:
                escritor_csv.writerow(alimento)

    def cargar_inventario(self):
        try:
            with open('alimentos_imperecederos.csv', 'r',encoding="utf-8-sig") as archivo:
                lector_csv = csv.reader(archivo)
                self.inventario = list(lector_csv)

            num_filas = len(self.inventario)
            self.tabla_inventario.setRowCount(num_filas)

            for fila, alimento in enumerate(self.inventario):
                for col, valor in enumerate(alimento):
                    item = QTableWidgetItem(valor)
                    self.tabla_inventario.setItem(fila, col, item)

        except FileNotFoundError:
            self.inventario = []

    def guardar_mermas(self, alimentos_eliminados):
        with open('mermas_imperecederos.csv', 'a', newline='',encoding="utf-8-sig") as archivo:
            escritor_csv = csv.writer(archivo)
            for alimento in alimentos_eliminados:
                alimento.append('Eliminado')
                escritor_csv.writerow(alimento)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = InventarioImperecederos()
    ventana.show()
    sys.exit(app.exec_())
