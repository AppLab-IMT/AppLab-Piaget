import sys
from PySide6.QtWidgets import QApplication , QPushButton, QWidget, QVBoxLayout


project = QApplication(sys.argv)





btn1 = QPushButton('btn1')

# adiciona widget e executa em app
btn1.show()

# nao recebe outro widget recebe um layout
central_widget = QWidget()

# layout e um widget que recebe outros widgets

layout = QVBoxLayout()
layout.addWidget(btn1)


# loop principal 
project.exec()