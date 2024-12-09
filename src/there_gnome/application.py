import sys
import threading
import numpy as np
import serial as ser
from pysinewave import SineWave
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
from there_gnome.ui.gui import Ui_MainWindow

# Main class for the user interface
class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize parent class

        # Flags and state variables
        self.experiment_ran = False
        self.measurement_running = False  # Track if measurement is running
        self.app_running = True
        self.in_range = False
        self.playing = False

        # Serial communication setup
        self.pitch_arduino = ser.Serial(port="COM4", baudrate=9600, timeout=0.1)

        # SineWave setup for sound generation
        self.sinewave = SineWave(pitch=12, pitch_per_second=1000, decibels=0, decibels_per_second=10000)

        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect UI elements to functionality
        self.ui.playButton.pressed.connect(self.play_sine)
        self.ui.stopButton.pressed.connect(self.stop_sine)

        self.ui.lengthDoubleSpinBox.valueChanged.connect(self.refresh_options_and_graph)
        self.ui.offsetSpinBox.valueChanged.connect(self.refresh_options_and_graph)
        self.ui.invertedToggle.checkStateChanged.connect(self.refresh_options_and_graph)
        self.ui.rangeDoubleSpinBox.valueChanged.connect(self.refresh_options_and_graph)
        self.ui.volfalloffDoubleSpinBox.valueChanged.connect(self.refresh_options_and_graph)

        # Start the audio thread
        self.audio_thread = threading.Thread(target=self.update_sound)
        self.audio_thread.start()

        # Initialize options and graph
        self.refresh_options_and_graph()

    def distance_to_pitch(self, distance):
        """Convert distance to a pitch value."""
        if self.inverted:
            return int(np.floor(-distance / self.note_length + self.offset + 1))
        else:
            return int(np.floor(distance / self.note_length + self.offset))

    def distance_to_volume(self, distance):
        """Convert distance to a volume value."""
        return 1 - (1 / (self.range ** (2 ** self.volfalloff))) * (distance ** (2 ** self.volfalloff))

    @Slot()
    def refresh_options_and_graph(self):
        """Update graph and related options."""
        self.note_length = self.ui.lengthDoubleSpinBox.value()
        self.offset = self.ui.offsetSpinBox.value()
        self.inverted = self.ui.invertedToggle.isChecked()
        self.range = self.ui.rangeDoubleSpinBox.value()
        self.volfalloff = self.ui.volfalloffDoubleSpinBox.value()

        # Clear and update the plot
        self.ui.plot_widget.clear()
        x = np.linspace(0, self.range, 600)
        self.ui.plot_widget.plot(x, [self.distance_to_pitch(X) for X in x], pen={"color": "m", "width": 2})
        self.ui.plot_widget.plot(x, [self.distance_to_volume(X) for X in x], pen={"color": "y", "width": 2})
        self.ui.plot_widget.setLabel("left", "Note index (magenta) / Volume (yellow)")
        self.ui.plot_widget.setLabel("bottom", "Distance (mm)")
        self.ui.plot_widget.showGrid(x=True, y=True)

    @Slot()
    def play_sine(self):
        """Play the sine wave."""
        self.sinewave.play()
        self.playing = True

    @Slot()
    def stop_sine(self):
        """Stop the sine wave."""
        self.sinewave.stop()
        self.playing = False

    def update_sound(self):
        """Thread function to update sound properties based on sensor data."""
        while self.app_running:
            try:
                # Read and decode data from Arduino
                data = self.pitch_arduino.readline()
                pitch_distance_mm = int(data.decode("utf-8"))

                # Update range state and UI if range changes
                if self.in_range != (pitch_distance_mm <= self.range) and self.playing:
                    self.ui.change_butt(not self.in_range)
                    self.ui.change_laser_eyes(not self.in_range)
                self.in_range = pitch_distance_mm <= self.range

                # Adjust pitch and volume based on distance
                out_of_range_multiplier = 10 ** -100 if not self.in_range else 1
                self.sinewave.set_pitch(self.distance_to_pitch(pitch_distance_mm))
                self.sinewave.set_volume(np.log2(1 * out_of_range_multiplier))

            except (ValueError, UnicodeDecodeError):
                # Handle invalid or noisy data gracefully
                continue

        print("App closed")

# Main function
def main():
    pg.setConfigOption("background", "#161616")  # Set plot background color
    pg.setConfigOption("foreground", "w")  # Set plot foreground color
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()

    # Clean up on app exit
    def on_exit():
        ui.app_running = False
        ui.audio_thread.join()

    app.aboutToQuit.connect(on_exit)
    sys.exit(app.exec())

# Entry point
if __name__ == "__main__":
    main()
