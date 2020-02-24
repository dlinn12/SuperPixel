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
        self.redLabel = QLabel()
        self.redLabel.setText("Red:      ")
        self.redLabel.setStyleSheet("color: red; font-weight: bold")
        self.redInput = QLineEdit(self)
        self.redInput.setStyleSheet("background-color: white")
        self.redInput.resize(130, 40)
        self.redInput.setText(str(self.red))
        self.redButton = QPushButton(self)
        self.redButton.setStyleSheet("background-color: white")
        self.redButton.setText("GO")
        self.redButton.clicked.connect(self.redClicked)
        self.redArea = QHBoxLayout()
        self.redArea.addWidget(self.redLabel)
        self.redArea.addWidget(self.redInput)
        self.redArea.addWidget(self.redButton)

        # Create input for the green light
        self.greenLabel = QLabel()
        self.greenLabel.setText("Green:   ")
        self.greenLabel.setStyleSheet("color: green; font-weight: bold")
        self.greenInput = QLineEdit(self)
        self.greenInput.setStyleSheet("background-color: white")
        self.greenInput.resize(130, 40)
        self.greenInput.setText(str(self.green))
        self.greenButton = QPushButton(self)
        self.greenButton.setStyleSheet("background-color: white")
        self.greenButton.setText("GO")
        self.greenButton.clicked.connect(self.greenClicked)
        self.greenArea = QHBoxLayout()
        self.greenArea.addWidget(self.greenLabel)
        self.greenArea.addWidget(self.greenInput)
        self.greenArea.addWidget(self.greenButton)

        # Create input for the blue light
        self.blueLabel = QLabel()
        self.blueLabel.setText("Blue:     ")
        self.blueLabel.setStyleSheet("color: blue; font-weight: bold")
        self.blueInput = QLineEdit(self)
        self.blueInput.setStyleSheet("background-color: white")
        self.blueInput.resize(130, 40)
        self.blueInput.setText(str(self.blue))
        self.blueButton = QPushButton(self)
        self.blueButton.setStyleSheet("background-color: white")
        self.blueButton.setText("GO")
        self.blueButton.clicked.connect(self.blueClicked)
        self.blueArea = QHBoxLayout()
        self.blueArea.addWidget(self.blueLabel)
        self.blueArea.addWidget(self.blueInput)
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
        self.red_selection = self.redInput.text()
        self.red = str(constrain(int(self.red_selection)))
        self.red_selection = rgb_maker(self.red, "red")
        self.redBox.setStyleSheet(self.red_selection)
        self.pixelOutput.setStyleSheet(rgb_output(self.red, self.green, self.blue))
        self.redInput.setText(self.red)

    def greenClicked(self):
        self.green_selection = self.greenInput.text()
        self.green = str(constrain(int(self.green_selection)))
        self.green_selection = rgb_maker(self.green, "green")
        self.greenBox.setStyleSheet(self.green_selection)
        self.pixelOutput.setStyleSheet(rgb_output(self.red, self.green, self.blue))
        self.greenInput.setText(self.green)

    def blueClicked(self):
        self.blue_selection = self.blueInput.text()
        self.blue = str(constrain(int(self.blue_selection)))
        self.blue_selection = rgb_maker(self.blue, "blue")
        self.blueBox.setStyleSheet(self.blue_selection)
        self.pixelOutput.setStyleSheet(rgb_output(self.red, self.green, self.blue))
        self.blueInput.setText(self.blue)
    

def rgb_maker(value, light):
    ''' This function takes in a value from 0-255 and light [red, blue, green]
        and returns the necessary CSS string to emit that change'''
    value = constrain(int(value))

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
    r = constrain(int(r))
    g = constrain(int(g))
    b = constrain(int(b))
    output = "background-color: rgb(" + str(r) + ", " + str(g) + ", " + str(b) + ")"
    return output


def constrain(val):
    if val > 255:
        val = 255
    if val < 0:
        val = 0
    return val


def start():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start()
