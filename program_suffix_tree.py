import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
import patricia_tree as pt
import suffix_array as sa
import time


# Recibimos y leimos el archivo de texto
txt = open(sys.argv[1])
fulltext = txt.read()

# Creamos su array de sufijos a partir del texto
array = sa.suffix_array(fulltext)

# Creamos el arbol de sufijos a partir de sufijos
root = pt.Patricia()
for w in array:
    root.insert(w.get_suffix()+'$')
root.insert('$')
root.pre_count_sons()
root.pre_most_popular()

# Creamos una clase App demo para el widget
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 800)

        fnt = QFont('Open Sans', 12)
        mainLayout = QVBoxLayout()

        # input field
        self.input = QLineEdit()
        self.input.setFixedHeight(50)
        self.input.setFont(fnt)
        mainLayout.addWidget(self.input)

        self.autocomplete_model = QStandardItemModel()
        self.setWords()
        

        self.completer = QCompleter()
        self.completer.setModel(self.autocomplete_model)
        self.input.setCompleter(self.completer)

        self.console = QTextEdit()
        self.console.setFont(fnt)
        self.console.append(str(root))
        mainLayout.addWidget(self.console)

        self.setLayout(mainLayout)

        self.input.textChanged.connect(self.onChanged)
        self.show()
    
    def setWords(self,):
        a=self.input.text()
        autocomplete_list = ["caca_"+str(a),"caca_"+str(a),"caca_"+str(a)]
        for i in range(0,3):
            self.autocomplete_model.setItem(i,QStandardItem(autocomplete_list[i]))


    def onChanged(self, text):
        print("Cambiare")
        self.setWords()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppDemo()
    sys.exit(app.exec_())
