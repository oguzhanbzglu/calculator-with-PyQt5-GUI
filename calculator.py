import sys
from _calculatorForm import Ui_Calculator
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon




class Window(QMainWindow):
    firstNum = None
    secondNum = None

    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_Calculator()
        self.ui.setupUi(self)

        #NUMBER BUTTONS
        self.ui.btn0.clicked.connect(self.buttonText)
        self.ui.btn1.clicked.connect(self.buttonText)
        self.ui.btn2.clicked.connect(self.buttonText)
        self.ui.btn3.clicked.connect(self.buttonText)
        self.ui.btn4.clicked.connect(self.buttonText)
        self.ui.btn5.clicked.connect(self.buttonText)
        self.ui.btn6.clicked.connect(self.buttonText)
        self.ui.btn7.clicked.connect(self.buttonText)
        self.ui.btn8.clicked.connect(self.buttonText)
        self.ui.btn9.clicked.connect(self.buttonText)

        #SEYMBOL BUTTONS
        self.ui.btnPoint.clicked.connect(self.buttonPoint)
        self.ui.btnChange.clicked.connect(self.changeButton)
        self.ui.btnPercent.clicked.connect(self.percentButton)
        self.ui.btnC.clicked.connect(self.clearButton)


        #CALCULATİON BUTTONS
        self.ui.btnResult.clicked.connect(self.response)
        self.ui.btnAdd.clicked.connect(self.calculation)
        self.ui.btnSubtract.clicked.connect(self.calculation)
        self.ui.btnMultiply.clicked.connect(self.calculation)
        self.ui.btnDivide.clicked.connect(self.calculation)

        #CHECKABLED
        self.ui.btnAdd.setCheckable(True)
        self.ui.btnSubtract.setCheckable(True)
        self.ui.btnMultiply.setCheckable(True)
        self.ui.btnDivide.setCheckable(True)


    def calculation(self):
        button = self.sender()
        self.firstNum = float(self.ui.txtResult.text())
        button.setChecked(True)
        print(self.firstNum)

    def clearButton(self):
        sender = self.sender().text()
        if sender == 'C':
            self.ui.txtResult.clear()
            self.ui.txtResult.setText(str(0))
            self.firstNum = False
            self.secondNum = False
            self.ui.btnAdd.setChecked(False)
            self.ui.btnSubtract.setChecked(False)
            self.ui.btnMultiply.setChecked(False)
            self.ui.btnDivide.setChecked(False)


    def buttonPoint(self):
        sender = self.sender().text()
        if '.' not in self.ui.txtResult.text():
            self.ui.txtResult.setText(self.ui.txtResult.text() + sender)


    def buttonText(self):
        sender = self.sender()
        if (self.ui.btnAdd.isChecked() or self.ui.btnSubtract.isChecked() or self.ui.btnMultiply.isChecked() or self.ui.btnDivide.isChecked()) and (not self.secondNum):
            self.ui.txtResult.setText(format(float(sender.text()),".15g")) #Baştaki sıfırı sildik.
            self.secondNum = True

        else:
            self.ui.txtResult.setText(format(float(self.ui.txtResult.text() + sender.text()), ".15g"))

    def percentButton(self):
        percent = float(self.ui.txtResult.text())*(0.01)
        self.ui.txtResult.setText(str(percent))

    def changeButton(self):
        changeNum = float(self.ui.txtResult.text())*(-1)
        self.ui.txtResult.setText(str(changeNum))

    def response(self):
        secondValue = float(self.ui.txtResult.text())
        print(secondValue)

        if self.ui.btnAdd.isChecked():
            newValue = self.firstNum+secondValue
            self.ui.txtResult.setText(format(newValue, '.15g'))
            self.ui.btnAdd.setChecked(False)

        if self.ui.btnSubtract.isChecked():
            newValue = self.firstNum-secondValue
            self.ui.txtResult.setText(format(newValue, '.15g'))
            self.ui.btnSubtract.setChecked(False)

        if self.ui.btnMultiply.isChecked():
            newValue = self.firstNum*secondValue
            self.ui.txtResult.setText(format(newValue, '.15g'))
            self.ui.btnMultiply.setChecked(False)

        if self.ui.btnDivide.isChecked():
            newValue = self.firstNum/secondValue
            self.ui.txtResult.setText(format(newValue, '.15g'))
            self.ui.btnDivide.setChecked(False)



def myApp():

    app = QApplication(sys.argv)
    win = Window()
    win.setWindowTitle('Calculator')
    win.setWindowIcon(QIcon('calculator.png'))
    win.setToolTip('Oguzhan')
    win.show()
    sys.exit(app.exec_())

myApp()