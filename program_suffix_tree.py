import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
import patricia_tree as pt
import suffix_array as sa
import time


if len(sys.argv) != 2:
    print('Use: '+sys.argv[0]+' archivo.txt')
    sys.exit(1)

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

        message = "\n \n \n"
        message += f'''
        ---------------------------------------------------------------
        -- Bienvenido al widget de búsqueda de sufijos --
        ---------------------------------------------------------------

        1 - Para buscar, solo comience a escribir en el
            input ubicado en la parte superior del
            widget
        2 - La aplicación le indicará las recomendaciones
            de llenado utilizando un suffix_tree

        archivo cargado: {sys.argv[1]}
        ---------------------------------------------------------------
        ----------------------- Authors -----------------------------
           Nicolás García -- Javier Lavados -- Lung Pang    
        ---------------------------------------------------------------
        '''
        self.console.append(message)
        mainLayout.addWidget(self.console)

        self.setLayout(mainLayout)

        self.input.textChanged.connect(self.onChanged)
        self.show()
    
    def setWords(self): # funcion que actualiza las palabras para el autocompletado
        text=self.input.text()
        result=root.autocompletar(text)
        print(result)
        for i in range(0,len(result)):
            if result[i]=="":
                self.autocomplete_model.setItem(i,QStandardItem(""))
            else:
                message =text+result[i]
                self.autocomplete_model.setItem(i,QStandardItem(message))

    def onChanged(self, text): # cada vez que el el texto cambia, se cambia las palabras sugeridas
        self.setWords()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppDemo()
    sys.exit(app.exec_())
