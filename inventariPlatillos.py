import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QMessageBox

class VentanaPlatillosRegistrados(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Platillos Registrados')
        self.resize(600, 400)

        self.table_platillos = QTableWidget()
        self.table_platillos.setColumnCount(5)
        self.table_platillos.setHorizontalHeaderLabels(['Nombre', 'Carne', 'Verduras', 'Mariscos', 'Pescados'])

        self.btn_eliminar = QPushButton('Eliminar Platillo')
        self.btn_eliminar.clicked.connect(self.eliminar_platillo)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_platillos)
        self.layout.addWidget(self.btn_eliminar)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.cargar_platillos()

    def cargar_platillos(self):
        with open('platillos.csv', 'r',encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            platillos = list(reader)
            self.table_platillos.setRowCount(len(platillos))

            for row, platillo in enumerate(platillos):
                for col, data in enumerate(platillo):
                    self.table_platillos.setItem(row, col, QTableWidgetItem(data))

    def eliminar_platillo(self):
        selected_row = self.table_platillos.currentRow()
        if selected_row >= 0:
            platillo = []
            for col in range(self.table_platillos.columnCount()):
                item = self.table_platillos.item(selected_row, col)
                platillo.append(item.text())

            platillo_nombre = platillo[0]
            platillo_carne = platillo[1]
            platillo_verduras = platillo[2]
            platillo_mariscos = platillo[3]
            platillo_pescados = platillo[4]

            self.actualizar_inventario('carnes.csv', platillo_carne, 1)
            self.actualizar_inventario('verduras.csv', platillo_verduras, 1)
            self.actualizar_inventario('mariscos.csv', platillo_mariscos, 1)
            self.actualizar_inventario('pescados.csv', platillo_pescados, 1)

            self.table_platillos.removeRow(selected_row)
            self.actualizar_archivo_platillos()

            QMessageBox.information(self, 'Platillo Eliminado', f'El platillo "{platillo_nombre}" ha sido eliminado.')
        else:
            QMessageBox.warning(self, 'Error', 'Por favor seleccione un platillo para eliminar.')

    def actualizar_inventario(self, archivo, ingrediente, cantidad):
        inventario_actualizado = []
        with open(archivo, 'r',encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == ingrediente:
                    cantidad_actualizada = int(row[1]) + cantidad
                    row[1] = str(cantidad_actualizada)
                inventario_actualizado.append(row)

        with open(archivo, 'w', newline='',encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerows(inventario_actualizado)

    def actualizar_archivo_platillos(self):
        platillos = []
        for row in range(self.table_platillos.rowCount()):
            platillo = []
            for col in range(self.table_platillos.columnCount()):
                item = self.table_platillos.item(row, col)
                platillo.append(item.text())
            platillos.append(platillo)

        with open('platillos.csv', 'w', newline='',encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerows(platillos)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPlatillosRegistrados()
    ventana.show()
    sys.exit(app.exec_())
