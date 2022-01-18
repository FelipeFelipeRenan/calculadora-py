import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Minha Calculadora') # mudando nome da janela
        self.setFixedSize(400, 400) # fixando uma largura e altura
        self.cw = QWidget() # criando o widget
        self.grid = QGridLayout(self.cw) # criando layout de grids
        # criando o display
        self.display = QLineEdit() 
        # colocando o disolay onde ira aparecer os numeros
        self.grid.addWidget(self.display, 0, 0 ,1 ,5) 
        # desativando o input de texto 
        self.display.setDisabled(True)
        # mudando o estilo
        self.display.setStyleSheet(
            '* {background: #FFF; color: #000; font-size: 30px;}'
        )
        # ajustando botoes
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # adicionando botoes
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''), 
            'background: #d5580d; color: #fff; font-weight: 700;'
            )
        
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1, 
            lambda: self.display.setText(self.display.text()[:-1]),
            'background: #13823a; color: #fff; font-weight: 700;'
            )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background: #095177; color: #fff; font-weight: 700;'
            )
        self.setCentralWidget(self.cw)
    
    # metodo para digitar no display
    def add_btn(self, btn, row, col, rowspan, colspan, funcao = None, style = None):
        # adicionando os botoes
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        
        if not funcao:

            # listener para mostrar o que foi clicado
            btn.clicked.connect(
                # lambda para unir os textos na tela
                lambda: self.display.setText(self.display.text() + btn.text())        
            )
        else:
            btn.clicked.connect(funcao)
        
        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        
        except Exception as e:
            self.display.setText('Operação inválida')

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()