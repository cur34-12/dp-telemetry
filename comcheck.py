import obd

# Scan Ports
ports = obd.scan_serial()      # return list of valid USB or RF ports
print(ports)