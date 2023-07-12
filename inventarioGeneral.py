from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from inventarioVerduras import InventarioVerduras
from inventarioCarnes import InventarioCarne
from inventarioMarisco import InventarioMariscos
from inventarioPescados import InventarioPescados
from platillos import VentanaPlatillos
from inventarioMermas import InventarioMermas
from inventariPlatillos import VentanaPlatillosRegistrados
from inperecederos import InventarioImperecederos 

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana Principal')

        layout = QVBoxLayout()

        label_bienvenido = QLabel('Bienvenido, ¿qué desea hacer?')
        layout.addWidget(label_bienvenido)

        button1 = QPushButton('Abrir Inventario de Verduras')
        button1.clicked.connect(self.abrir_inventario_verduras)
        layout.addWidget(button1)

        button2 = QPushButton('Abrir Inventario de Carnes')
        button2.clicked.connect(self.abrir_inventario_carnes)
        layout.addWidget(button2)

        button3 = QPushButton('Abrir Inventario de Mariscos')
        button3.clicked.connect(self.abrir_inventario_mariscos)
        layout.addWidget(button3)

        button4 = QPushButton('Abrir Inventario de Pescados')
        button4.clicked.connect(self.abrir_inventario_pescados)
        layout.addWidget(button4)

        button5 = QPushButton('Abrir Ventana de Platillos')
        button5.clicked.connect(self.abrir_ventana_platillos)
        layout.addWidget(button5)

        button7 = QPushButton('Abrir Inventario de Platillos')
        button7.clicked.connect(self.abrir_inventario_platillos)
        layout.addWidget(button7)

        
        button8 = QPushButton('Abrir Inventario de imperecederos')
        button8.clicked.connect(self.abrir_ventana_imperecederos)
        layout.addWidget(button8)

        

        button6 = QPushButton('Abrir Inventario de Mermas')
        button6.clicked.connect(self.abrir_inventario_mermas)
        layout.addWidget(button6)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.ventanas = []  # Lista para almacenar las ventanas abiertas

        # Ajustar el tamaño de la ventana
        self.setGeometry(100, 100, 800, 600)

    def abrir_inventario_verduras(self):
        ventana = InventarioVerduras()
        self.ventanas.append(ventana)
        ventana.show()

    def abrir_inventario_carnes(self):
        ventana = InventarioCarne()
        self.ventanas.append(ventana)
        ventana.show()

    def abrir_inventario_mariscos(self):
        ventana = InventarioMariscos()
        self.ventanas.append(ventana)
        ventana.show()

    def abrir_inventario_pescados(self):
        ventana = InventarioPescados()
        self.ventanas.append(ventana)
        ventana.show()

    def abrir_ventana_platillos(self):
        ventana =  VentanaPlatillos()
        self.ventanas.append(ventana)
        ventana.show()

    def abrir_inventario_platillos(self):
        ventana = VentanaPlatillosRegistrados()
        self.ventanas.append(ventana)
        ventana.show()

    def abrir_inventario_mermas(self):
        ventana = InventarioMermas()
        self.ventanas.append(ventana)
        ventana.show()
    
    def abrir_ventana_imperecederos(self):
        ventana = InventarioImperecederos ()
        self.ventanas.append(ventana)
        ventana.show()



if __name__ == '__main__':
    app = QApplication([])
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    app.exec_()
