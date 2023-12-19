# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/tabs/basic_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1132, 667)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        Form.setFont(font)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QFrame(Form)
        self.title.setStyleSheet("")
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.title)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.title)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.title)
        self.des = QtWidgets.QFrame(Form)
        self.des.setStyleSheet("")
        self.des.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.des.setFrameShadow(QtWidgets.QFrame.Raised)
        self.des.setObjectName("des")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.des)
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.des)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.des)
        self.main = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setStyleSheet("")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_frame = QtWidgets.QFrame(self.main)
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.input_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.input_frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            309, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(
            198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 3, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.input_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.seq_input = QtWidgets.QTextEdit(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seq_input.sizePolicy().hasHeightForWidth())
        self.seq_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.seq_input.setFont(font)
        self.seq_input.setObjectName("seq_input")
        self.gridLayout_2.addWidget(self.seq_input, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.input_frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_13 = QtWidgets.QFrame(self.frame_8)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_6 = QtWidgets.QLabel(self.frame_13)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 70, 70))
        self.label_6.setMinimumSize(QtCore.QSize(70, 70))
        self.label_6.setMaximumSize(QtCore.QSize(70, 70))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/images/images/gene_info.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.frame_13)
        self.load_start = QtWidgets.QFrame(self.frame_8)
        self.load_start.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.load_start.setFrameShadow(QtWidgets.QFrame.Raised)
        self.load_start.setObjectName("load_start")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.load_start)
        self.verticalLayout_6.setContentsMargins(5, -1, 10, 5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.load_btn = QtWidgets.QPushButton(self.load_start)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/icons/upload.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.load_btn.setIcon(icon)
        self.load_btn.setObjectName("load_btn")
        self.verticalLayout_6.addWidget(self.load_btn)
        self.start_btn = QtWidgets.QPushButton(self.load_start)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.start_btn.setIcon(icon1)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout_6.addWidget(self.start_btn)
        self.horizontalLayout_2.addWidget(self.load_start, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.input_frame)
        self.output_frame = QtWidgets.QFrame(self.main)
        self.output_frame.setStyleSheet("")
        self.output_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_frame.setObjectName("output_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.output_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.out_text = QtWidgets.QFrame(self.output_frame)
        self.out_text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_text.setObjectName("out_text")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.out_text)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.out_text)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(
            self.label_5, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        )
        self.verticalLayout_5.addWidget(self.out_text, 0, QtCore.Qt.AlignTop)
        self.out_screen = QtWidgets.QFrame(self.output_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_screen.sizePolicy().hasHeightForWidth())
        self.out_screen.setSizePolicy(sizePolicy)
        self.out_screen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_screen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_screen.setObjectName("out_screen")
        self.gridLayout = QtWidgets.QGridLayout(self.out_screen)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.out_screen)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.out_screen)
        self.clear_save = QtWidgets.QFrame(self.output_frame)
        self.clear_save.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.clear_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.clear_save.setObjectName("clear_save")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.clear_save)
        self.horizontalLayout_3.setContentsMargins(-1, 0, 12, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.clear_btn = QtWidgets.QPushButton(self.clear_save)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/x-circle.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.clear_btn.setIcon(icon2)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_3.addWidget(self.clear_btn)
        spacerItem2 = QtWidgets.QSpacerItem(
            212, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem2)
        self.save_btn = QtWidgets.QPushButton(self.clear_save)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.save_btn.setIcon(icon3)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_3.addWidget(self.save_btn)
        self.verticalLayout_5.addWidget(self.clear_save, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.output_frame)
        self.verticalLayout.addWidget(self.main)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(
            _translate("Form", "Retrieving Basic Information About Your Sequence")
        )
        self.textEdit.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Noto Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Enter your DNA/RNA or Protein sequence, choose the sequence type, and click &quot;Start&quot; to analyze. For DNA/RNA, you can expect outputs such as GC content, nucleotide frequency and transcription; for Protein, you can expect to get amino acid frequency,molecular weight, or reading frames. Use &quot;Load File&quot; to import sequences, &quot;Save Output&quot; to save results, and &quot;Clear&quot; to start a new. Ensure correct inputs to avoid warnings.</p></body></html>',
            )
        )
        self.label_2.setText(_translate("Form", "Biomolecule Type: "))
        self.comboBox.setItemText(0, _translate("Form", "DNA"))
        self.comboBox.setItemText(1, _translate("Form", "RNA"))
        self.comboBox.setItemText(2, _translate("Form", "Protein"))
        self.label_3.setText(_translate("Form", "Label:"))
        self.label_4.setText(_translate("Form", "Input"))
        self.seq_input.setPlaceholderText(
            _translate("Form", "Paste the Sequence or URL")
        )
        self.load_btn.setText(_translate("Form", "Load"))
        self.start_btn.setText(_translate("Form", "Start"))
        self.label_5.setText(_translate("Form", "Output"))
        self.clear_btn.setText(_translate("Form", "Clear"))
        self.save_btn.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
