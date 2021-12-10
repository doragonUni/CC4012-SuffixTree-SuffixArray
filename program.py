import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
import patricia_tree as pt
import suffix_array as sa

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        fnt = QFont('Open Sans', 12)

        mainLayout = QVBoxLayout()

        # input field
        self.input = QLineEdit()
        self.input.setFixedHeight(50)
        self.input.setFont(fnt)
        self.input.editingFinished.connect(self.addEntry)
        mainLayout.addWidget(self.input)

        self.model = QStandardItemModel()
        completer = QCompleter(self.model, self)
        self.input.setCompleter(completer)

        self.console = QTextEdit()
        self.console.setFont(fnt)
        mainLayout.addWidget(self.console)

        self.setLayout(mainLayout)

    def addEntry(self):
        entryItem = self.input.text()
        self.input.clear()
        self.console.append(entryItem)

        if not self.model.findItems(entryItem):
            self.model.appendRow(QStandardItem(entryItem))


txt = open(sys.argv[1])
fulltext = txt.read()
array = sa.suffixArray(fulltext)

print(array)
root = pt.Patricia()
for w in array:
    root.insert(fulltext[w:]+'$')
root.insert('$')
root.pre_count_sons()
root.pre_most_popular()

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())