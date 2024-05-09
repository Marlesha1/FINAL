from Car_GUI import CarController


class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        input_widgets = (self.le_m1, self.le_v, self.le_k1, self.le_c1, self.le_m2, self.le_k2, self.le_ang, \
                         self.le_tmax, self.chk_IncludeAccel)
        display_widgets = (self.gv_PositionVsTime, self.gv_ForceVsTime)
        self.controller = CarController(input_widgets, display_widgets)
        self.btn_calculate.clicked.connect(self.controller.calculate)
        self.setupTabs()

    def setupTabs(self):
        # Connect tab widget's currentChanged signal to slot
        self.tabWidget.currentChanged.connect(self.tabChanged)

    def tabChanged(self, index):
        # Slot to handle tab change event
        if index == 0:
            # Switch to position vs. time graph
            self.controller.doPlot('position')
        elif index == 1:
            # Switch to force vs. time graph
            self.controller.doPlot('force')
