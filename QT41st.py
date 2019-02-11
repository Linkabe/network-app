from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
app.setStyle('windows')

palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)

app.setStyleSheet("QPushButton { margin: 10ex; }")

window = QWidget()
layout = QVBoxLayout()

layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))

window.setLayout(layout)
window.show()
app.exec_()
