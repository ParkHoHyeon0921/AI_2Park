# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Form_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Login(object):
    def setupUi(self, Form_Login):
        Form_Login.setObjectName("Form_Login")
        Form_Login.resize(970, 700)
        Form_Login.setStyleSheet("#widget{    \n"
"    background-image: url(:/image/pills_background.png);\n"
"}\n"
"\n"
"#widget_login_form{\n"
"    background-color: rgba(125, 215, 223, 200);\n"
"}\n"
"\n"
"#widget_slogan{\n"
"    background-color: rgba(134, 174, 239, 200);\n"
"}\n"
"\n"
"#label {\n"
"    color: #31599A;\n"
"}\n"
"\n"
"#label_2{\n"
"    font: bold;\n"
"    color: #F4F4F4;\n"
"}\n"
"\n"
"#widget_6 QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #DFDFDF;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"#widget_6 QPushButton:hover {\n"
"    background-color: #9FC5E8;\n"
"    border: 2px solid #C9DAF8;\n"
"}\n"
"#widget_6 QPushButton:pressed {\n"
"    background-color: #4A86E8;\n"
"    border: 2px solid #86AEEF;\n"
"}\n"
"#label_guide{\n"
"    color: #4A86E8;\n"
"    font: bold 10pt;\n"
"    padding: 5px;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form_Login)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form_Login)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.widget_login_form = QtWidgets.QWidget(self.widget_10)
        self.widget_login_form.setMaximumSize(QtCore.QSize(16777215, 350))
        self.widget_login_form.setObjectName("widget_login_form")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_login_form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget_login_form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
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
        self.lineEdit_username.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_username.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout_6.addWidget(self.lineEdit_username)
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
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_guide = QtWidgets.QLabel(self.widget_6)
        self.label_guide.setAlignment(QtCore.Qt.AlignCenter)
        self.label_guide.setObjectName("label_guide")
        self.verticalLayout_3.addWidget(self.label_guide)
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget_7)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_join = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_join.sizePolicy().hasHeightForWidth())
        self.btn_join.setSizePolicy(sizePolicy)
        self.btn_join.setObjectName("btn_join")
        self.horizontalLayout_4.addWidget(self.btn_join)
        self.btn_login = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_4.addWidget(self.btn_login)
        self.verticalLayout_3.addWidget(self.widget_8)
        self.verticalLayout_4.addWidget(self.widget_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_7.addWidget(self.widget_login_form)
        spacerItem3 = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.widget_slogan = QtWidgets.QWidget(self.widget_10)
        self.widget_slogan.setMaximumSize(QtCore.QSize(16777215, 250))
        self.widget_slogan.setObjectName("widget_slogan")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_slogan)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_slogan)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("배달의민족 도현")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout_7.addWidget(self.widget_slogan)
        spacerItem6 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_5.addWidget(self.widget_10)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_5.addWidget(self.widget_9)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form_Login)
        QtCore.QMetaObject.connectSlotsByName(Form_Login)

    def retranslateUi(self, Form_Login):
        _translate = QtCore.QCoreApplication.translate
        Form_Login.setWindowTitle(_translate("Form_Login", "Form"))
        self.label_3.setText(_translate("Form_Login", "아이디"))
        self.label_4.setText(_translate("Form_Login", "비밀번호"))
        self.label_guide.setText(_translate("Form_Login", "TextLabel"))
        self.checkBox.setText(_translate("Form_Login", "아이디 기억하기"))
        self.btn_join.setText(_translate("Form_Login", "회원가입"))
        self.btn_login.setText(_translate("Form_Login", "로그인"))
        self.label.setText(_translate("Form_Login", "What Drugs?\n"
"경구약.  안전하게 먹자!"))
        self.label_2.setText(_translate("Form_Login", "2차 기업 프로젝트 : 2Parks\n"
" 박광현, 박호현의 인공지능을 활용한\n"
"투약 식별 및 복용관리 프로그램"))
from gui.compiled import my_qrc_rc
