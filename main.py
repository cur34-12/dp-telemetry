import obd
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import time

# Enable Debugging
# obd.logger.setLevel(obd.logging.DEBUG)

# Setup InfluxDB config an client
url = "http://localhost:8086"
token = "fLPVuTLeWiYziE5ykVnxfti2168D8OYzKTeHGTLyQdT737JWroi75ttxS-KuFzA2mLICHkDlohU301FBbh3JCQ=="
org = "7ae34c5005339f61"
bucket = "dptelemetry"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

# Scan Ports
# ports = obd.scan_serial()      # return list of valid USB or RF ports
# print(ports)

# Initiate the connection to the OBDII Emulator
connection = obd.OBD(portstr="COM5", baudrate=115200, protocol=None, fast=True, timeout=0.1, check_voltage=True)

while 1<2:
    # Core
    responseSpeed = connection.query(obd.commands.SPEED)
    if responseSpeed.is_null():
        break
    p = influxdb_client.Point("Core").field("speed", responseSpeed.value.magnitude)

    responseRpm = connection.query(obd.commands.RPM)
    if responseRpm.is_null():
        break
    r = influxdb_client.Point("Core").field("rpm", responseRpm.value.magnitude)

    # Cooling
    responseCoolantTemp = connection.query(obd.commands.COOLANT_TEMP)
    if responseCoolantTemp.is_null():
        break
    q = influxdb_client.Point("Cooling").field("coolant-temp", responseCoolantTemp.value.magnitude)

    # value.magnitude removes the units as part of the response object
    # print(responseSpeed.value.magnitude)

    # Write Data to Influx DB
    write_api = client.write_api(write_options=SYNCHRONOUS)


    write_api.write(bucket=bucket, org=org, record=p)
    write_api.write(bucket=bucket, org=org, record=r)    
    write_api.write(bucket=bucket, org=org, record=q)
    
    # Sleep for 1 second before repeating loop
    time.sleep(1)