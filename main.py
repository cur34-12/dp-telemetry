import obd

# Enable Debugging
# obd.logger.setLevel(obd.logging.DEBUG)

# Scan Ports
# ports = obd.scan_serial()      # return list of valid USB or RF ports
# print(ports)

# Initiate the connection to the OBDII Emulator
connection = obd.OBD(portstr="COM5", baudrate=115200, protocol=None, fast=True, timeout=0.1, check_voltage=True)

# Send a command
cmdRPM = obd.commands.RPM
response = connection.query(cmdRPM)

# value.magnitude removes the units as part of the response object
print(response.value.magnitude)
