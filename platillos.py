import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class VentanaPlatillos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana de Platillos')
        self.resize(400, 300)

        # Cargar inventarios de pescados, carnes, mariscos y verduras desde archivos CSV
        self.inventario_pescados = self.cargar_inventario('pescados.csv')
        self.inventario_carnes = self.cargar_inventario('carnes.csv')
        self.inventario_mariscos = self.cargar_inventario('mariscos.csv')
        self.inventario_verduras = self.cargar_inventario('verduras.csv')

        # Etiquetas y campos de texto para ingresar información del platillo
        self.label_nombre = QLabel('Nombre:')
        self.input_nombre = QLineEdit()

        self.label_carne = QLabel('Carne:')
        self.combo_carne = QComboBox()
        self.combo_carne.addItems(self.inventario_carnes.keys())

        self.label_verduras = QLabel('Verduras:')
        self.combo_verduras = QComboBox()
        self.combo_verduras.addItems(self.inventario_verduras.keys())

        self.label_mariscos = QLabel('Mariscos:')
        self.combo_mariscos = QComboBox()
        self.combo_mariscos.addItems(self.inventario_mariscos.keys())

        self.label_pescados = QLabel('Pescados:')
        self.combo_pescados = QComboBox()
        self.combo_pescados.addItems(self.inventario_pescados.keys())

        # Botón para crear el platillo
        self.btn_crear_platillo = QPushButton('Crear Platillo')
        self.btn_crear_platillo.clicked.connect(self.crear_platillo)

        # Diseño del layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.label_carne)
        layout.addWidget(self.combo_carne)
        layout.addWidget(self.label_verduras)
        layout.addWidget(self.combo_verduras)
        layout.addWidget(self.label_mariscos)
        layout.addWidget(self.combo_mariscos)
        layout.addWidget(self.label_pescados)
        layout.addWidget(self.combo_pescados)
        layout.addWidget(self.btn_crear_platillo)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def cargar_inventario(self, archivo):
        inventario = {}
        with open(archivo, 'r',encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            for row in reader:
                ingrediente = row[0]
                cantidad = int(row[3])
                inventario[ingrediente] = cantidad
        return inventario

    def actualizar_inventario(self, archivo, ingrediente, cantidad):
        inventario_actualizado = []
        with open(archivo, 'r',encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == ingrediente:
                    cantidad_actualizada = int(row[3]) - cantidad
                    if cantidad_actualizada < 0:
                        QMessageBox.warning(self, 'Error', f'No hay suficiente {ingrediente} en el inventario.')
                        return False
                    row[1] = str(cantidad_actualizada)
                inventario_actualizado.append(row)
        
        with open(archivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(inventario_actualizado)

        return True

    def guardar_platillo(self, platillo):
        with open('platillos.csv', 'a', newline='',encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(platillo)

    def crear_platillo(self):
        nombre = self.input_nombre.text()
        carne = self.combo_carne.currentText()
        verduras = self.combo_verduras.currentText()
        mariscos = self.combo_mariscos.currentText()
        pescados = self.combo_pescados.currentText()

        # Validar que se haya ingresado un nombre
        if nombre:
            # Descontar los ingredientes del inventario correspondiente
            if self.actualizar_inventario('carnes.csv', carne, 1) and \
                self.actualizar_inventario('verduras.csv', verduras, 1) and \
                self.actualizar_inventario('mariscos.csv', mariscos, 1) and \
                self.actualizar_inventario('pescados.csv', pescados, 1):

                # Guardar el platillo en el archivo "platillos.csv"
                platillo = [nombre, carne, verduras, mariscos, pescados]
                self.guardar_platillo(platillo)

                # Mostrar mensaje de éxito
                QMessageBox.information(self, 'Platillo Creado', 'El platillo se ha creado exitosamente.')

                # Reiniciar los campos de entrada
                self.input_nombre.clear()
                self.combo_carne.setCurrentIndex(0)
                self.combo_verduras.setCurrentIndex(0)
                self.combo_mariscos.setCurrentIndex(0)
                self.combo_pescados.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, 'Error', 'Por favor ingrese un nombre para el platillo.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPlatillos()
    ventana.show()
    sys.exit(app.exec_())
