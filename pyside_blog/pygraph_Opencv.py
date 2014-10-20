# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pygraph_Opencv.ui'
#
# Created: Mon Oct 20 12:33:32 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Qt_CV_MainWindow(object):
    def setupUi(self, Qt_CV_MainWindow):
        Qt_CV_MainWindow.setObjectName("Qt_CV_MainWindow")
        Qt_CV_MainWindow.resize(1052, 766)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Qt_CV_MainWindow.sizePolicy().hasHeightForWidth())
        Qt_CV_MainWindow.setSizePolicy(sizePolicy)
        Qt_CV_MainWindow.setMouseTracking(True)
        Qt_CV_MainWindow.setAcceptDrops(False)
        self.centralwidget = QtGui.QWidget(Qt_CV_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 50, 411, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_edit = QtGui.QLineEdit(self.layoutWidget)
        self.file_edit.setObjectName("file_edit")
        self.horizontalLayout.addWidget(self.file_edit)
        self.file_button = QtGui.QPushButton(self.layoutWidget)
        self.file_button.setObjectName("file_button")
        self.horizontalLayout.addWidget(self.file_button)
        self.pic_view = GraphicsLayoutWidget(self.centralwidget)
        self.pic_view.setGeometry(QtCore.QRect(519, 190, 512, 512))
        self.pic_view.setViewportUpdateMode(QtGui.QGraphicsView.FullViewportUpdate)
        self.pic_view.setObjectName("pic_view")
        self.exec_button = QtGui.QPushButton(self.centralwidget)
        self.exec_button.setGeometry(QtCore.QRect(640, 10, 81, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exec_button.sizePolicy().hasHeightForWidth())
        self.exec_button.setSizePolicy(sizePolicy)
        self.exec_button.setObjectName("exec_button")
        self.file_scrollbar = QtGui.QScrollBar(self.centralwidget)
        self.file_scrollbar.setGeometry(QtCore.QRect(400, 140, 421, 41))
        self.file_scrollbar.setProperty("value", 50)
        self.file_scrollbar.setOrientation(QtCore.Qt.Horizontal)
        self.file_scrollbar.setObjectName("file_scrollbar")
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 354, 120, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.hist_view = PlotWidget(self.centralwidget)
        self.hist_view.setGeometry(QtCore.QRect(397, 190, 121, 511))
        self.hist_view.setObjectName("hist_view")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 320, 391, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.color_combo = QtGui.QComboBox(self.centralwidget)
        self.color_combo.setGeometry(QtCore.QRect(110, 168, 271, 22))
        self.color_combo.setObjectName("color_combo")
        self.color_combo.addItem("")
        self.color_combo.addItem("")
        self.color_combo.addItem("")
        self.color_combo.addItem("")
        self.eject_edge_or_not = QtGui.QCheckBox(self.centralwidget)
        self.eject_edge_or_not.setGeometry(QtCore.QRect(20, 620, 171, 19))
        self.eject_edge_or_not.setObjectName("eject_edge_or_not")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 198, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.smooth_combo = QtGui.QComboBox(self.centralwidget)
        self.smooth_combo.setGeometry(QtCore.QRect(110, 200, 271, 22))
        self.smooth_combo.setObjectName("smooth_combo")
        self.smooth_combo.addItem("")
        self.smooth_combo.addItem("")
        self.smooth_combo.addItem("")
        self.smooth_combo.addItem("")
        self.smooth_combo.addItem("")
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 440, 391, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 450, 321, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(75)
        font.setUnderline(True)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 330, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(75)
        font.setUnderline(True)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 221, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(75)
        font.setUnderline(True)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setObjectName("label_9")
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 110, 391, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 221, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(75)
        font.setUnderline(True)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setObjectName("label_10")
        self.Mode_combo = QtGui.QComboBox(self.centralwidget)
        self.Mode_combo.setGeometry(QtCore.QRect(110, 50, 271, 22))
        self.Mode_combo.setObjectName("Mode_combo")
        self.Mode_combo.addItem("")
        self.Mode_combo.addItem("")
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 50, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 560, 391, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 570, 171, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(75)
        font.setUnderline(True)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setTextFormat(QtCore.Qt.RichText)
        self.label_12.setObjectName("label_12")
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 483, 121, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.threshold1_edit = QtGui.QLineEdit(self.centralwidget)
        self.threshold1_edit.setGeometry(QtCore.QRect(140, 354, 61, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold1_edit.sizePolicy().hasHeightForWidth())
        self.threshold1_edit.setSizePolicy(sizePolicy)
        self.threshold1_edit.setMaxLength(255)
        self.threshold1_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.threshold1_edit.setObjectName("threshold1_edit")
        self.threshold2_edit = QtGui.QLineEdit(self.centralwidget)
        self.threshold2_edit.setGeometry(QtCore.QRect(140, 394, 61, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold2_edit.sizePolicy().hasHeightForWidth())
        self.threshold2_edit.setSizePolicy(sizePolicy)
        self.threshold2_edit.setMaxLength(254)
        self.threshold2_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.threshold2_edit.setObjectName("threshold2_edit")
        self.threshold1_slider = QtGui.QSlider(self.centralwidget)
        self.threshold1_slider.setGeometry(QtCore.QRect(210, 359, 179, 19))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold1_slider.sizePolicy().hasHeightForWidth())
        self.threshold1_slider.setSizePolicy(sizePolicy)
        self.threshold1_slider.setMaximum(254)
        self.threshold1_slider.setProperty("value", 160)
        self.threshold1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold1_slider.setObjectName("threshold1_slider")
        self.threshold2_slider = QtGui.QSlider(self.centralwidget)
        self.threshold2_slider.setGeometry(QtCore.QRect(210, 400, 179, 19))
        self.threshold2_slider.setMaximum(254)
        self.threshold2_slider.setProperty("value", 80)
        self.threshold2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold2_slider.setObjectName("threshold2_slider")
        self.min_area_edit = QtGui.QLineEdit(self.centralwidget)
        self.min_area_edit.setGeometry(QtCore.QRect(140, 523, 59, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_area_edit.sizePolicy().hasHeightForWidth())
        self.min_area_edit.setSizePolicy(sizePolicy)
        self.min_area_edit.setMaxLength(1000)
        self.min_area_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.min_area_edit.setObjectName("min_area_edit")
        self.max_area_edit = QtGui.QLineEdit(self.centralwidget)
        self.max_area_edit.setGeometry(QtCore.QRect(140, 483, 61, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_area_edit.sizePolicy().hasHeightForWidth())
        self.max_area_edit.setSizePolicy(sizePolicy)
        self.max_area_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.max_area_edit.setObjectName("max_area_edit")
        self.max_area_slider = QtGui.QSlider(self.centralwidget)
        self.max_area_slider.setGeometry(QtCore.QRect(210, 488, 179, 19))
        self.max_area_slider.setMaximum(90000)
        self.max_area_slider.setProperty("value", 5000)
        self.max_area_slider.setOrientation(QtCore.Qt.Horizontal)
        self.max_area_slider.setObjectName("max_area_slider")
        self.min_area_slider = QtGui.QSlider(self.centralwidget)
        self.min_area_slider.setGeometry(QtCore.QRect(210, 530, 179, 19))
        self.min_area_slider.setMaximum(90000)
        self.min_area_slider.setProperty("value", 120)
        self.min_area_slider.setOrientation(QtCore.Qt.Horizontal)
        self.min_area_slider.setObjectName("min_area_slider")
        self.form_view_or_image = QtGui.QCheckBox(self.centralwidget)
        self.form_view_or_image.setGeometry(QtCore.QRect(20, 660, 181, 19))
        self.form_view_or_image.setObjectName("form_view_or_image")
        self.threshold1_edit_2 = QtGui.QLineEdit(self.centralwidget)
        self.threshold1_edit_2.setGeometry(QtCore.QRect(400, 11, 51, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold1_edit_2.sizePolicy().hasHeightForWidth())
        self.threshold1_edit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.threshold1_edit_2.setFont(font)
        self.threshold1_edit_2.setMaxLength(1000)
        self.threshold1_edit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.threshold1_edit_2.setObjectName("threshold1_edit_2")
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 6, 271, 46))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.sub_view = GraphicsLayoutWidget(self.centralwidget)
        self.sub_view.setGeometry(QtCore.QRect(830, 0, 201, 181))
        self.sub_view.setObjectName("sub_view")
        self.EBA_button = QtGui.QPushButton(self.centralwidget)
        self.EBA_button.setGeometry(QtCore.QRect(730, 10, 81, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EBA_button.sizePolicy().hasHeightForWidth())
        self.EBA_button.setSizePolicy(sizePolicy)
        self.EBA_button.setObjectName("EBA_button")
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(200, 620, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.smooth_combo_2 = QtGui.QComboBox(self.centralwidget)
        self.smooth_combo_2.setGeometry(QtCore.QRect(290, 620, 81, 22))
        self.smooth_combo_2.setObjectName("smooth_combo_2")
        self.smooth_combo_2.addItem("")
        self.smooth_combo_2.addItem("")
        self.smooth_combo_2.addItem("")
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.smooth_combo_3 = QtGui.QComboBox(self.centralwidget)
        self.smooth_combo_3.setGeometry(QtCore.QRect(110, 230, 271, 22))
        self.smooth_combo_3.setObjectName("smooth_combo_3")
        self.smooth_combo_3.addItem("")
        self.smooth_combo_3.addItem("")
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 260, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(110, 250, 271, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.file_edit_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.file_edit_2.setObjectName("file_edit_2")
        self.horizontalLayout_2.addWidget(self.file_edit_2)
        self.file_button_2 = QtGui.QPushButton(self.layoutWidget_2)
        self.file_button_2.setObjectName("file_button_2")
        self.horizontalLayout_2.addWidget(self.file_button_2)
        Qt_CV_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Qt_CV_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Qt_CV_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Qt_CV_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Qt_CV_MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(Qt_CV_MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Qt_CV_MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), Qt_CV_MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(Qt_CV_MainWindow)

    def retranslateUi(self, Qt_CV_MainWindow):
        Qt_CV_MainWindow.setWindowTitle(QtGui.QApplication.translate("Qt_CV_MainWindow", "Qt_OpenCV", None, QtGui.QApplication.UnicodeUTF8))
        self.file_button.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.exec_button.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "High Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Low Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.color_combo.setItemText(0, QtGui.QApplication.translate("Qt_CV_MainWindow", "None (Gray Scale)", None, QtGui.QApplication.UnicodeUTF8))
        self.color_combo.setItemText(1, QtGui.QApplication.translate("Qt_CV_MainWindow", "Red   (Extract Red Color)", None, QtGui.QApplication.UnicodeUTF8))
        self.color_combo.setItemText(2, QtGui.QApplication.translate("Qt_CV_MainWindow", "Green(Extract Green Color)", None, QtGui.QApplication.UnicodeUTF8))
        self.color_combo.setItemText(3, QtGui.QApplication.translate("Qt_CV_MainWindow", "Blue  (Extract Blue Color)", None, QtGui.QApplication.UnicodeUTF8))
        self.eject_edge_or_not.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Eject Edge Contours", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Color filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Smoothing", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo.setItemText(0, QtGui.QApplication.translate("Qt_CV_MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo.setItemText(1, QtGui.QApplication.translate("Qt_CV_MainWindow", "Bilateral", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo.setItemText(2, QtGui.QApplication.translate("Qt_CV_MainWindow", "GaussianBlur", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo.setItemText(3, QtGui.QApplication.translate("Qt_CV_MainWindow", "medianBlur ", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo.setItemText(4, QtGui.QApplication.translate("Qt_CV_MainWindow", "Blur", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Range of Contour Areas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Filter & Smoothig", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.Mode_combo.setItemText(0, QtGui.QApplication.translate("Qt_CV_MainWindow", "Single mode (Files)", None, QtGui.QApplication.UnicodeUTF8))
        self.Mode_combo.setItemText(1, QtGui.QApplication.translate("Qt_CV_MainWindow", "For Folders   (SubDirectory)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Other Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Max Area Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Min Area Size", None, QtGui.QApplication.UnicodeUTF8))
        self.threshold1_edit.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "160", None, QtGui.QApplication.UnicodeUTF8))
        self.threshold2_edit.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "80", None, QtGui.QApplication.UnicodeUTF8))
        self.min_area_edit.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "120", None, QtGui.QApplication.UnicodeUTF8))
        self.max_area_edit.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "5000", None, QtGui.QApplication.UnicodeUTF8))
        self.form_view_or_image.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Adjust View from Image", None, QtGui.QApplication.UnicodeUTF8))
        self.threshold1_edit_2.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "μ㎡/pix　[Enter this number]", None, QtGui.QApplication.UnicodeUTF8))
        self.EBA_button.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "EBA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Extention", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo_2.setItemText(0, QtGui.QApplication.translate("Qt_CV_MainWindow", "*.jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo_2.setItemText(1, QtGui.QApplication.translate("Qt_CV_MainWindow", "*.bmp", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo_2.setItemText(2, QtGui.QApplication.translate("Qt_CV_MainWindow", "*.tiff", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Edge", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo_3.setItemText(0, QtGui.QApplication.translate("Qt_CV_MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth_combo_3.setItemText(1, QtGui.QApplication.translate("Qt_CV_MainWindow", "Canny", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Shading", None, QtGui.QApplication.UnicodeUTF8))
        self.file_button_2.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Qt_CV_MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("Qt_CV_MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import GraphicsLayoutWidget, PlotWidget
