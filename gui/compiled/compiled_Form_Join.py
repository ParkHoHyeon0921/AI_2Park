# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Form_Join.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form_Join(object):
    def setupUi(self, Form_Join):
        Form_Join.setObjectName("Form_Join")
        Form_Join.resize(397, 506)
        Form_Join.setStyleSheet("#label_title{\n"
"    \n"
"    font: 75 14pt \"맑은 고딕\";\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Join)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_login_form = QtWidgets.QWidget(Form_Join)
        self.widget_login_form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_login_form.setObjectName("widget_login_form")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_login_form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget_login_form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.label_title = QtWidgets.QLabel(self.widget_2)
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_4.addWidget(self.label_title)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(135, 0))
        self.lineEdit_username.setMaximumSize(QtCore.QSize(135, 16777215))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout_6.addWidget(self.lineEdit_username)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_5.addWidget(self.lineEdit_password)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.widget_10 = QtWidgets.QWidget(self.widget_2)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.widget_10)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_username_3 = QtWidgets.QLineEdit(self.widget_10)
        self.lineEdit_username_3.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_username_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_username_3.setObjectName("lineEdit_username_3")
        self.horizontalLayout_8.addWidget(self.lineEdit_username_3)
        self.verticalLayout_4.addWidget(self.widget_10)
        self.widget_9 = QtWidgets.QWidget(self.widget_2)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.widget_9)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_username_2 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_username_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_username_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_username_2.setObjectName("lineEdit_username_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_username_2)
        self.verticalLayout_4.addWidget(self.widget_9)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_6)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.widget_6)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.widget_8)
        self.verticalLayout_4.addWidget(self.widget_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget_login_form)

        self.retranslateUi(Form_Join)
        QtCore.QMetaObject.connectSlotsByName(Form_Join)

    def retranslateUi(self, Form_Join):
        _translate = QtCore.QCoreApplication.translate
        Form_Join.setWindowTitle(_translate("Form_Join", "Form"))
        self.label_title.setText(_translate("Form_Join", "WD 회원가입 페이지"))
        self.label_3.setText(_translate("Form_Join", "아이디"))
        self.pushButton_2.setText(_translate("Form_Join", "중복확인"))
        self.label_4.setText(_translate("Form_Join", "비밀번호"))
        self.label_6.setText(_translate("Form_Join", "이름"))
        self.label_5.setText(_translate("Form_Join", "이메일"))
        self.label.setText(_translate("Form_Join", "안내 문구"))
        self.label_7.setText(_translate("Form_Join", "이용약관"))
        self.pushButton_3.setText(_translate("Form_Join", "읽기"))
        self.checkBox.setText(_translate("Form_Join", "확인했습니다."))
        self.pushButton.setText(_translate("Form_Join", "회원가입하기"))