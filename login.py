import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QPixmap

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon('logo.png'))

        # Crear etiquetas y campos de texto para usuario y contraseña
        label_usuario = QLabel('Usuario:')
        self.input_usuario = QLineEdit()

        label_contrasena = QLabel('Contraseña:')
        self.input_contrasena = QLineEdit()
        self.input_contrasena.setEchoMode(QLineEdit.Password)

        # Crear botón de inicio de sesión
        btn_login = QPushButton('Iniciar sesión')
        btn_login.clicked.connect(self.login)

        # Crear layout vertical y agregar los widgets
        layout = QVBoxLayout()
        layout.addSpacing(30)
        layout.addWidget(label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(label_contrasena)
        layout.addWidget(self.input_contrasena)
        layout.addSpacing(20)
        layout.addWidget(btn_login)
        layout.addStretch()

        # Crear widget central y establecer el layout
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer el widget central en la ventana principal
        self.setCentralWidget(widget)

    def login(self):
        # Obtener el usuario y la contraseña ingresados
        usuario = self.input_usuario.text()
        contrasena = self.input_contrasena.text()

        # Verificar si las credenciales son válidas (en este ejemplo, usuario: admin, contraseña: 1234)
        if usuario == 'admin' and contrasena == '1234':
            print('Inicio de sesión exitoso')
            self.close()
        else:
            print('Credenciales incorrectas')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec_())
