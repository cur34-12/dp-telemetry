import obd
import time
import configparser
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# Grab config values
config = configparser.ConfigParser()
config.read('config.ini')

# Enable Debugging
# obd.logger.setLevel(obd.logging.DEBUG)

# Setup InfluxDB config an client
url = config['INFLUX']['url']
token = config['INFLUX']['token']
org = config['INFLUX']['org']
bucket = config['INFLUX']['bucket']

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

# Scan Ports
# ports = obd.scan_serial()      # return list of valid USB or RF ports
# print(ports)

# Initiate the connection to the OBDII Emulator
portstr= config['ODBEMU']['portstr']
connection = obd.OBD(portstr=portstr, baudrate=115200, protocol=None, fast=True, timeout=0.1, check_voltage=True)

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