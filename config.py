# enviro config file

# you may edit this file by hand but if you enter provisioning mode
# then the file will be automatically overwritten with new details

provisioned = True

# enter a nickname for this board
nickname = 'samenmeten'

# network access details
wifi_ssid = 'Loy WLAN'
wifi_password = 'NETT8752021!'

# how often to wake up and take a reading (in minutes)
reading_frequency = 5

# where to upload to ("http", "mqtt", "adafruit_io", "influxdb")
destination = 'http'

# how often to upload data (number of cached readings)
upload_frequency = 1

# web hook settings
custom_http_url = 'https://api.sensor.community/v1/push-sensor-data/'
custom_http_url2 = 'https://api-rrd.madavi.de/data.php'
header_xpin1 ='1'
header_xpin2 ='11'

# mqtt broker settings
mqtt_broker_address = ''
mqtt_broker_username = ''
mqtt_broker_password = ''

# adafruit ui settings
adafruit_io_username = ''
adafruit_io_key = ''

# influxdb settings
influxdb_org = ''
influxdb_url = ''
influxdb_token = ''
influxdb_bucket = ''

# grow specific settings
auto_water = False
moisture_target_a = 50
moisture_target_b = 50
moisture_target_c = 50