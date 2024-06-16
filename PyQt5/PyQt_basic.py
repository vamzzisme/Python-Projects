from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

screenx = 100
screeny = 100
screen_width = 300
screen_height = 300

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(screenx, screeny, screen_width, screen_height)
		self.setWindowTitle("basic for all")
		self.initUi()

	def initUi(self):
		# a LABEL CREATION
		self.label = QtWidgets.QLabel(self)
		self.label.setText("First Label")
		self.label.move(50, 50)

		# a BUTTON CREATION
		self.button1 = QtWidgets.QPushButton(self)
		self.button1.setText("click")
		self.button1.clicked.connect(self.clicked)

	def clicked(self):
		self.label.setText("you pressed the button")
		self.update()

	def update(self):
		self.label.adjustSize()

def window():
	app = QApplication(sys.argv)
	screen = MyWindow()

	screen.show()
	sys.exit(app.exec_())

window()