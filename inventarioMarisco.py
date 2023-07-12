import sys
import csv
from datetime import date, timedelta
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class InventarioMariscos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inventario de Mariscos')
        self.resize(800, 600)  # Establecer tamaño de la ventana

        # Crear etiquetas y campos de texto para el ingreso de mariscos
        label_tipo = QLabel('Tipo:')
        self.input_tipo = QLineEdit()

        label_fecha_caducidad = QLabel('Fecha de Caducidad (YYYY-MM-DD):')
        self.input_fecha_caducidad = QLineEdit()

        label_cantidad = QLabel('Cantidad:')
        self.input_cantidad = QLineEdit()

        # Crear botones para agregar y eliminar mariscos
        btn_agregar = QPushButton('Agregar')
        btn_agregar.clicked.connect(self.agregar_marisco)

        btn_eliminar = QPushButton('Eliminar')
        btn_eliminar.clicked.connect(self.eliminar_marisco)

        # Crear tabla para mostrar el inventario de mariscos
        self.tabla_inventario = QTableWidget(self)
        self.tabla_inventario.setColumnCount(4)
        self.tabla_inventario.setHorizontalHeaderLabels(['Tipo', 'Fecha de Caducidad', 'Estado', 'Cantidad'])

        # Crear layout vertical y agregar los widgets
        layout = QVBoxLayout()
        layout.addWidget(label_tipo)
        layout.addWidget(self.input_tipo)
        layout.addWidget(label_fecha_caducidad)
        layout.addWidget(self.input_fecha_caducidad)
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

        # Crear el inventario como una lista de mariscos
        self.inventario = []

        # Cargar inventario previo si existe
        self.cargar_inventario()

        # Generar alertas
        self.generar_alertas()

    def agregar_marisco(self):
        tipo = self.input_tipo.text()
        fecha_caducidad = self.input_fecha_caducidad.text()
        cantidad = self.input_cantidad.text()

        if tipo and fecha_caducidad and cantidad:
            marisco = [tipo, fecha_caducidad, 'Activa', cantidad]
            self.inventario.append(marisco)

            num_filas = self.tabla_inventario.rowCount()
            self.tabla_inventario.insertRow(num_filas)

            for col, valor in enumerate(marisco):
                item = QTableWidgetItem(valor)
                self.tabla_inventario.setItem(num_filas, col, item)

            self.input_tipo.clear()
            self.input_fecha_caducidad.clear()
            self.input_cantidad.clear()

            self.guardar_inventario()
        else:
            QMessageBox.warning(self, 'Error', 'Por favor complete todos los campos.')

    def eliminar_marisco(self):
        filas_seleccionadas = self.tabla_inventario.selectionModel().selectedRows()
        filas_seleccionadas.reverse()
        mariscos_eliminados = []

        for fila in filas_seleccionadas:
            marisco = self.inventario[fila.row()]
            mariscos_eliminados.append(marisco)
            self.tabla_inventario.removeRow(fila.row())
            del self.inventario[fila.row()]

        self.guardar_inventario()
        self.guardar_mermas(mariscos_eliminados)

    def guardar_inventario(self):
        with open('mariscos.csv', 'w', newline='',encoding="utf-8-sig") as archivo:
            escritor_csv = csv.writer(archivo)
            for marisco in self.inventario:
                escritor_csv.writerow(marisco)

    def cargar_inventario(self):
        try:
            with open('mariscos.csv', 'r',encoding="utf-8-sig") as archivo:
                lector_csv = csv.reader(archivo)
                self.inventario = list(lector_csv)

            num_filas = len(self.inventario)
            self.tabla_inventario.setRowCount(num_filas)

            for fila, marisco in enumerate(self.inventario):
                for col, valor in enumerate(marisco):
                    item = QTableWidgetItem(valor)
                    self.tabla_inventario.setItem(fila, col, item)

        except FileNotFoundError:
            self.inventario = []

    def generar_alertas(self):
        fecha_actual = date.today()

        for fila, marisco in enumerate(self.inventario):
            fecha_caducidad = date.fromisoformat(marisco[1])

            if fecha_caducidad < fecha_actual:
                self.tabla_inventario.item(fila, 1).setBackground(QColor('red'))
                QMessageBox.warning(self, 'Alerta', f'El marisco de tipo {marisco[0]} ha caducado.')
            elif fecha_caducidad - fecha_actual <= timedelta(days=3):
                self.tabla_inventario.item(fila, 1).setBackground(QColor('yellow'))
                QMessageBox.warning(self, 'Alerta', f'El marisco de tipo {marisco[0]} está cerca de su fecha de caducidad.')

    def guardar_mermas(self, mariscos_eliminados):
        with open('mermas_mariscos.csv', 'a', newline='',encoding="utf-8-sig") as archivo:
            escritor_csv = csv.writer(archivo)
            for marisco in mariscos_eliminados:
                marisco.append('Eliminada')
                escritor_csv.writerow(marisco)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = InventarioMariscos()
    ventana.show()
    sys.exit(app.exec_())
