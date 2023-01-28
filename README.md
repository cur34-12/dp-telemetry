# dp-telemetry

ELM327 sourced telemetry app connected for Grafana

## Using

* [Python 3.11](https://python.org)
* [PythonOBD Github](https://github.com/brendan-w/python-OBD)
* [PythonOBD Docs](https://python-obd.readthedocs.io/en/latest/)
* [OBD Emulator](https://github.com/Ircama/ELM327-emulator)
* [COM2COM](https://sourceforge.net/projects/com0com/)
* [InfluxDB](https://www.influxdata.com/)
* [Grafana](https://grafana.com/)

## Setup

1. Install [Python 3.11](https://python.org) and make sure `python` is added to path
2. Make sure Pip is installed/updated
    `python -m pip install --upgrade pip`
3. Install python-OBD using terminal:
    `python -m pip install obd`
4. Install the ELM327-emulator using terminal:
    `python -m pip install ELM327-emulator`
5. Install [InfluxDB](https://www.influxdata.com/) and go through basic configuration steps (and make sure its running)
6. Create a bucket in InfluxDB to use for storing telemetry
7. Copy config.sample.ini to config.ini
8. Create an all access API key in InfluxDB and update the key in the config.ini file
9. Update the URL, bucket name in the config file based on your initial configuration of InfluxDB
10. Get the OrgID from the InfluxDB url after http://localhost:8086/orgs/{orgId} and update the field in config.ini
11. Install [Grafana](https://grafana.com/) and go through basic configuration steps
12. In Grafana go to Configuration > Data Sources > Add source > Influx DB. Change Query Language to flux then set the HTTP > URL and InfluxDB Details > Organization, Token and Bucket.  Turn off basic auth if it came on by default.
13. In Grafana go to Dashboards > Create New Dashboard > Import Dashboard > Paste JSON and copy the contents of the grafana.json file into there.
14. Install [COM2COM](https://sourceforge.net/projects/com0com/)
15. Run ELM327-emulator with:
    `python -m elm`
16. Look for the line indicating which COM port the emulator is running on and update the value in config.ini. There is also a comcheck.py file for helping debug COM port related issues.
17. Run the main python file for collecting telemetry and check the data is coming in in both Grafana and InfluxDB.
    `python main.py`
18. Enjoy...hope it works.
