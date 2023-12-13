from PyQt5.QtWidgets import (
    QWidget,
    QMessageBox,
    QGraphicsPixmapItem,
    QGraphicsView,
    QGraphicsScene,
)

from PyQt5.QtGui import QFontDatabase, QImage, QPixmap
from PyQt5.QtCore import Qt
from io import BytesIO
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


from ui.tabs.dot_plot_ui import Ui_Form
from seq_algorithm.dotplot import DotMatrix

import numpy as np
import matplotlib.pyplot as plt


class DotPlot(QWidget):
    """Second Tab of the GUI App. Dot Plot Sequence Alignment"""

    def __init__(self):
        super(DotPlot, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.graphicsView.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.stylesheet_file("static/style/dot_plot_tab_style.qss")
        QFontDatabase.addApplicationFont(
            ":/fonts/Lora-VariableFont/Lora-VariableFont_wght.ttf"
        )
        #### ====== Signal Buttons  ======####
        # self.ui.load_seq1.clicked.connect(self.load_file1)
        # self.ui.load_seq2.clicked.connect(self.load_file2)
        # self.ui.save_btn.clicked.connect(self.function)
        self.ui.plot_btn.clicked.connect(self.plot_clicked)

    def stylesheet_file(self, style_path):
        style_path = "static/style/dot_plot_tab_style.qss"
        with open(style_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def plot_clicked(self):
        """Retrieving the input values upon clicking the Plot button"""
        #### ====== Retrieve Values ======####
        label_1 = (
            self.ui.label_seq1.text() or " No Sample Label Added [First Sequence] "
        )
        input_seq1 = self.ui.textEdit.toPlainText()
        label_2 = (
            self.ui.label_seq2.text() or " No Sample Label Added [Second Sequence] "
        )
        input_seq2 = self.ui.textEdit_2.toPlainText()

        self.perform_plot(input_seq1, input_seq2, label_1, label_2)

    def perform_plot(self, input_seq1, input_seq2, label_1, label_2):
        """Implements the methods on class DotMatrix"""
        try:
            self.dm = DotMatrix(
                M=np.empty((1, 1), dtype=str), seqA=input_seq1, seqB=input_seq2
            )
            if self.dm.is_valid:
                fig = self.dm.fill_plot(label_1=label_1, label_2=label_2)
                self.embed_plot(fig)
            else:
                raise ValueError()
        except ValueError as e:
            self.pop_warning(f"DotMatrix Error: {e}")

    def embed_plot(self, fig):
        """Embed the MatplotLib plot into the QGraphicsView"""
        buff = BytesIO()
        fig.savefig(buff, format="png")
        buff.seek(0)
        img = QImage.fromData(buff.read())
        if not self.ui.graphicsView.scene():
            self.ui.graphicsView.setScene(QGraphicsScene())

        pixmap_item = QGraphicsPixmapItem(QPixmap(img))
        self.ui.graphicsView.scene().clear()
        self.ui.graphicsView.setSceneRect(0, 0, img.width(), img.height())
        self.ui.graphicsView.scene().addItem(pixmap_item)

    def pop_warning(self, message):
        """Warning Message if the Input is Wrong"""
        pop_warning = QMessageBox()
        pop_warning.setIcon(QMessageBox.Warning)
        pop_warning.setWindowTitle("Input Error")
        pop_warning.setText(message)
        pop_warning.setStyleSheet(
            """
        QMessageBox{
            background-color: rgb(54,54,54); /* charcoal gray*/ 
            }
        QMessageBox QLabel{
            color: #fff;
            }
        QMessageBox QPushButton {
            background-color: rgb(120,157,186); /* light blue */
	        border: 3px solid rgb(5,92,142);
	        border-radius:15px;
	        padding: 5px;
	        color: #000;
            font-size:12px;
            }
        QMessageBox QPushButton::hover{
            background-color: rgba(5,92,142,0.5); /* dark-blue */
	        color: #fff;
	        border-radius: 15px;
            font-size:12px;
            }
        """
        )
        pop_warning.exec_()
