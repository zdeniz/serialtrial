from PyQt5 import QtCore, QtGui, QtWidgets
from UI.mainwindow import Ui_MainWindow as MainWindow
import sys
import glob
import serial
import serial.tools.list_ports

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/ttyUSB*') # ubuntu is /dev/ttyUSB0
    elif sys.platform.startswith('darwin'):
        # ports = glob.glob('/dev/tty.*')
        ports = glob.glob('/dev/tty.SLAB_USBtoUART*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except serial.SerialException as e:
            if e.errno == 13:
                raise e
            pass
        except OSError:
            pass
    return result


class MainWindowClass(QtWidgets.QMainWindow, MainWindow):

    val1 = 1
    val2 = "123"

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    print(serial_ports())
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)

    app = QtWidgets.QApplication(sys.argv)
    UIMain = MainWindowClass()
    UIMain.show()
    # screenGeometry = QtGui.QApplication.desktop().availableGeometry()
    # UIMain.resize(screenGeometry.width(), screenGeometry.height())
    sys.exit(app.exec_())

#    app = QtGui.QApplication()