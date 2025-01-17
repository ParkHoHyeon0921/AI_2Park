# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Form_Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Home(object):
    def setupUi(self, Form_Home):
        Form_Home.setObjectName("Form_Home")
        Form_Home.resize(1005, 774)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_Home.sizePolicy().hasHeightForWidth())
        Form_Home.setSizePolicy(sizePolicy)
        Form_Home.setStyleSheet("#label_camera{\n"
"    background-color: #555555;\n"
"}\n"
"#label_title, #label_title_banner{\n"
"    font: bold 16pt \"맑은 고딕\";\n"
"}\n"
"\n"
"#label_status {\n"
"    font: bold 14pt \"맑은 고딕\";\n"
"}\n"
"\n"
"#label_subtitle_1, #label_subtitle_2, #label_subtitle_3, #label_subtitle_4{\n"
"    font: bold 14pt \"맑은 고딕\";\n"
"}\n"
"#widget_subtitle_1, #widget_subtitle_2,#widget_subtitle_3, #widget_subtitle_4{\n"
"    border: 2px solid #C9DAF8;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form_Home)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setMaximumSize(QtCore.QSize(934, 350))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/image/portrait.jpg"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_subtitle_1 = QtWidgets.QWidget(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_subtitle_1.sizePolicy().hasHeightForWidth())
        self.widget_subtitle_1.setSizePolicy(sizePolicy)
        self.widget_subtitle_1.setMinimumSize(QtCore.QSize(455, 0))
        self.widget_subtitle_1.setMaximumSize(QtCore.QSize(455, 16777215))
        self.widget_subtitle_1.setObjectName("widget_subtitle_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_subtitle_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_subtitle_1 = QtWidgets.QLabel(self.widget_subtitle_1)
        self.label_subtitle_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle_1.setObjectName("label_subtitle_1")
        self.verticalLayout_3.addWidget(self.label_subtitle_1)
        self.label_7 = QtWidgets.QLabel(self.widget_subtitle_1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_10 = QtWidgets.QLabel(self.widget_subtitle_1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.widget_subtitle_1)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.widget_subtitle_1)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget_subtitle_1)
        self.widget_subtitle_2 = QtWidgets.QWidget(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_subtitle_2.sizePolicy().hasHeightForWidth())
        self.widget_subtitle_2.setSizePolicy(sizePolicy)
        self.widget_subtitle_2.setObjectName("widget_subtitle_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_subtitle_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_subtitle_2 = QtWidgets.QLabel(self.widget_subtitle_2)
        self.label_subtitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle_2.setObjectName("label_subtitle_2")
        self.verticalLayout_4.addWidget(self.label_subtitle_2)
        self.label = QtWidgets.QLabel(self.widget_subtitle_2)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_subtitle_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.widget_subtitle_2)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_subtitle_3 = QtWidgets.QWidget(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_subtitle_3.sizePolicy().hasHeightForWidth())
        self.widget_subtitle_3.setSizePolicy(sizePolicy)
        self.widget_subtitle_3.setMinimumSize(QtCore.QSize(455, 0))
        self.widget_subtitle_3.setMaximumSize(QtCore.QSize(455, 16777215))
        self.widget_subtitle_3.setObjectName("widget_subtitle_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_subtitle_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_subtitle_3 = QtWidgets.QLabel(self.widget_subtitle_3)
        self.label_subtitle_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle_3.setObjectName("label_subtitle_3")
        self.verticalLayout_5.addWidget(self.label_subtitle_3)
        self.label_5 = QtWidgets.QLabel(self.widget_subtitle_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.widget_subtitle_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget_subtitle_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label_18 = QtWidgets.QLabel(self.widget_subtitle_3)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.widget_subtitle_3)
        self.widget_subtitle_4 = QtWidgets.QWidget(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_subtitle_4.sizePolicy().hasHeightForWidth())
        self.widget_subtitle_4.setSizePolicy(sizePolicy)
        self.widget_subtitle_4.setObjectName("widget_subtitle_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_subtitle_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_subtitle_4 = QtWidgets.QLabel(self.widget_subtitle_4)
        self.label_subtitle_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle_4.setObjectName("label_subtitle_4")
        self.verticalLayout_6.addWidget(self.label_subtitle_4)
        self.label_14 = QtWidgets.QLabel(self.widget_subtitle_4)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)
        self.label_16 = QtWidgets.QLabel(self.widget_subtitle_4)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.label_15 = QtWidgets.QLabel(self.widget_subtitle_4)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_2.addWidget(self.widget_subtitle_4)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form_Home)
        QtCore.QMetaObject.connectSlotsByName(Form_Home)

    def retranslateUi(self, Form_Home):
        _translate = QtCore.QCoreApplication.translate
        Form_Home.setWindowTitle(_translate("Form_Home", "Form"))
        self.label_subtitle_1.setText(_translate("Form_Home", "기능 소개"))
        self.label_7.setText(_translate("Form_Home", "- 경구약 분류"))
        self.label_10.setText(_translate("Form_Home", "- 회원별 경구약 목록 저장/편집"))
        self.label_11.setText(_translate("Form_Home", "- 회원별 경구약 복용 스케줄러"))
        self.label_12.setText(_translate("Form_Home", "- 경구약 복용 지침 안내"))
        self.label_subtitle_2.setText(_translate("Form_Home", "버전 안내"))
        self.label.setText(_translate("Form_Home", "현재 버전 : V 1.0.1"))
        self.label_2.setText(_translate("Form_Home", "현재 250종의 약물을 구분할 수 있습니다."))
        self.label_subtitle_3.setText(_translate("Form_Home", "레퍼런스 안내"))
        self.label_5.setText(_translate("Form_Home", "* 사이트 : AI Hub"))
        self.label_8.setText(_translate("Form_Home", "* 인공지능 감지 모델 : YOLO v8"))
        self.label_9.setText(_translate("Form_Home", "* 인공지능 분류 모델 : Keras CNN Conv2D"))
        self.label_18.setText(_translate("Form_Home", "* 복용 예측 모델 : Scikit-learn RandomForest 회귀모델"))
        self.label_subtitle_4.setText(_translate("Form_Home", "사용전 주의사항"))
        self.label_14.setText(_translate("Form_Home", "웹캠이 연결되었는지 확인해주세요"))
        self.label_16.setText(_translate("Form_Home", "AI hub에서 제공한 데이터의 일부만 활용했기 때문에 소량의 알약들만 구분 가능합니다."))
        self.label_15.setText(_translate("Form_Home", "경구약 복용 데이터셋은 임의로 만든 것이니 실제와는 다릅니다."))
from gui.compiled import my_qrc_rc
