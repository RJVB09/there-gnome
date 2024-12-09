import matplotlib.pyplot as plt
import serial as ser
import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot
from there_gnome.ui.gui import Ui_MainWindow
import pyqtgraph as pg
import numpy as np

from pysinewave import SineWave

arduino = ser.Serial(port="COM4", baudrate=9600, timeout=0.1)

sinewave = SineWave(pitch = 12, pitch_per_second = 1000)

playing = False

sinewave.play()

def distance_to_pitch(distance, length, offset, flip):
    if flip:
        return int(-distance / length + offset - 1)
    else:
        return int(distance / length + offset)


while 1:

    data = arduino.readline()

    decoded_data = data.decode("utf-8")
    distance_mm = int(decoded_data)
    #data_list.append(int(decoded_data))

    #sinewave.set_pitch(int(distance_mm/20 - 1))
    sinewave.set_pitch(18-int(distance_mm/20 - 1))
    #sinewave.set_frequency(distance_mm + 200)

    print(distance_mm)


# print(rm.list_resources())


# device = rm.open_resource("ASRL9::INSTR", read_termination="\r\n", write_termination="\n")

# print(device.query(""))

# rm.close()


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):

        # Call the inherited init.
        super().__init__()

        # Prevent saving nothing
        self.experiment_ran = False
        self.measurement_running = False  # Flag to track if measurement is running
        
        # Use the UI created in the designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    



def main():
    pg.setConfigOption("background", "#161616")
    pg.setConfigOption("foreground", "w")
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  