import matplotlib.pyplot as plt
import serial as ser
import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot
from there_gnome.ui.gui import Ui_MainWindow
import pyqtgraph as pg
import numpy as np
import threading

from pysinewave import SineWave


sinewave = SineWave(pitch = 12, pitch_per_second = 1000)

playing = False

#sinewave.play()


while False:

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

        self.pitch_arduino = ser.Serial(port="COM4", baudrate=9600, timeout=0.1)
        #self.volume_arduino = ser.Serial(port="COM4", baudrate=9600, timeout=0.1)

        self.sinewave = SineWave(pitch = 12, pitch_per_second = 1000, decibels=0, decibels_per_second=10000)

        self.playing = False
        
        # Use the UI created in the designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.playButton.pressed.connect(self.play_sine)
        self.ui.stopButton.pressed.connect(self.stop_sine)

        self.refresh_options_and_graph()
        self.ui.lengthDoubleSpinBox.valueChanged.connect(self.refresh_options_and_graph)
        self.ui.offsetSpinBox.valueChanged.connect(self.refresh_options_and_graph)
        self.ui.invertedToggle.checkStateChanged.connect(self.refresh_options_and_graph)
        self.ui.rangeDoubleSpinBox.valueChanged.connect(self.refresh_options_and_graph)
        self.ui.volfalloffDoubleSpinBox.valueChanged.connect(self.refresh_options_and_graph)

        self.app_running = True

        self.audio_thread = threading.Thread(target=self.update_sound, args=())
        self.audio_thread.start()

        self.in_range = False

    def distance_to_pitch(self, distance):
        if self.inverted:
            return int(np.floor(-distance / self.note_length + self.offset + 1))
        else:
            return int(np.floor(distance / self.note_length + self.offset))
    
    def distance_to_volume(self, distance):
        return 1 - 1 / (self.range ** (2 ** self.volfalloff)) * (distance ** (2 ** self.volfalloff))

    @Slot()
    def refresh_options_and_graph(self):
        self.note_length = self.ui.lengthDoubleSpinBox.value()
        self.offset = self.ui.offsetSpinBox.value()
        self.inverted = self.ui.invertedToggle.isChecked()
        self.range = self.ui.rangeDoubleSpinBox.value()
        self.volfalloff = self.ui.volfalloffDoubleSpinBox.value()

        # Clear the graph and plot the data
        self.ui.plot_widget.clear()

        x = np.linspace(0, self.range, 600)

        self.ui.plot_widget.plot(x, [self.distance_to_pitch(X) for X in x], pen = {"color": "m", "width": 2})
        self.ui.plot_widget.plot(x, [self.distance_to_volume(X) for X in x], pen = {"color": "y", "width": 2})
        self.ui.plot_widget.setLabel("left", "Note index (magenta) / Volume (yellow)")
        self.ui.plot_widget.setLabel("bottom", "Distance (mm)")
        self.ui.plot_widget.showGrid(x=True, y=True)

    @Slot()
    def play_sine(self):
        self.sinewave.play()
        self.playing = True

    @Slot()
    def stop_sine(self):
        self.sinewave.stop()
        self.playing = False

    def update_sound(self):
        while self.app_running:
            data = self.pitch_arduino.readline()

            pitch_decoded_data = data.decode("utf-8")
            pitch_distance_mm = int(pitch_decoded_data)

            if self.in_range != (pitch_distance_mm <= self.range) and self.playing:
                self.ui.change_butt(not self.in_range)
                self.ui.change_laser_eyes(not self.in_range)

            self.in_range = pitch_distance_mm <= self.range
            out_of_range_multiplier = 10 ** -100 if not self.in_range else 1
            

            self.sinewave.set_pitch(self.distance_to_pitch(pitch_distance_mm))
            #print(np.log2(1 * out_of_range_multiplier))
            self.sinewave.set_volume(np.log2(1 * out_of_range_multiplier))
            #print(self.distance_to_pitch(pitch_distance_mm))

        print("App closed")
    



def main():
    pg.setConfigOption("background", "#161616")
    pg.setConfigOption("foreground", "w")
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()

    def on_exit():
        ui.app_running = False
        ui.audio_thread.join()

    app.aboutToQuit.connect(on_exit)
    
    sys.exit(app.exec())
    


if __name__ == "__main__":
    main()  