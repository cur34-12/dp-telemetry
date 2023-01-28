import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
          
url = "http://localhost:8086"
token = "fLPVuTLeWiYziE5ykVnxfti2168D8OYzKTeHGTLyQdT737JWroi75ttxS-KuFzA2mLICHkDlohU301FBbh3JCQ=="
org = "7ae34c5005339f61"
bucket = "dptelemetry"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("Speed").field("speed", 25.3)
write_api.write(bucket=bucket, org=org, record=p)
