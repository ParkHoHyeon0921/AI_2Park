# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Form_Camera.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Camera(object):
    def setupUi(self, Form_Camera):
        Form_Camera.setObjectName("Form_Camera")
        Form_Camera.resize(970, 700)
        Form_Camera.setStyleSheet("#label_camera{\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"\n"
"#label_title, #label_title_banner{\n"
"    font: bold 16pt \"맑은 고딕\";\n"
"}\n"
"\n"
"#label_status {\n"
"    font: bold 14pt \"맑은 고딕\";\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #DFDFDF;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #9FC5E8;\n"
"    border: 2px solid #C9DAF8;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4A86E8;\n"
"    border: 2px solid #86AEEF;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Camera)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(Form_Camera)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.widget_4)
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_camera = QtWidgets.QLabel(self.widget)
        self.label_camera.setText("")
        self.label_camera.setObjectName("label_camera")
        self.horizontalLayout_2.addWidget(self.label_camera)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_title_banner = QtWidgets.QLabel(self.widget_5)
        self.label_title_banner.setMinimumSize(QtCore.QSize(0, 30))
        self.label_title_banner.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_title_banner.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_banner.setObjectName("label_title_banner")
        self.verticalLayout_3.addWidget(self.label_title_banner)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_medi_list = QtWidgets.QWidget(self.widget_6)
        self.widget_medi_list.setObjectName("widget_medi_list")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_medi_list)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4.addWidget(self.widget_medi_list)
        self.scrollArea = QtWidgets.QScrollArea(self.widget_6)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 506))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.layout_medi_list = QtWidgets.QVBoxLayout()
        self.layout_medi_list.setSpacing(0)
        self.layout_medi_list.setObjectName("layout_medi_list")
        self.verticalLayout_7.addLayout(self.layout_medi_list)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_6.addWidget(self.widget_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.horizontalLayout.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(Form_Camera)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 90))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_status = QtWidgets.QLabel(self.widget_2)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_3.addWidget(self.label_status)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form_Camera)
        QtCore.QMetaObject.connectSlotsByName(Form_Camera)

    def retranslateUi(self, Form_Camera):
        _translate = QtCore.QCoreApplication.translate
        Form_Camera.setWindowTitle(_translate("Form_Camera", "Form"))
        self.label_title.setText(_translate("Form_Camera", "실시간 카메라 영상"))
        self.label_title_banner.setText(_translate("Form_Camera", "확인된 경구약 목록"))
        self.label_status.setText(_translate("Form_Camera", "현재까지 0종 약물이 확인되었습니다."))
