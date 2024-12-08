import matplotlib.pyplot as plt
import serial as ser

from pysinewave import SineWave

arduino = ser.Serial(port="COM4", baudrate=9600, timeout=0.1)

sinewave = SineWave(pitch = 12, pitch_per_second = 1000)

playing = False

sinewave.play()

while 1:

    data = arduino.readline()

    decoded_data = data.decode("utf-8")
    distance_mm = int(decoded_data)
    #data_list.append(int(decoded_data))

    #sinewave.set_pitch(int(distance_mm/20 - 1))
    sinewave.set_pitch(18-int(distance_mm/20 - 1))
    #sinewave.set_frequency(distance_mm + 200)

    print(distance_mm)
    # print(int(800.0/1500.0 * int(decoded_data) + 200.0))


# print(rm.list_resources())


# device = rm.open_resource("ASRL9::INSTR", read_termination="\r\n", write_termination="\n")

# print(device.query(""))

# rm.close()
