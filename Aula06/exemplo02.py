
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


app = QApplication([])
janela = QWidget()
janela.setWindowTitle("Minha Primeira Janela")
rotulo = QLabel("Olá, mundo!, como vai tudo bem?", parent=janela)


janela.resize(800, 300)

janela.show()

app.exec_()
