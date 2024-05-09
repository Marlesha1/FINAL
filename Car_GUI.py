import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsScene


class CarController:
    def __init__(self, input_widgets, display_widgets):
        # Initialize your controller with input and display widgets
        self.input_widgets = input_widgets
        self.display_widgets = display_widgets

    def calculate(self):
        # Placeholder calculation logic
        m1 = float(self.input_widgets[0].text())
        v = float(self.input_widgets[1].text())
        k1 = float(self.input_widgets[2].text())
        c1 = float(self.input_widgets[3].text())
        m2 = float(self.input_widgets[4].text())
        k2 = float(self.input_widgets[5].text())
        ang = float(self.input_widgets[6].text())
        tmax = float(self.input_widgets[7].text())

        # Placeholder: Calculate forces
        force_spring = 1000  # Placeholder value for spring force
        force_dashpot = 500  # Placeholder value for dashpot force

        # Display the calculated forces
        self.display_widgets[5].setText(f"Spring Force: {force_spring} N, Dashpot Force: {force_dashpot} N")

    def doPlot(self, plot_type):
        if plot_type == 'position':
            t = np.linspace(0, 10, 100)
            position_data = np.sin(t)

            # Plot position vs. time
            plt.figure()
            plt.plot(t, position_data)
            plt.xlabel('Time')
            plt.ylabel('Position')
            plt.title('Position vs. Time')
            plt.grid(True)
            plt.draw()

            # Convert plot to image
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image = QImage.fromData(buf.getvalue())

            # Display the plot in QGraphicsView
            scene = QGraphicsScene()
            pixmap = QPixmap.fromImage(image)
            scene.addPixmap(pixmap)
            self.display_widgets[0].setScene(scene)

        elif plot_type == 'force':
            t = np.linspace(0, 10, 100)
            force_data = np.cos(t)

            # Plot force vs. time
            plt.figure()
            plt.plot(t, force_data)
            plt.xlabel('Time')
            plt.ylabel('Force')
            plt.title('Force vs. Time')
            plt.grid(True)
            plt.draw()

            # Convert plot to image
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image = QImage.fromData(buf.getvalue())

            # Display the plot in QGraphicsView
            scene = QGraphicsScene()
            pixmap = QPixmap.fromImage(image)
            scene.addPixmap(pixmap)
            self.display_widgets[1].setScene(scene)
