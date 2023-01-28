import obd

# Initiate the connection to the OBDII Emulator
connection = obd.OBD(portstr="COM5", baudrate=115200, protocol=None, fast=True, timeout=0.1, check_voltage=True)

# Send a command
cmdRpm = obd.commands.RPM
responseRpm = connection.query(cmdRpm)
print(responseRpm.value)