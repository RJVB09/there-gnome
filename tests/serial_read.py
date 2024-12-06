import winsound

import matplotlib.pyplot as plt
import serial as ser

arduino = ser.Serial(port="COM9", baudrate=9600, timeout=0.1)

data_list = []

while 1:

    data = arduino.readline()

    decoded_data = data.decode("utf-8")
    #data_list.append(int(decoded_data))
    #print(int(decoded_data))
    # print(int(800.0/1500.0 * int(decoded_data) + 200.0))
    winsound.Beep(int(700.0/1500.0 * int(decoded_data) + 200.0), 10)


# print(rm.list_resources())


# device = rm.open_resource("ASRL9::INSTR", read_termination="\r\n", write_termination="\n")

# print(device.query(""))

# rm.close()
