# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\user\Documents\Data Science\pairwise_gui\ui\tabs\global_align.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 720)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title = QtWidgets.QFrame(Form)
        self.title.setMaximumSize(QtCore.QSize(16777215, 16777210))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.title)
        self.gridLayout_4.setContentsMargins(0, 5, 10, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.title)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.title)
        self.label_6.setMaximumSize(QtCore.QSize(50, 50))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/images/images/bases1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.title)
        self.des = QtWidgets.QFrame(Form)
        self.des.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.des.setFrameShadow(QtWidgets.QFrame.Raised)
        self.des.setObjectName("des")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.des)
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.des)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 110))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.frame_3 = QtWidgets.QFrame(self.des)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.seq_mainframe = QtWidgets.QFrame(self.frame_3)
        self.seq_mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seq_mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seq_mainframe.setObjectName("seq_mainframe")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.seq_mainframe)
        self.verticalLayout_7.setContentsMargins(10, 0, 0, 15)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.seq1_frame = QtWidgets.QFrame(self.seq_mainframe)
        self.seq1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seq1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seq1_frame.setObjectName("seq1_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.seq1_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.seq1_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.load_seq1 = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/icons/upload.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.load_seq1.setIcon(icon)
        self.load_seq1.setObjectName("load_seq1")
        self.horizontalLayout.addWidget(self.load_seq1)
        self.verticalLayout_2.addWidget(self.frame)
        self.textEdit = QtWidgets.QTextEdit(self.seq1_frame)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_7.addWidget(self.seq1_frame)
        self.seq2_frame = QtWidgets.QFrame(self.seq_mainframe)
        self.seq2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seq2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seq2_frame.setObjectName("seq2_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.seq2_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.seq2_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.load_seq2 = QtWidgets.QPushButton(self.frame_2)
        self.load_seq2.setIcon(icon)
        self.load_seq2.setObjectName("load_seq2")
        self.horizontalLayout_2.addWidget(self.load_seq2)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.seq2_frame)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_5.addWidget(self.textEdit_2)
        self.verticalLayout_7.addWidget(self.seq2_frame)
        self.gridLayout.addWidget(self.seq_mainframe, 0, 0, 1, 1)
        self.align_frame = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.align_frame.sizePolicy().hasHeightForWidth())
        self.align_frame.setSizePolicy(sizePolicy)
        self.align_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.align_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.align_frame.setObjectName("align_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.align_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.align_frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.frame_8.setFont(font)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.align_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_11)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_11)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.start_save_btns = QtWidgets.QFrame(self.align_frame)
        self.start_save_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.start_save_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start_save_btns.setObjectName("start_save_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.start_save_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.clear_btn = QtWidgets.QPushButton(self.start_save_btns)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/trash-2.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.clear_btn.setIcon(icon1)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_3.addWidget(self.clear_btn)
        self.align_btn = QtWidgets.QPushButton(self.start_save_btns)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/play-circle.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.align_btn.setIcon(icon2)
        self.align_btn.setObjectName("align_btn")
        self.horizontalLayout_3.addWidget(self.align_btn)
        spacerItem = QtWidgets.QSpacerItem(
            228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.save_btn = QtWidgets.QPushButton(self.start_save_btns)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.save_btn.setIcon(icon3)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_3.addWidget(self.save_btn)
        self.verticalLayout_6.addWidget(self.start_save_btns)
        self.gridLayout.addWidget(self.align_frame, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.des)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Global  Alignment"))
        self.textBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Noto Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Global alignment is useful for comparing entire sequences of DNA or protein to reveal evolutionary relationships and functional similarities. The algorithm used in this part is Needleman-Wunsch Algorithm.</p></body></html>',
            )
        )
        self.label_2.setText(_translate("Form", "Sequence 1"))
        self.load_seq1.setText(_translate("Form", "Load"))
        self.textEdit.setPlaceholderText(_translate("Form", "Enter First Sequence"))
        self.label_3.setText(_translate("Form", "Sequence 2"))
        self.load_seq2.setText(_translate("Form", "Load"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "Enter Second Sequence"))
        self.label_4.setText(_translate("Form", "Aligned Sequences"))
        self.clear_btn.setText(_translate("Form", "Clear"))
        self.align_btn.setText(_translate("Form", "Align"))
        self.save_btn.setText(_translate("Form", "Save"))
