import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit)

class MainWindow(QMainWindow):
	'''Create the main windows of the application and set size and title
	'''
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.title = "SuperPixel"
		self.left = 200
		self.top = 100
		self.width = 600
		self.height = 600
		self.red = 255
		self.green = 255
		self.blue = 255
		self.setStyleSheet("background-color: black")

		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowTitle(self.title)
		self.central_widget = QWidget()
		self.setCentralWidget(self.central_widget)

		# Create label showing pixel output
		self.pixelOutput = QWidget()
		self.pixelOutput.setMinimumHeight(15)
		self.pixelOutput.setMinimumWidth(15)
		self.pixelOutput.setMaximumHeight(60)
		self.pixelOutput.setMaximumWidth(60)
		self.pixelOutput.setStyleSheet(rgb_output(self.red, self.green, self.blue))

		# Create the red color in the pixel
		self.redBox = QWidget()
		self.redBox.setMinimumHeight(60)
		self.redBox.setMinimumWidth(60)
		self.redBox.setStyleSheet(rgb_maker(self.red, "red"))

		# Create the green color in the pixel
		self.greenBox = QWidget()
		self.greenBox.setMinimumHeight(60)
		self.greenBox.setMinimumWidth(60)
		self.greenBox.setStyleSheet(rgb_maker(self.green, "green"))

		# Create the blue color in the pixel
		self.blueBox = QWidget()
		self.blueBox.setMinimumHeight(60)
		self.blueBox.setMinimumWidth(60)
		self.blueBox.setStyleSheet(rgb_maker(self.blue, "blue"))

		# Create space for 3 boxes set in order horizontally
		self.pixelBox = QHBoxLayout()
		self.pixel_box_margins = 30
		self.pixelBox.setContentsMargins(self.pixel_box_margins, self.pixel_box_margins, self.pixel_box_margins, self.pixel_box_margins)
		self.pixelBox.addWidget(self.redBox)
		self.pixelBox.addWidget(self.greenBox)
		self.pixelBox.addWidget(self.blueBox)


		# Create input for the red light
		self.redLabel = QLineEdit(self)
		self.redLabel.setStyleSheet("background-color: white")
		self.redLabel.resize(130, 40)
		self.redLabel.setText(str(self.red))
		self.redButton = QPushButton(self)
		self.redButton.setStyleSheet("background-color: white")
		self.redButton.setText("GO")
		self.redButton.clicked.connect(self.redClicked)
		self.redArea = QHBoxLayout()
		self.redArea.addWidget(self.redLabel)
		self.redArea.addWidget(self.redButton)

		# Create input for the green light
		self.greenLabel = QLineEdit(self)
		self.greenLabel.setStyleSheet("background-color: white")
		self.greenLabel.resize(130, 40)
		self.greenLabel.setText(str(self.green))
		self.greenButton = QPushButton(self)
		self.greenButton.setStyleSheet("background-color: white")
		self.greenButton.setText("GO")
		self.greenButton.clicked.connect(self.greenClicked)
		self.greenArea = QHBoxLayout()
		self.greenArea.addWidget(self.greenLabel)
		self.greenArea.addWidget(self.greenButton)

		# Create input for the blue light
		self.blueLabel = QLineEdit(self)
		self.blueLabel.setStyleSheet("background-color: white")
		self.blueLabel.resize(130, 40)
		self.blueLabel.setText(str(self.blue))
		self.blueButton = QPushButton(self)
		self.blueButton.setStyleSheet("background-color: white")
		self.blueButton.setText("GO")
		self.blueButton.clicked.connect(self.blueClicked)
		self.blueArea = QHBoxLayout()
		self.blueArea.addWidget(self.blueLabel)
		self.blueArea.addWidget(self.blueButton)

		# Add every layout to the main window
		self.vBox = QVBoxLayout()
		self.vBox.addWidget(self.pixelOutput)
		self.vBox.addLayout(self.pixelBox)
		self.vBox.addLayout(self.redArea)
		self.vBox.addLayout(self.greenArea)
		self.vBox.addLayout(self.blueArea)
		self.central_widget.setLayout(self.vBox)

		self.show()

	# These functions update each color in the pixel

	def redClicked(self):
		self.red_selection = self.redLabel.text()
		self.red = self.red_selection
		self.red_selection = rgb_maker(self.red_selection, "red")
		self.redBox.setStyleSheet(self.red_selection)
		self.pixelOutput.setStyleSheet(rgb_output(self.red, self.green, self.blue))

	def greenClicked(self):
		self.green_selection = self.greenLabel.text()
		self.green = self.green_selection
		self.green_selection = rgb_maker(self.green_selection, "green")
		self.greenBox.setStyleSheet(self.green_selection)
		self.pixelOutput.setStyleSheet(rgb_output(self.red, self.green, self.blue))

	def blueClicked(self):
		self.blue_selection = self.blueLabel.text()
		self.blue = self.blue_selection
		self.blue_selection = rgb_maker(self.blue_selection, "blue")
		self.blueBox.setStyleSheet(self.blue_selection)
		self.pixelOutput.setStyleSheet(rgb_output(self.red, self.green, self.blue))
	

def rgb_maker(value, light):
	''' This function takes in a value from 0-255 and light [red, blue, green]
		and returns the necessary CSS string to emit that change'''
	value = int(value)
	if value > 255:
		value = 255
	if value < 0:
		value = 0

	base = "background-color: rgb("
	if light == "red":
		return base + str(value) + ", 0, 0)"
	elif light == "green":
		return base + "0, " + str(value) + ", 0)"
	else:
		return base + "0, 0, " + str(value) + ")"

def rgb_output(r, g, b):
	''' This fucntion returns the value for the pixel with all colors combined
	'''
	output = "background-color: rgb(" + str(r) + ", " + str(g) + ", " + str(b) + ")"
	return output


def start():
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	w = MainWindow()
	sys.exit(app.exec_())

if __name__ == "__main__":
	start()