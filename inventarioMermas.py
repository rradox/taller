import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox

class InventarioMermas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inventario de Mermas')
        self.resize(800, 600)  # Establecer tamaño de la ventana

        # Crear tabla para mostrar el inventario de mermas
        self.tabla_mermas = QTableWidget(self)
        self.tabla_mermas.setColumnCount(3)
        self.tabla_mermas.setHorizontalHeaderLabels(['Tipo', 'Descripción', 'Cantidad'])

        # Crear botón para eliminar las mermas
        btn_eliminar_mermas = QPushButton('Eliminar Mermas')
        btn_eliminar_mermas.clicked.connect(self.eliminar_mermas)

        # Crear layout vertical y agregar la tabla y el botón
        layout = QVBoxLayout()
        layout.addWidget(self.tabla_mermas)
        layout.addWidget(btn_eliminar_mermas)

        # Crear widget central y establecer el layout
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer el widget central en la ventana principal
        self.setCentralWidget(widget)

        # Cargar el inventario de mermas
        self.cargar_inventario_mermas()

    def cargar_inventario_mermas(self):
        inventario_mermas = []

        # Cargar mermas de carne
        with open('mermas.csv', 'r', newline='', encoding="utf-8-sig") as archivo_carne:
            lector_csv_carne = csv.reader(archivo_carne)
            for mermas in lector_csv_carne:
                tipo = 'Carne'
                descripcion = mermas[0]
                cantidad = mermas[3]
                inventario_mermas.append([tipo, descripcion, cantidad])

        # Cargar mermas de verduras
        with open('mermas_verduras.csv', 'r', newline='', encoding="utf-8-sig") as archivo_verduras:
            lector_csv_verduras = csv.reader(archivo_verduras)
            for mermas_verduras in lector_csv_verduras:
                tipo = 'Verdura'
                descripcion = mermas_verduras[0]
                cantidad = mermas_verduras[3]
                inventario_mermas.append([tipo, descripcion, cantidad])

        # Cargar mermas de mariscos
        with open('mermas_mariscos.csv', 'r', newline='', encoding="utf-8-sig") as archivo_mariscos:
            lector_csv_mariscos = csv.reader(archivo_mariscos)
            for mermas_mariscos in lector_csv_mariscos:
                tipo = 'Marisco'
                descripcion = mermas_mariscos[0]
                cantidad = mermas_mariscos[3]
                inventario_mermas.append([tipo, descripcion, cantidad])

        # Cargar mermas de pescados
        with open('mermas_pescados.csv', 'r', newline='', encoding="utf-8-sig") as archivo_pescados:
            lector_csv_pescados = csv.reader(archivo_pescados)
            for mermas_pescados in lector_csv_pescados:
                tipo = 'Pescado'
                descripcion = mermas_pescados[0]
                cantidad = mermas_pescados[3]
                inventario_mermas.append([tipo, descripcion, cantidad])

        # Cargar mermas de alimentos imperecederos
        with open('mermas_imperecederos.csv', 'r', newline='', encoding="utf-8-sig") as archivo_imperecederos:
            lector_csv_imperecederos = csv.reader(archivo_imperecederos)
            for mermas_imperecederos in lector_csv_imperecederos:
                tipo = 'Imperecedero'
                descripcion = mermas_imperecederos[0]
                cantidad = mermas_imperecederos[2]
                inventario_mermas.append([tipo, descripcion, cantidad])

        num_filas = len(inventario_mermas)
        self.tabla_mermas.setRowCount(num_filas)

        for fila, merma in enumerate(inventario_mermas):
            for col, valor in enumerate(merma):
                item = QTableWidgetItem(valor)
                self.tabla_mermas.setItem(fila, col, item)

    def eliminar_mermas(self):
        eliminar_confirmado = QMessageBox.question(self, 'Eliminar Mermas', '¿Está seguro de eliminar todas las mermas?', QMessageBox.Yes | QMessageBox.No)
        if eliminar_confirmado ==QMessageBox.Yes:
            self.eliminar_mermas_carne()
            self.eliminar_mermas_verduras()
            self.eliminar_mermas_mariscos()
            self.eliminar_mermas_pescados()
            self.eliminar_mermas_imperecederos()
            self.tabla_mermas.setRowCount(0)
            QMessageBox.information(self, 'Mermas Eliminadas', 'Todas las mermas han sido eliminadas correctamente.')

    def eliminar_mermas_carne(self):
        with open('mermas.csv', 'w', newline='', encoding="utf-8-sig") as archivo_carne:
            escritor_csv_carne = csv.writer(archivo_carne)
            escritor_csv_carne.writerow(['Tipo', 'Descripción', 'Cantidad'])

    def eliminar_mermas_verduras(self):
        with open('mermas_verduras.csv', 'w', newline='', encoding="utf-8-sig") as archivo_verduras:
            escritor_csv_verduras = csv.writer(archivo_verduras)
            escritor_csv_verduras.writerow(['Tipo', 'Descripción', 'Cantidad'])

    def eliminar_mermas_mariscos(self):
        with open('mermas_mariscos.csv', 'w', newline='', encoding="utf-8-sig") as archivo_mariscos:
            escritor_csv_mariscos = csv.writer(archivo_mariscos)
            escritor_csv_mariscos.writerow(['Tipo', 'Descripción', 'Cantidad'])

    def eliminar_mermas_pescados(self):
        with open('mermas_pescados.csv', 'w', newline='', encoding="utf-8-sig") as archivo_pescados:
            escritor_csv_pescados = csv.writer(archivo_pescados)
            escritor_csv_pescados.writerow(['Tipo', 'Descripción', 'Cantidad'])

    def eliminar_mermas_imperecederos(self):
        with open('mermas_imperecederos.csv', 'w', newline='', encoding="utf-8-sig") as archivo_imperecederos:
            escritor_csv_imperecederos = csv.writer(archivo_imperecederos)
            escritor_csv_imperecederos.writerow(['Tipo', 'Descripción', 'Cantidad'])

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana_mermas = InventarioMermas()
    ventana_mermas.show()

    sys.exit(app.exec_())
