import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class Model:
    def __init__(self):
        self.weight = 0
        self.thrust = 0

    def set_weight(self, weight):
        self.weight = weight

    def set_thrust(self, thrust):
        self.thrust = thrust

    def calculate_sto(self):
        weights = [self.weight, self.weight - 10000, self.weight + 10000]
        sto_values = [self.sto(weight) for weight in weights]
        return weights, sto_values

    def sto(self, weight):
        # Some STO calculation based on weight and thrust, replace this with your actual calculation
        return np.random.uniform(0, 100)

class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STO Calculator")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.weight_label = QLabel("Weight (lb):")
        self.weight_edit = QLineEdit()
        self.layout.addWidget(self.weight_label)
        self.layout.addWidget(self.weight_edit)

        self.thrust_label = QLabel("Thrust (lb):")
        self.thrust_edit = QLineEdit()
        self.layout.addWidget(self.thrust_label)
        self.layout.addWidget(self.thrust_edit)

        self.calculate_button = QPushButton("Calculate")
        self.layout.addWidget(self.calculate_button)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.controller = Controller(self)

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model()
        self.view.calculate_button.clicked.connect(self.calculate)

    def calculate(self):
        weight = float(self.view.weight_edit.text())
        thrust = float(self.view.thrust_edit.text())
        self.model.set_weight(weight)
        self.model.set_thrust(thrust)
        weights, sto_values = self.model.calculate_sto()
        self.plot(weights, sto_values)

    def plot(self, weights, sto_values):
        ax = self.view.figure.add_subplot(111)
        ax.clear()
        ax.plot(weights, sto_values, label='STO')
        ax.scatter(self.model.weight, self.model.sto(self.model.weight), color='red', label='Specified Weight')
        ax.legend()
        ax.set_xlabel('Weight (lb)')
        ax.set_ylabel('STO')
        self.view.canvas.draw()

def main():
    app = QApplication(sys.argv)
    view = View()
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
